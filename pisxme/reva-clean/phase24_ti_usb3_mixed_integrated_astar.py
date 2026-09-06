"""Disposable mixed-layer integrated USB3 route for U7 orientation probes."""
from pathlib import Path
from heapq import heappush,heappop
import os,pcbnew
R=Path(__file__).resolve().parent
BASE=R/os.environ.get('P24_MIXED_BASE','PHASE24_STORAGE_ORIENTATION_U7_0_J3_270_TI.kicad_pcb')
OUT=R/os.environ.get('P24_MIXED_OUT','PHASE24_STORAGE_ORIENTATION_U7_0_J3_270_TI_MIXED_ASTAR.kicad_pcb')
F,B=pcbnew.F_Cu,pcbnew.B_Cu;STEP=.25;WIDTH=.15
JOBS=(('CM5_USB3_RX_N','128','42',F),('CM5_USB3_RX_P','130','43',F),('CM5_USB3_TX_N','140','45',B),('CM5_USB3_TX_P','142','46',B))
def V(p):return pcbnew.VECTOR2I_MM(float(p[0]),float(p[1]))
def xy(o):
 p=o if hasattr(o,'x') else o.GetPosition();return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def pad(b,r,n):return b.FindFootprintByReference(r).FindPadByNumber(n)
def net(b,n):
 for q in (n,'/CORE_CM5/'+n,'/STORAGE/'+n):
  z=b.FindNet(q)
  if z:return z
 raise RuntimeError('missing '+n)
def grid(p):return round(p[0]/STEP),round(p[1]/STEP)
def pt(g):return g[0]*STEP,g[1]*STEP
def raster(s,a,z,r=.24):
 ax,ay=grid(a);zx,zy=grid(z);k=max(abs(zx-ax),abs(zy-ay),1);q=max(1,round(r/STEP))
 for i in range(k+1):
  x=round(ax+(zx-ax)*i/k);y=round(ay+(zy-ay)*i/k)
  for dx in range(-q,q+1):
   for dy in range(-q,q+1):s.add((x+dx,y+dy))
def rect(s,p,rx,ry):
 x,y=grid(p);qx=max(1,round(rx/STEP));qy=max(1,round(ry/STEP))
 for dx in range(-qx,qx+1):
  for dy in range(-qy,qy+1):s.add((x+dx,y+dy))
def obs(b,layer):
 s=set()
 for t in b.GetTracks():
  if isinstance(t,pcbnew.PCB_VIA):raster(s,xy(t),xy(t),.42)
  elif t.GetLayer()==layer:raster(s,xy(t.GetStart()),xy(t.GetEnd()),.24)
 for f in b.GetFootprints():
  if f.GetReference() in ('J7','U7'):continue
  for p in f.Pads():
   if p.GetLayerSet().Contains(layer):
    q=p.GetSize();rect(s,xy(p),pcbnew.ToMM(q.x)/2+.16,pcbnew.ToMM(q.y)/2+.16)
 return s
def route(s,a,z):
 a=grid(a);z=grid(z)
 for c in (a,z):
  for dx in range(-2,3):
   for dy in range(-2,3):s.discard((c[0]+dx,c[1]+dy))
 q=[(0,a)];cost={a:0};prev={a:None}
 while q:
  _,c=heappop(q)
  if c==z:break
  for n in ((c[0]+1,c[1]),(c[0]-1,c[1]),(c[0],c[1]+1),(c[0],c[1]-1)):
   if not(40<=n[0]<=900 and 40<=n[1]<=700) or n in s:continue
   v=cost[c]+1
   if v<cost.get(n,10**9):cost[n]=v;prev[n]=c;heappush(q,(v+abs(n[0]-z[0])+abs(n[1]-z[1]),n))
 if z not in prev:raise RuntimeError(f'no path {a}->{z}')
 out=[];c=z
 while c is not None:out.append(pt(c));c=prev[c]
 return out[::-1]
def track(b,n,a,z,l):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(a));t.SetEnd(V(z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(n);b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
for t in list(b.GetTracks()):
 if 'CM5_USB3_' in t.GetNetname():b.Remove(t)
terms=[]
for name,j,u,l in JOBS:terms.append((name,xy(pad(b,'J7',j)),xy(pad(b,'U7',u)),net(b,name),l))
sf=obs(b,F);sb=obs(b,B)
for idx,(name,src,dst,n,l) in enumerate(terms):
 if l==F:
  sv=(74.0,src[1]);tv=(96.0,dst[1]);track(b,n,src,sv,B);via(b,n,sv);p=route(sf,sv,tv)
  for a,z in zip(p,p[1:]):track(b,n,a,z,F);raster(sf,a,z,.28)
  via(b,n,tv);track(b,n,tv,dst,F)
 else:
  tv=(96.0,dst[1]);p=route(sb,src,tv)
  for a,z in zip(p,p[1:]):track(b,n,a,z,B);raster(sb,a,z,.28)
  via(b,n,tv);track(b,n,tv,dst,F)
 print(name,'layer',l,'segments',len(p),'src',src,'dst',dst)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
