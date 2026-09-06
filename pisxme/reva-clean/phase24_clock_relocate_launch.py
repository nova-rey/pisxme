"""Relocate the native-valid V2 clock island, then route U7 launches."""
from pathlib import Path
from heapq import heappush, heappop
import math, pcbnew
R=Path(__file__).resolve().parent
SRC=R/'PHASE24_SELECTED_MACRO_STORAGE_V26_CLOCK_V2_SOUTH40.kicad_pcb'
OUT=R/'PHASE24_SELECTED_MACRO_STORAGE_V26_CLOCK_V2_WEST_LAUNCH.kicad_pcb'
CLOCK={'/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'}
DX,DY=-20.0,-10.0; STEP=.25
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def shift(p): return V(xy(p)[0]+DX,xy(p)[1]+DY)
b=pcbnew.LoadBoard(str(SRC)); u=b.FindFootprintByReference('U7')
for ref in ('Y1','R23','C42','C43'):
 f=b.FindFootprintByReference(ref); f.SetPosition(shift(f.GetPosition()))
for item in list(b.GetTracks()):
 if item.GetNetname() not in CLOCK: continue
 if isinstance(item,pcbnew.PCB_VIA): item.SetPosition(shift(item.GetPosition()))
 else: item.SetStart(shift(item.GetStart())); item.SetEnd(shift(item.GetEnd()))
def cell(q): return round(q[0]/STEP),round(q[1]/STEP)
def pxy(c): return c[0]*STEP,c[1]*STEP
def blocked(netcode,layer):
 o=set()
 def mark(x0,x1,y0,y1):
  for x in range(math.floor(x0/STEP),math.ceil(x1/STEP)+1):
   for y in range(math.floor(y0/STEP),math.ceil(y1/STEP)+1): o.add((x,y))
 for t in b.GetTracks():
  if t.GetLayer()!=layer or t.GetNetCode()==netcode: continue
  a=xy(t.GetStart()); z=xy(t.GetEnd()); mark(min(a[0],z[0])-.2,max(a[0],z[0])+.2,min(a[1],z[1])-.2,max(a[1],z[1])+.2)
 for f in b.GetFootprints():
  for p in f.Pads():
   if p.GetNetCode()==netcode or not p.GetLayerSet().Contains(layer): continue
   q=xy(p.GetPosition()); sx=pcbnew.ToMM(p.GetSize().x); sy=pcbnew.ToMM(p.GetSize().y); mark(q[0]-sx/2-.2,q[0]+sx/2+.2,q[1]-sy/2-.2,q[1]+sy/2+.2)
 return o
def astar(a,g,occ,res):
 s=cell(a); goal=cell(g); q=[(0,s)]; prev={s:None}; cost={s:0}
 while q:
  _,z=heappop(q)
  if z==goal: break
  for n in ((z[0]+1,z[1]),(z[0]-1,z[1]),(z[0],z[1]+1),(z[0],z[1]-1)):
   if not (68/STEP<=n[0]<=122/STEP and 112/STEP<=n[1]<=170/STEP): continue
   if n!=goal and (n in occ or n in res): continue
   c=cost[z]+1
   if c<cost.get(n,10**9): cost[n]=c; prev[n]=z; heappush(q,(c+abs(n[0]-goal[0])+abs(n[1]-goal[1]),n))
 if goal not in prev: raise RuntimeError(f'no path {a}->{g}')
 path=[]; z=goal
 while z is not None: path.append(z); z=prev[z]
 return list(reversed(path))
res={pcbnew.F_Cu:set(),pcbnew.B_Cu:set()}
spec=[('54','/STORAGE/BRIDGE_XO',108.0,pcbnew.B_Cu,-.25),('52','/STORAGE/BRIDGE_XI',109.0,pcbnew.B_Cu,.75),('53','/STORAGE/BRIDGE_VSSOSC',108.5,pcbnew.F_Cu,.25)]
for num,name,oldx,layer,off in spec:
 p=next(p for p in u.Pads() if p.GetNumber()==num); net=b.FindNet(name); start=xy(p.GetPosition()); target=(oldx+DX,159.5+DY); via=(start[0]+off,start[1]+1.0) if layer==pcbnew.B_Cu else start
 path=astar(via if layer==pcbnew.B_Cu else start,target,blocked(net.GetNetCode(),layer),res[layer]); print(num,layer,len(path))
 if layer==pcbnew.B_Cu:
  v=pcbnew.PCB_VIA(b); v.SetPosition(V(*via)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(net); b.Add(v)
  t=pcbnew.PCB_TRACK(b); t.SetStart(p.GetPosition()); t.SetEnd(V(*via)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.15)); t.SetNet(net); b.Add(t)
 for a,z in zip(path,path[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*pxy(a))); t.SetEnd(V(*pxy(z))); t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(.15)); t.SetNet(net); b.Add(t); res[layer].add(z)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
