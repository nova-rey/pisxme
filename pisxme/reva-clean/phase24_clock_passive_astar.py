"""Connect remaining U7 clock passive pads with a B.Cu obstacle search."""
from pathlib import Path
from heapq import heappush,heappop
import math
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_CLOCK_XI_XO_VS_ASTAR_PROBE.kicad_pcb'; OUT=R/'PHASE24_CLOCK_COMPLETE_PASSIVE_ASTAR.kicad_pcb'; STEP=.25
N={'XI':'/STORAGE/BRIDGE_XI','XO':'/STORAGE/BRIDGE_XO','VS':'/STORAGE/BRIDGE_VSSOSC'}
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def P(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def G(q): return round(q[0]/STEP),round(q[1]/STEP)
def XY(g): return g[0]*STEP,g[1]*STEP
def main():
 b=pcbnew.LoadBoard(str(BASE)); nets={k:b.FindNet(v) for k,v in N.items()}; fps={r:b.FindFootprintByReference(r) for r in ('Y1','R23','C42','C43')}; occ=set()
 def mark(a,z,inflate=.12):
  for x in range(math.floor((min(a[0],z[0])-inflate)/STEP),math.ceil((max(a[0],z[0])+inflate)/STEP)+1):
   for y in range(math.floor((min(a[1],z[1])-inflate)/STEP),math.ceil((max(a[1],z[1])+inflate)/STEP)+1): occ.add((x,y))
 for item in b.GetTracks():
  if type(item).__name__=='PCB_VIA':
   if item.GetNetname() not in N.values():
    q=mm(item.GetPosition()); mark(q,q,.35)
  elif item.GetNetname() not in N.values(): mark(mm(item.GetStart()),mm(item.GetEnd()))
 for fp in b.GetFootprints():
  for p in fp.Pads():
   if p.GetNetname() in N.values(): continue
   q=mm(p.GetPosition()); s=mm(p.GetSize()); mark((q[0]-s[0]/2,q[1]-s[1]/2),(q[0]+s[0]/2,q[1]+s[1]/2),.18)
 def route(start,goal):
  s=G(start); g=G(goal)
  for dx in range(-3,4):
   for dy in range(-3,4): occ.discard((s[0]+dx,s[1]+dy))
  q=[(0,s)]; prev={s:None}; cost={s:0}; lo=G((90,115)); hi=G((130,145))
  while q:
   _,cur=heappop(q)
   if cur==g: break
   x,y=cur
   for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
    if not(lo[0]<=nx<=hi[0] and lo[1]<=ny<=hi[1]) or ((nx,ny) in occ and (nx,ny)!=g): continue
    nc=cost[cur]+1; ns=(nx,ny)
    if nc<cost.get(ns,10**9): cost[ns]=nc; prev[ns]=cur; heappush(q,(nc+abs(nx-g[0])+abs(ny-g[1]),ns))
  if g not in prev: raise RuntimeError(f'no B.Cu passive path {start}->{goal}')
  path=[]; cur=g
  while cur is not None: path.append(cur); cur=prev[cur]
  return list(reversed(path))
 anchors={'XI':mm(P(fps['Y1'],'1').GetPosition()),'XO':mm(P(fps['Y1'],'3').GetPosition()),'VS':mm(P(fps['Y1'],'2').GetPosition())}
 targets={'XI':[('R23','1'),('C42','1')],'XO':[('R23','2'),('C43','1')],'VS':[('Y1','4'),('C42','2'),('C43','2')]}
 for k,vals in targets.items():
  for ref,pn in vals:
   end=mm(P(fps[ref],pn).GetPosition()); path=route(anchors[k],end); last=anchors[k]
   for a,z in zip(path,path[1:]):
    e=XY(z); t=pcbnew.PCB_TRACK(b); t.SetStart(V(*last)); t.SetEnd(V(*e)); t.SetLayer(pcbnew.B_Cu); t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(nets[k]); b.Add(t); mark(last,e); last=e
   anchors[k]=end
   print(k,ref,pn,len(path))
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
