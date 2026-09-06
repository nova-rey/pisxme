"""Obstacle-aware U7 clock launch from actual pads to V2 passive tails."""
from pathlib import Path
from heapq import heappush, heappop
import math
import pcbnew
R=Path(__file__).resolve().parent
src=R/'PHASE24_SELECTED_MACRO_STORAGE_V26_CLOCK_V2_SOUTH40.kicad_pcb'
out=R/'PHASE24_SELECTED_MACRO_STORAGE_V26_CLOCK_V2_ASTAR_LAUNCH.kicad_pcb'
STEP=.25
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
b=pcbnew.LoadBoard(str(src)); u=b.FindFootprintByReference('U7')
spec=[('52','/STORAGE/BRIDGE_XI',109.0),('53','/STORAGE/BRIDGE_VSSOSC',108.5),('54','/STORAGE/BRIDGE_XO',108.0)]
def cell(q): return (round(q[0]/STEP),round(q[1]/STEP))
def xy(c): return (c[0]*STEP,c[1]*STEP)
def blocked(netcode):
 o=set()
 def mark(x0,x1,y0,y1):
  for x in range(math.floor(x0/STEP),math.ceil(x1/STEP)+1):
   for y in range(math.floor(y0/STEP),math.ceil(y1/STEP)+1): o.add((x,y))
 for t in b.GetTracks():
  if t.GetLayer()!=pcbnew.B_Cu or t.GetNetCode()==netcode: continue
  q0=mm(t.GetStart()); q1=mm(t.GetEnd()); mark(min(q0[0],q1[0])-.2,max(q0[0],q1[0])+.2,min(q0[1],q1[1])-.2,max(q0[1],q1[1])+.2)
 for f in b.GetFootprints():
  for p in f.Pads():
   if p.GetNetCode()==netcode or not p.GetLayerSet().Contains(pcbnew.B_Cu): continue
   q=mm(p.GetPosition()); sx=pcbnew.ToMM(p.GetSize().x); sy=pcbnew.ToMM(p.GetSize().y); mark(q[0]-sx/2-.2,q[0]+sx/2+.2,q[1]-sy/2-.2,q[1]+sy/2+.2)
 return o
def route(start,goal,occ,reserved):
 s=cell(start); g=cell(goal); q=[(0,s)]; prev={s:None}; cost={s:0}
 while q:
  _,u0=heappop(q)
  if u0==g: break
  for v in ((u0[0]+1,u0[1]),(u0[0]-1,u0[1]),(u0[0],u0[1]+1),(u0[0],u0[1]-1)):
   if not (88/STEP<=v[0]<=120/STEP and 116/STEP<=v[1]<=164/STEP): continue
   if v!=g and (v in occ or v in reserved): continue
   nc=cost[u0]+1
   if nc<cost.get(v,10**9): cost[v]=nc; prev[v]=u0; heappush(q,(nc+abs(v[0]-g[0])+abs(v[1]-g[1]),v))
 if g not in prev: raise RuntimeError(f'no path {start}->{goal}')
 path=[]; z=g
 while z is not None: path.append(z); z=prev[z]
 return list(reversed(path))
reserved=set()
for num,name,xgoal in spec:
 p=next(p for p in u.Pads() if p.GetNumber()==num); n=b.FindNet(name); s=mm(p.GetPosition())
 via=(s[0]+({'52':.75,'53':.25,'54':-.25}[num]),s[1]+1.0)
 goal=(xgoal,159.5)
 occ=blocked(n.GetNetCode())
 path=route(via,goal,occ,reserved); print(num,len(path))
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*via)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
 t=pcbnew.PCB_TRACK(b); t.SetStart(p.GetPosition()); t.SetEnd(V(*via)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.15)); t.SetNet(n); b.Add(t)
 for a,z in zip(path,path[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*xy(a))); t.SetEnd(V(*xy(z))); t.SetLayer(pcbnew.B_Cu); t.SetWidth(pcbnew.FromMM(.15)); t.SetNet(n); b.Add(t); reserved.add(z)
b.BuildListOfNets(); b.Save(str(out)); print(out)
