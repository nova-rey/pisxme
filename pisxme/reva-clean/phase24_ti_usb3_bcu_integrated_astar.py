"""Disposable integrated TI-U7 USB3 B.Cu corridor experiment.

Routes all four native J7-to-U7 nets on B.Cu around the retained board
obstacles, then uses ordinary through-vias and short F.Cu dogbones into the
TI lands.  No expected graph edges are authored.
"""
from pathlib import Path
from heapq import heappush, heappop
import pcbnew
import os

R=Path(__file__).resolve().parent
BASE=R/os.environ.get('P24_TI_BCU_BASE','PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_REVIEW.kicad_pcb')
OUT=R/os.environ.get('P24_TI_BCU_OUT','PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_BCU_INTEGRATED_ASTAR.kicad_pcb')
F,B=pcbnew.F_Cu,pcbnew.B_Cu; STEP=.25; WIDTH=.15
JOBS=(('CM5_USB3_RX_N','128','42'),('CM5_USB3_RX_P','130','43'),('CM5_USB3_TX_N','140','45'),('CM5_USB3_TX_P','142','46'))
def V(p): return pcbnew.VECTOR2I_MM(float(p[0]),float(p[1]))
def xy(o):
 p=o if hasattr(o,'x') else o.GetPosition(); return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def net(b,n):
 for q in (n,'/CORE_CM5/'+n,'/STORAGE/'+n):
  z=b.FindNet(q)
  if z:return z
 raise RuntimeError('missing '+n)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(n)
def grid(p): return round(p[0]/STEP),round(p[1]/STEP)
def point(g): return g[0]*STEP,g[1]*STEP
def block_line(s,a,z,r=.24):
 ax,ay=grid(a); zx,zy=grid(z); k=max(abs(zx-ax),abs(zy-ay),1); q=max(1,round(r/STEP))
 for i in range(k+1):
  x=round(ax+(zx-ax)*i/k); y=round(ay+(zy-ay)*i/k)
  for dx in range(-q,q+1):
   for dy in range(-q,q+1): s.add((x+dx,y+dy))
def block_rect(s,p,rx,ry):
 x,y=grid(p)
 for dx in range(-max(1,round(rx/STEP)),max(1,round(rx/STEP))+1):
  for dy in range(-max(1,round(ry/STEP)),max(1,round(ry/STEP))+1):s.add((x+dx,y+dy))
def obstacles(b):
 s=set()
 for t in b.GetTracks():
  if isinstance(t,pcbnew.PCB_VIA): block_line(s,xy(t),xy(t),.42)
  elif t.GetLayer()==B: block_line(s,xy(t.GetStart()),xy(t.GetEnd()),.24)
 for f in b.GetFootprints():
  if f.GetReference() in ('J7','U7'): continue
  for p in f.Pads():
   if p.GetLayerSet().Contains(B):
    q=p.GetSize(); block_rect(s,xy(p),pcbnew.ToMM(q.x)/2+.16,pcbnew.ToMM(q.y)/2+.16)
 return s
def astar(s,a,z):
 a=grid(a); z=grid(z); 
 for c in (a,z):
  for dx in range(-2,3):
   for dy in range(-2,3): s.discard((c[0]+dx,c[1]+dy))
 q=[(0,a)]; cost={a:0}; prev={a:None}
 while q:
  _,c=heappop(q)
  if c==z: break
  for n in ((c[0]+1,c[1]),(c[0]-1,c[1]),(c[0],c[1]+1),(c[0],c[1]-1)):
   if not (grid((10,10))[0]<=n[0]<=grid((235,175))[0] and grid((10,10))[1]<=n[1]<=grid((235,175))[1]) or n in s: continue
   v=cost[c]+1
   if v<cost.get(n,10**9): cost[n]=v; prev[n]=c; heappush(q,(v+abs(n[0]-z[0])+abs(n[1]-z[1]),n))
 if z not in prev: raise RuntimeError(f'no B.Cu path {a}->{z}')
 out=[]; c=z
 while c is not None: out.append(point(c)); c=prev[c]
 return out[::-1]
def track(b,n,a,z,l):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(a));t.SetEnd(V(z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(n);b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
terms=[]
for name,j,u in JOBS:
 n=net(b,name); terms.append((name,xy(pad(b,'J7',j)),xy(pad(b,'U7',u))))
for t in list(b.GetTracks()):
 if any(x in t.GetNetname() for x in ('CM5_USB3_RX_','CM5_USB3_TX_')): b.Remove(t)
s=obstacles(b)
targets=((89.0,122.8),(89.0,124.0),(89.0,126.0),(89.0,127.2))
for (name,src,dst),tv in zip(terms,targets):
 n=net(b,name)
 # Leave the carrier pad field on a dedicated monotonic dogbone before the
 # shared-board search.  Starting A* at the pad itself lets neighboring J7
 # lands become artificial crossings in an otherwise legal corridor.
 sv=(73.0, src[1])
 track(b,n,src,sv,B); via(b,n,sv); block_line(s,src,sv,.28)
 p=astar(s,sv,tv)
 for a,z in zip(p,p[1:]): track(b,n,a,z,B); block_line(s,a,z,.28)
 via(b,n,tv); track(b,n,tv,dst,F)
 print(name,'segments',len(p),'src',src,'target',dst)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
