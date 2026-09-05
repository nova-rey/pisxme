"""Obstacle-aware three-net clock escape probe; disposable, no production edits."""
from pathlib import Path
from heapq import heappush,heappop
import math,pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'; OUT=R/'PHASE24_CLOCK_ASTAR_NEARWEST.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def main():
 b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7'); u.SetOrientationDegrees(180)
 io=pcbnew.PCB_IO_KICAD_SEXPR(); y=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),'Crystal_3225_4Pad'); y.SetReference('Y1'); y.SetPosition(V(108,130)); b.Add(y)
 names={'XI':'/STORAGE/BRIDGE_XI','VS':'/STORAGE/BRIDGE_VSSOSC','XO':'/STORAGE/BRIDGE_XO'}; nets={}
 for k,v in names.items():
  nets[k]=b.FindNet(v)
  if nets[k] is None:
   nets[k]=pcbnew.NETINFO_ITEM(b,v); nets[k].SetNetCode(b.GetNetCount()+1); b.Add(nets[k])
 for p in y.Pads():
  k={'1':'XI','2':'VS','3':'XO','4':'VS'}[str(p.GetNumber())]; p.SetNet(nets[k]); p.SetNetCode(nets[k].GetNetCode()); ls=pcbnew.LSET(); ls.AddLayer(pcbnew.B_Cu); p.SetLayerSet(ls)
 sources={'XI':pad(u,'52'),'VS':pad(u,'53'),'XO':pad(u,'54')}; targets={'XI':pad(y,'1'),'VS':pad(y,'4'),'XO':pad(y,'3')}
 for k,p in sources.items(): p.SetNet(nets[k]); p.SetNetCode(nets[k].GetNetCode())
 seeds={'XI':(126.5,127.0),'VS':(122.5,127.0),'XO':(128.0,126.0)}
 # Grid chosen fine enough for the package field; coarse enough to keep the
 # search bounded. Existing item bboxes are conservatively inflated.
 step=.25; xmin,xmax,ymin,ymax=95,140,100,150
 def cell(p): return (round(xy(p)[0]/step),round(xy(p)[1]/step))
 occ={pcbnew.F_Cu:set(),pcbnew.B_Cu:set()}
 def reserve(layer,gx,gy):
  for dx in (-1,0,1):
   for dy in (-1,0,1): occ[layer].add((gx+dx,gy+dy))
 def reserve_via(gx,gy):
  for layer in (pcbnew.F_Cu,pcbnew.B_Cu):
   for dx in (-3,-2,-1,0,1,2,3):
    for dy in (-3,-2,-1,0,1,2,3): occ[layer].add((gx+dx,gy+dy))
 def mark(layer,ax,bx,ay,by):
  for gx in range(math.floor(ax/step),math.ceil(bx/step)+1):
   for gy in range(math.floor(ay/step),math.ceil(by/step)+1): occ[layer].add((gx,gy))
 for item in b.GetTracks():
  if item.GetLayer() in occ:
   bb=item.GetBoundingBox(); mark(item.GetLayer(),pcbnew.ToMM(bb.GetX())-.18,pcbnew.ToMM(bb.GetRight())+.18,pcbnew.ToMM(bb.GetY())-.18,pcbnew.ToMM(bb.GetBottom())+.18)
 for f in b.GetFootprints():
  for p in f.Pads():
   if p.GetLayer() not in occ: continue
   if (f is u and p in sources.values()) or (f is y and p in targets.values()): continue
   px,py=xy(p); sz=p.GetSize()
   mark(p.GetLayer(),px-pcbnew.ToMM(sz.x)/2-.18,px+pcbnew.ToMM(sz.x)/2+.18,py-pcbnew.ToMM(sz.y)/2-.18,py+pcbnew.ToMM(sz.y)/2+.18)
 def blocked(g,layer,skip):
  return g in occ[layer]
 def route(k):
  start=cell(sources[k]); goal=cell(targets[k]);
  if k=='XI': goal=tuple(round(v/step) for v in (104.0,129.15))
  if k=='XO': goal=tuple(round(v/step) for v in (112.0,130.0))
  seed=cell_point=tuple(round(v/step) for v in seeds[k]); goal_layer=pcbnew.B_Cu
  skips=[(u,sources[k]),(y,targets[k])]; start_state=(seed[0],seed[1],pcbnew.B_Cu); goal_state=(goal[0],goal[1],goal_layer); q=[(0,start_state)]; prev={start_state:None}; cost={start_state:0}
  while q:
   _,cur=heappop(q)
   if cur==goal_state: break
   x,y0,l=cur
   moves=[(x+1,y0,l),(x-1,y0,l),(x,y0+1,l),(x,y0-1,l),(x,y0,pcbnew.B_Cu if l==pcbnew.F_Cu else pcbnew.F_Cu)]
   for nx,ny,nl in moves:
    if not (int(xmin/step)<=nx<=int(xmax/step) and int(ymin/step)<=ny<=int(ymax/step)): continue
    if nl!=l and (nx,ny) in (start,goal): continue
    if any(abs(nx-sx)<=2 and abs(ny-sy)<=2 for sk,(sx,sy) in [(sk,tuple(round(v/step) for v in seeds[sk])) for sk in seeds] if sk!=k): continue
    if nl==l and (nx,ny)!=goal and blocked((nx,ny),nl,skips): continue
    nc=cost[cur]+(8 if nl!=l else 1); ns=(nx,ny,nl)
    if nc<cost.get(ns,10**9):
     cost[ns]=nc; prev[ns]=cur; heappush(q,(nc+abs(nx-goal[0])+abs(ny-goal[1]),ns))
  if goal_state not in prev: raise RuntimeError('no route '+k)
  path=[]; z=goal_state
  while z is not None: path.append(z); z=prev[z]
  path.reverse(); return path
 def addpath(k,path):
  net=nets[k]
  for a,z in zip(path,path[1:]):
   if a[2]!=z[2]:
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(a[0]*step,a[1]*step)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(net); b.Add(v)
    reserve_via(a[0],a[1])
   else:
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(a[0]*step,a[1]*step)); t.SetEnd(V(z[0]*step,z[1]*step)); t.SetLayer(a[2]); t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(net); b.Add(t)
    for gx in range(min(a[0],z[0]),max(a[0],z[0])+1):
     for gy in range(min(a[1],z[1]),max(a[1],z[1])+1): reserve(a[2],gx,gy)
 def seedpath(k):
  net=nets[k]; src=xy(sources[k]); dst=seeds[k]
  bends={'XI':[(123,134.5),dst],
         'VS':[(122.5,133.5),dst],
         'XO':[(122.0,126.0),(128.0,126.0)] if k=='XO' else []}[k]
  a=src
  for z in bends:
   t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(net); b.Add(t)
   for gx in range(math.floor(min(a[0],z[0])/step),math.ceil(max(a[0],z[0])/step)+1):
    for gy in range(math.floor(min(a[1],z[1])/step),math.ceil(max(a[1],z[1])/step)+1): reserve(pcbnew.F_Cu,gx,gy)
   a=z
  v=pcbnew.PCB_VIA(b); v.SetPosition(V(*dst)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(net); b.Add(v)
  cell_point=tuple(round(v/step) for v in dst); reserve_via(*cell_point)
 for k in ('XI','VS','XO'):
  path=route(k); print(k,len(path),path[0],path[-1]); seedpath(k); addpath(k,path)
 # Approach XI from the west side of the crystal; this prevents the XI tail
 # from sharing the narrow pad-row corridor with the VSSOSC bridge.
 xi=targets['XI']; t=pcbnew.PCB_TRACK(b); t.SetStart(V(104.0,129.15)); t.SetEnd(V(*xy(xi))); t.SetLayer(pcbnew.B_Cu); t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(nets['XI']); b.Add(t)
 p2=xy(pad(y,'2')); p4=xy(pad(y,'4')); vss=nets['VS']
 for a,z in [(p2,(105.0,135.0)),((105.0,135.0),(118.0,135.0)),((118.0,135.0),(118.0,129.15)),((118.0,129.15),p4)]:
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.B_Cu); t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(vss); b.Add(t)
 xo=nets['XO']; t=pcbnew.PCB_TRACK(b); t.SetStart(V(112.0,130.0)); t.SetEnd(V(*xy(targets['XO']))); t.SetLayer(pcbnew.B_Cu); t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(xo); b.Add(t)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
