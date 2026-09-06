"""Integrate a clipped native CM5IO USB3 source escape with the selected macro.

The source-side paths are copied from the saved official CM5IO-derived
fixture and clipped at x=77 mm.  The remaining four paths are then searched
on B.Cu around the real integrated-board obstacles.  This is disposable
route-development evidence only.
"""
from pathlib import Path
from heapq import heappush, heappop
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_REVIEW.kicad_pcb'
ORACLE=R/'PHASE24_USB3_CM5IO_SOURCE_ESCAPE_U7_ROT0_CLEANPASS.kicad_pcb'
OUT=R/'PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_CM5IO_SOURCE_INTEGRATED.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; STEP=.25; WIDTH=.15; CUT=77.0
JOBS=(('CM5_USB3_RX_N','128','42'),('CM5_USB3_RX_P','130','43'),('CM5_USB3_TX_N','140','45'),('CM5_USB3_TX_P','142','46'))
def V(p): return pcbnew.VECTOR2I_MM(float(p[0]),float(p[1]))
def xy(o):
 p=o if hasattr(o,'x') else o.GetPosition(); return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(n)
def net(b,n):
 for q in (n,'/CORE_CM5/'+n,'/STORAGE/'+n):
  z=b.FindNet(q)
  if z:return z
 raise RuntimeError('missing '+n)
def grid(p): return round(p[0]/STEP),round(p[1]/STEP)
def point(g): return g[0]*STEP,g[1]*STEP
def block_line(s,a,z,r=.24):
 ax,ay=grid(a);zx,zy=grid(z);k=max(abs(zx-ax),abs(zy-ay),1);q=max(1,round(r/STEP))
 for i in range(k+1):
  x=round(ax+(zx-ax)*i/k);y=round(ay+(zy-ay)*i/k)
  for dx in range(-q,q+1):
   for dy in range(-q,q+1):s.add((x+dx,y+dy))
def block_rect(s,p,rx,ry):
 x,y=grid(p);qx=max(1,round(rx/STEP));qy=max(1,round(ry/STEP))
 for dx in range(-qx,qx+1):
  for dy in range(-qy,qy+1):s.add((x+dx,y+dy))
def add_track(b,n,a,z,l):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(a));t.SetEnd(V(z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(n);b.Add(t)
def add_via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
def clip_segment(a,z):
 ax,ay=a;zx,zy=z
 if ax<=CUT and zx<=CUT:return (a,z)
 if ax>CUT and zx>CUT:return None
 if ax==zx:return None
 q=(CUT-ax)/(zx-ax); c=(CUT,ay+q*(zy-ay))
 return (a,c) if ax<=CUT else (c,z)
def astar(blocked,a,z):
 a=grid(a);z=grid(z)
 for c in (a,z):
  for dx in range(-2,3):
   for dy in range(-2,3):blocked.discard((c[0]+dx,c[1]+dy))
 q=[(0,a)];cost={a:0};prev={a:None}
 while q:
  _,c=heappop(q)
  if c==z:break
  for n in ((c[0]+1,c[1]),(c[0]-1,c[1]),(c[0],c[1]+1),(c[0],c[1]-1)):
   if not (grid((10,10))[0]<=n[0]<=grid((235,175))[0] and grid((10,10))[1]<=n[1]<=grid((235,175))[1]) or n in blocked:continue
   v=cost[c]+1
   if v<cost.get(n,10**9):cost[n]=v;prev[n]=c;heappush(q,(v+abs(n[0]-z[0])+abs(n[1]-z[1]),n))
 if z not in prev:raise RuntimeError(f'no integrated B.Cu path {a}->{z}')
 out=[];c=z
 while c is not None:out.append(point(c));c=prev[c]
 return out[::-1]
def obstacles(b):
 s=set()
 for t in b.GetTracks():
  if isinstance(t,pcbnew.PCB_VIA):block_line(s,xy(t),xy(t),.42)
  elif t.GetLayer()==B:block_line(s,xy(t.GetStart()),xy(t.GetEnd()),.24)
 for f in b.GetFootprints():
  if f.GetReference() in ('J7','U7'):continue
  for p in f.Pads():
   if p.GetLayerSet().Contains(B):
    q=p.GetSize();block_rect(s,xy(p),pcbnew.ToMM(q.x)/2+.16,pcbnew.ToMM(q.y)/2+.16)
 return s
oracle=pcbnew.LoadBoard(str(ORACLE));b=pcbnew.LoadBoard(str(BASE))
for t in list(b.GetTracks()):
 if any(x in t.GetNetname() for x in ('CM5_USB3_RX_','CM5_USB3_TX_')):b.Remove(t)
ends={}
for name,j,u in JOBS:
 n=net(b,name); op=net(oracle,name)
 candidates=[]
 for t in oracle.GetTracks():
  if t.GetNetname()!=op.GetNetname():continue
  if isinstance(t,pcbnew.PCB_VIA):
   p=xy(t)
   if p[0]<=CUT:candidates.append(('via',p,t.GetWidth(t.TopLayer()),t.GetDrill(),t.TopLayer(),t.BottomLayer()))
  else:
   clipped=clip_segment(xy(t.GetStart()),xy(t.GetEnd()))
   if clipped is not None:
    a,z=clipped;candidates.append(('track',a,z,t.GetLayer(),t.GetWidth()))
 for rec in candidates:
  if rec[0]=='via':
   _,p,w,d,top,bottom=rec;q=pcbnew.PCB_VIA(b);q.SetPosition(V(p));q.SetWidth(w);q.SetDrill(d);q.SetLayerPair(top,bottom);q.SetNet(n);b.Add(q)
  else:
   _,a,z,l,w=rec;add_track(b,n,a,z,l)
 # Use the rightmost clipped native point as the integrated handoff.
 pts=[]
 for rec in candidates:
  if rec[0]=='via':pts.append(rec[1])
  else:pts.extend((rec[1],rec[2]))
 hand=max(pts,key=lambda p:(p[0],p[1]))
 ends[name]=(n,hand,xy(pad(b,'U7',u)))
print('native source handoffs', {k:v[1] for k,v in ends.items()})
s=obstacles(b)
targets=((89.0,122.8),(89.0,124.0),(89.0,126.0),(89.0,127.2))
for (name,(n,hand,dst)),tv in zip(ends.items(),targets):
 add_via(b,n,hand);p=astar(s,hand,tv)
 for a,z in zip(p,p[1:]):add_track(b,n,a,z,B);block_line(s,a,z,.28)
 add_via(b,n,tv);add_track(b,n,tv,dst,F)
 print(name,'segments',len(p),'handoff',hand,'target',dst)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
