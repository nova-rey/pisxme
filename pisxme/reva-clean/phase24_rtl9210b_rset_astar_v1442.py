"""V1442: net/layer-aware A* RSET escape on the saved V1428 geometry."""
from pathlib import Path
from heapq import heappush, heappop
import math, pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RSET_ASTAR_V1442.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; STEP=.20; R=.25
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(q): return q.x/1e6,q.y/1e6
def near(a,b): return (a[0]-b[0])**2+(a[1]-b[1])**2 < .16
board=pcbnew.LoadBoard(str(BASE)); net=board.FindNet('RSET'); assert net
def pad(ref,num):
 f=next(x for x in board.GetFootprints() if x.GetReference()==ref)
 return xy(next(p for p in f.Pads() if p.GetPadName()==num).GetPosition())
start=pad('U1','51'); goal=pad('R1','1')
X0,X1,Y0,Y1=78.,108.,52.,78.
def cell(p): return round((p[0]-X0)/STEP),round((p[1]-Y0)/STEP)
def pos(c): return (X0+c[0]*STEP,Y0+c[1]*STEP)
S=cell(start); G=cell(goal)
blocked={(l,x,y) for l in (0,1) for x in range(int((X1-X0)/STEP)+1) for y in range(int((Y1-Y0)/STEP)+1) if False}
def mark_circle(l,cx,cy,r):
 for x in range(max(0,int((cx-r-X0)/STEP)-1),min(int((X1-X0)/STEP),int((cx+r-X0)/STEP)+1)+1):
  for y in range(max(0,int((cy-r-Y0)/STEP)-1),min(int((Y1-Y0)/STEP),int((cy+r-Y0)/STEP)+1)+1):
   if (pos((x,y))[0]-cx)**2+(pos((x,y))[1]-cy)**2 <= r*r: blocked.add((l,x,y))
def mark_seg(l,a,b,r):
 dx,dy=b[0]-a[0],b[1]-a[1]; n=max(1,int(math.hypot(dx,dy)/STEP*3))
 for i in range(n+1): mark_circle(l,a[0]+dx*i/n,a[1]+dy*i/n,r)
for t in board.GetTracks():
 if t.GetNet()==net: continue
 if isinstance(t,pcbnew.PCB_VIA):
  q=xy(t.GetPosition()); mark_circle(0,q[0],q[1],R); mark_circle(1,q[0],q[1],R); continue
 l=0 if t.GetLayer()==F else 1 if t.GetLayer()==B else None
 if l is not None: mark_seg(l,xy(t.GetStart()),xy(t.GetEnd()),R)
for f in board.GetFootprints():
 for p in f.Pads():
  if p.GetNet()==net: continue
  q=xy(p.GetPosition()); sz=p.GetSize(); rr=max(sz.x,sz.y)/2e6+R
  for l in (0,1) if p.GetLayerSet().Contains(F) and p.GetLayerSet().Contains(B) else (0 if p.GetLayerSet().Contains(F) else 1,): mark_circle(l,q[0],q[1],rr)
for l in (0,1): blocked.discard((l,*S)); blocked.discard((l,*G))
Q=[(0,S[0],S[1],0)]; prev={(0,*S):None}; cost={(0,*S):0}; end=None
while Q:
 _,x,y,l=heappop(Q); state=(l,x,y)
 if (x,y)==G: end=state; break
 for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
  nx,ny=x+dx,y+dy
  if not (0<=nx<=int((X1-X0)/STEP) and 0<=ny<=int((Y1-Y0)/STEP)): continue
  ns=(l,nx,ny)
  if ns in blocked: continue
  nc=cost[state]+math.hypot(dx,dy)
  if nc<cost.get(ns,1e9): cost[ns]=nc; prev[ns]=state; heappush(Q,(nc+math.hypot(nx-G[0],ny-G[1]),nx,ny,l))
  ns=(1-l,x,y)
  if ns not in blocked and cost[state]+5<cost.get(ns,1e9): cost[ns]=cost[state]+5; prev[ns]=state; heappush(Q,(cost[ns]+math.hypot(x-G[0],y-G[1]),x,y,1-l))
assert end is not None, 'no A* path'
path=[]
while end is not None: path.append(end); end=prev[end]
path.reverse();
def addseg(a,z,l):
 q=pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F if l==0 else B); q.SetWidth(pcbnew.FromMM(.20)); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
for a,z in zip(path,path[1:]):
 if a[0]==z[0]: addseg(pos(a[1:]),pos(z[1:]),a[0])
 else:
  q=pcbnew.PCB_VIA(board); q.SetPosition(P(*pos(a[1:]))); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
board.BuildListOfNets(); pcbnew.ZONE_FILLER(board).Fill(board.Zones()); board.Save(str(OUT)); print(OUT,'steps',len(path),'cost',round(cost[path[-1]],1))
