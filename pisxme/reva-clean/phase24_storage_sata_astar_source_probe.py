"""Disposable native-pad A* routing probe for the eight SATA selector legs."""
from pathlib import Path
from heapq import heappush, heappop
import os
import pcbnew, math
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_VCCK_LOCAL_V1.kicad_pcb'; OUT=R/os.environ.get('PISXME_SATA_ASTAR_OUT','PHASE24_STORAGE_SATA_ASTAR_V1.kicad_pcb'); F,B=pcbnew.F_Cu,pcbnew.B_Cu; STEP=.25
def V(q): return pcbnew.VECTOR2I(int(round(q[0]*1e6)),int(round(q[1]*1e6)))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def P(b,r,n): return xy(b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition())
def g(q): return round(q[0]/STEP),round(q[1]/STEP)
def q(c): return c[0]*STEP,c[1]*STEP
def block(s,z,r=.3):
 x,y=g(z); rr=max(1,math.ceil(r/STEP))
 for dx in range(-rr,rr+1):
  for dy in range(-rr,rr+1): s.add((x+dx,y+dy))
def line(s,a,z):
 a,z=g(a),g(z); k=max(abs(z[0]-a[0]),abs(z[1]-a[1]),1)
 for i in range(k+1): block(s,q((round(a[0]+(z[0]-a[0])*i/k),round(a[1]+(z[1]-a[1])*i/k))))
def occ(b):
 o={F:set(),B:set()}
 for t in b.GetTracks():
  if isinstance(t,pcbnew.PCB_VIA): block(o[F],xy(t.GetPosition()),.4); block(o[B],xy(t.GetPosition()),.4)
  else: line(o[t.GetLayer()],xy(t.GetStart()),xy(t.GetEnd()))
 for f in b.GetFootprints():
  for p in f.Pads():
   r=max(xy(p.GetSize()))/2+.25; z=xy(p.GetPosition())
   # Respect the saved pad layer set.  Blocking an F.Cu-only SMD pad on B.Cu
   # made the prior search reject legal underside corridors.
   if p.IsOnLayer(F): block(o[F],z,r)
   if p.IsOnLayer(B): block(o[B],z,r)
 return o
def route(o,a,z,start=F,goal=F):
 s=(*g(a),start); t=(*g(z),goal); l={F:set(o[F]),B:set(o[B])}
 for x,y,lay in ((s[0],s[1],start),(t[0],t[1],goal)):
  for dx in range(-8,9):
   for dy in range(-8,9): l[lay].discard((x+dx,y+dy))
 pq=[(0,s)]; prev={s:None}; cost={s:0}; bound=(g((70,95)),g((230,175)))
 while pq:
  _,c=heappop(pq)
  if c==t: break
  x,y,lay=c
  for nx,ny,nlay in ((x+1,y,lay),(x-1,y,lay),(x,y+1,lay),(x,y-1,lay),(x,y,B if lay==F else F)):
   if not(bound[0][0]<=nx<=bound[1][0] and bound[0][1]<=ny<=bound[1][1]) or (nx,ny) in l[nlay] and (nx,ny,nlay)!=t: continue
   n=(nx,ny,nlay); nc=cost[c]+1+(45 if nlay!=lay else 0)
   if nc<cost.get(n,10**9): cost[n]=nc; prev[n]=c; heappush(pq,(nc+abs(nx-t[0])+abs(ny-t[1]),n))
 if t not in prev: raise RuntimeError(f'no route {a}->{z}')
 out=[]; c=t
 while c is not None: out.append(c); c=prev[c]
 return out[::-1]
def emit(b,n,path):
 last=None; seen=set()
 for a,z in zip(path,path[1:]):
  if a[2]!=z[2]:
   p=q(a[:2])
   if p not in seen:
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v); seen.add(p)
   last=None; continue
  lay=a[2]; a,z=q(a[:2]),q(z[:2])
  if last is None:last=a
  if last!=z:
   t=pcbnew.PCB_TRACK(b); t.SetStart(V(last)); t.SetEnd(V(z)); t.SetLayer(lay); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t); last=z
def direct(b,n,pts,lay):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(a)); t.SetEnd(V(z)); t.SetLayer(lay); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(BASE))
def N(name):
 n=b.FindNet(name) or b.FindNet('/STORAGE/'+name)
 if not n: raise RuntimeError('missing net '+name)
 return n
for t in list(b.GetTracks()):
 if any(x in t.GetNetname() for x in (('BRIDGE_SATA_',) if os.environ.get('PISXME_SATA_ASTAR_SAFE_EXITS')=='1' else ('BRIDGE_SATA_','TUSB_SATA_'))): b.RemoveNative(t)
jobs=[('BRIDGE_SATA_RX_P','U7','60','C32','2'),('BRIDGE_SATA_RX_N','U7','59','C33','2'),('BRIDGE_SATA_TX_P','U7','57','C30','2'),('BRIDGE_SATA_TX_N','U7','56','C31','2'),('TUSB_SATA_RXP','C32','1','U13','36'),('TUSB_SATA_RXN','C33','1','U13','35'),('TUSB_SATA_TXP','C30','1','U13','38'),('TUSB_SATA_TXN','C31','1','U13','37')]
if os.environ.get('PISXME_SATA_ASTAR_SAFE_EXITS')=='1':
 # Keep the known-good U7 pad dogbones and search only after the explicit
 # through-via. This prevents the grid search from relaxing through adjacent
 # QFN pads.
 safe={'BRIDGE_SATA_RX_P':('60',(94.6,127.8),(93.7,129.4),'C32'),
       'BRIDGE_SATA_RX_N':('59',(95.0,127.8),(94.3,130.0),'C33'),
       'BRIDGE_SATA_TX_P':('57',(95.8,127.8),(96.5,129.4),'C30'),
       'BRIDGE_SATA_TX_N':('56',(96.2,127.8),(97.1,129.4),'C31')}
 for name,(pin,source,sv,cap) in safe.items():
  n=N(name); direct(b,n,[source,(source[0],source[1]+.9),sv],F); v=pcbnew.PCB_VIA(b); v.SetPosition(V(sv)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
  pth=route(occ(b),sv,P(b,cap,'2'),B,F); print(name,len(pth)); emit(b,n,pth)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT); raise SystemExit
for name,ra,pa,rb,pb in jobs:
 n=N(name); path=route(occ(b),P(b,ra,pa),P(b,rb,pb)); print(name,len(path)); emit(b,n,path)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
