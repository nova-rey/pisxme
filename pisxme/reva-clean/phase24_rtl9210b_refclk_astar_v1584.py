"""V1584: obstacle-aware fixed-orientation REFCLK pair experiment.

This is deliberately disposable.  It builds its obstacle map from the saved
PCB's native pads, tracks, and vias instead of assuming that a coordinate
corridor is empty.
"""
from pathlib import Path
from heapq import heappush, heappop
from math import hypot
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_HANDOFF_TO_J1_ASTAR_V1592.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
STEP=.25; X0,X1=84.,145.; Y0,Y1=38.,96.; W=.20; C=.20; VIA=.60
LAYERS=(F,B)
def mm(v): return pcbnew.ToMM(v)
def xy(v): return (mm(v.x),mm(v.y))
def idx(x,y): return (round((x-X0)/STEP),round((y-Y0)/STEP))
def pos(k): return (X0+k[0]*STEP,Y0+k[1]*STEP)
def clear_pad(obs,pad):
 px,py=xy(pad.GetPosition()); sx,sy=xy(pad.GetSize())
 for ix in range(round((X1-X0)/STEP)+1):
  for iy in range(round((Y1-Y0)/STEP)+1):
   x,y=pos((ix,iy))
   if abs(x-px)<=sx/2+.03 and abs(y-py)<=sy/2+.03:
    for l in LAYERS: obs[l].discard((ix,iy))
def segdist(px,py,ax,ay,bx,by):
 dx=bx-ax; dy=by-ay
 if dx==dy==0:return hypot(px-ax,py-ay)
 t=max(0,min(1,((px-ax)*dx+(py-ay)*dy)/(dx*dx+dy*dy)))
 return hypot(px-(ax+t*dx),py-(ay+t*dy))

def obstacle_map(board, own):
 obs={l:set() for l in LAYERS}
 def mark(l,fn):
  for ix in range(round((X1-X0)/STEP)+1):
   for iy in range(round((Y1-Y0)/STEP)+1):
    x,y=pos((ix,iy))
    if fn(x,y): obs[l].add((ix,iy))
 for fp in board.Footprints():
  for p in fp.Pads():
   px,py=xy(p.GetPosition()); sx,sy=xy(p.GetSize())
   rad=max(sx,sy)/2+C
   layers=list(p.GetLayerSet()) if hasattr(p.GetLayerSet(),'__iter__') else []
   for l in LAYERS:
    if p.IsOnLayer(l): mark(l,lambda x,y,px=px,py=py,r=rad:hypot(x-px,y-py)<=r)
 for q in board.GetTracks():
  if q.GetNetname() in own: continue
  a=xy(q.GetStart()); z=xy(q.GetEnd())
  if type(q).__name__=='PCB_VIA':
   r=mm(q.GetWidth())/2+C
   for l in LAYERS: mark(l,lambda x,y,a=a,r=r:hypot(x-a[0],y-a[1])<=r)
  else:
   r=mm(q.GetWidth())/2+C
   l=q.GetLayer()
   if l in LAYERS: mark(l,lambda x,y,a=a,z=z,r=r:segdist(x,y,*a,*z)<=r)
 return obs

def astar(obs, reserved, start, goal):
 start=(idx(*start),0); goal=(idx(*goal),0)
 pq=[]; heappush(pq,(0,start)); prev={}; cost={start:0}
 while pq:
  _,state=heappop(pq); (cell,li)=state
  if state==goal:
   path=[]
   while state in prev: path.append(state); state=prev[state]
   path.append(start); return list(reversed(path))
  x,y=cell
  for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
   n=(x+dx,y+dy); px,py=pos(n) if 0<=n[0]<=round((X1-X0)/STEP) and 0<=n[1]<=round((Y1-Y0)/STEP) else (999,999)
   if not (X0<=px<=X1 and Y0<=py<=Y1): continue
   if n in obs[LAYERS[li]] or n in reserved[LAYERS[li]]: continue
   ns=(n,li); nc=cost[state]+1
   if nc<cost.get(ns,10**9): prev[ns]=state;cost[ns]=nc;heappush(pq,(nc+hypot(n[0]-goal[0][0],n[1]-goal[0][1]),ns))
  nli=1-li; px,py=pos(cell)
  if cell not in obs[LAYERS[nli]] and cell not in reserved[LAYERS[nli]]:
   ns=(cell,nli); nc=cost[state]+8
   if nc<cost.get(ns,10**9): prev[ns]=state;cost[ns]=nc;heappush(pq,(nc+hypot(x-goal[0][0],y-goal[0][1]),ns))
 raise RuntimeError(f'no route {start}->{goal}')

def add_track(board,net,layer,a,z):
 q=pcbnew.PCB_TRACK(board);q.SetStart(pcbnew.VECTOR2I_MM(*a));q.SetEnd(pcbnew.VECTOR2I_MM(*z));q.SetLayer(layer);q.SetWidth(pcbnew.FromMM(W));q.SetNet(net);q.SetNetCode(net.GetNetCode());board.Add(q)
def add_via(board,net,a):
 q=pcbnew.PCB_VIA(board);q.SetPosition(pcbnew.VECTOR2I_MM(*a));q.SetWidth(pcbnew.FromMM(VIA));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(net);q.SetNetCode(net.GetNetCode());board.Add(q)

def emit(board,net,path,source,target,reserved):
 points=[]; last=None
 for (cell,li) in path:
  p=pos(cell)
  if last is None: points=[(li,p)];last=(cell,li);continue
  if li!=last[1]: add_via(board,net,pos(cell));points.append((li,p))
  else: points.append((li,p))
  last=(cell,li)
 # connect exact pads to path endpoints, then coalesce collinear runs
 points[0]=(points[0][0],source); points[-1]=(points[-1][0],target)
 for (la,a),(lb,z) in zip(points,points[1:]):
  if la==lb and a!=z:add_track(board,net,LAYERS[la],a,z)

b=pcbnew.LoadBoard(str(BASE)); own={'REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXP','LANE0_TXN'}
for q in list(b.GetTracks()):
 if q.GetNetname() in own: b.RemoveNative(q)
for pad in b.FindFootprintByReference('U1').Pads(): pad.SetLocalClearance(pcbnew.FromMM(.15))
obs=obstacle_map(b,own); reserved={F:set(),B:set()}
for name,source,target in (
 ('REFCLK_P',(85.,70.4),(137.25,62.725)),
 ('LANE0_TXN',(85.,72.8),(135.25,62.725)),
 ('LANE0_RXP',(85.,71.6),(134.25,62.725)),
 ('LANE0_RXN',(85.,72.0),(133.75,62.725)),
 ('REFCLK_N',(85.,70.8),(136.75,62.725)),
 ('LANE0_TXP',(85.,73.2),(135.75,62.725)),
):
 net=b.FindNet(name)
 # Permit the actual endpoint pad rectangles only; neighboring connector
 # pads remain physical obstacles in the native geometry map.
 sp=next(p for fp in b.Footprints() for p in fp.Pads()
         if p.GetNetname()==name and abs(mm(p.GetPosition().x)-source[0])<.01
         and abs(mm(p.GetPosition().y)-source[1])<.01)
 tp=next(p for fp in b.Footprints() for p in fp.Pads()
         if p.GetNetname()==name and abs(mm(p.GetPosition().x)-target[0])<.01
         and abs(mm(p.GetPosition().y)-target[1])<.01)
 clear_pad(obs,sp); clear_pad(obs,tp)
 path=astar(obs,reserved,source,target); emit(b,net,path,source,target,reserved)
 # Diagnostic multi-net search: reserve the centerline only. Native DRC will
 # decide whether the resulting physical clearance is legal.
 for cell,li in path:
  reserved[LAYERS[li]].add(cell)
 print(name,'steps',len(path),'transitions',sum(a[1]!=b[1] for a,b in zip(path,path[1:])))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
