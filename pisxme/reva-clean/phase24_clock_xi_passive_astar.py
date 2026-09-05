"""Disposable two-layer XI-to-R23 passive branch search."""
from pathlib import Path
import sys
from heapq import heappush,heappop
import math
import pcbnew
R=Path(__file__).resolve().parent; BASE=Path(sys.argv[1]) if len(sys.argv)>1 else R/'PHASE24_CLOCK_XI_XO_VS_ASTAR_PROBE.kicad_pcb'; OUT=Path(sys.argv[4]) if len(sys.argv)>4 else R/'PHASE24_CLOCK_XI_PASSIVE_ASTAR_PROBE.kicad_pcb'; STEP=.25; NET=sys.argv[2] if len(sys.argv)>2 else '/STORAGE/BRIDGE_XI'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def G(q): return round(q[0]/STEP),round(q[1]/STEP)
def XY(g): return g[0]*STEP,g[1]*STEP
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet(NET)
 def pad_token(spec):
  ref,pn=spec.split('.',1); return next(p for p in b.FindFootprintByReference(ref).Pads() if str(p.GetNumber())==pn)
 source_pad=pad_token(sys.argv[3] if len(sys.argv)>3 else 'Y1.1'); target_pad=pad_token(sys.argv[5] if len(sys.argv)>5 else 'R23.1')
 start=mm(source_pad.GetPosition()); target=mm(target_pad.GetPosition()); occ={pcbnew.F_Cu:set(),pcbnew.B_Cu:set()}
 def mark(l,a,z,inf=.12):
  for x in range(math.floor((min(a[0],z[0])-inf)/STEP),math.ceil((max(a[0],z[0])+inf)/STEP)+1):
   for yy in range(math.floor((min(a[1],z[1])-inf)/STEP),math.ceil((max(a[1],z[1])+inf)/STEP)+1): occ[l].add((x,yy))
 for item in b.GetTracks():
  if type(item).__name__=='PCB_VIA':
   if item.GetNetname()!=NET: q=mm(item.GetPosition()); mark(pcbnew.F_Cu,q,q,.35); mark(pcbnew.B_Cu,q,q,.35)
  elif item.GetNetname()!=NET: mark(item.GetLayer(),mm(item.GetStart()),mm(item.GetEnd()))
 for fp in b.GetFootprints():
  for p in fp.Pads():
   if p.GetNetname()==NET: continue
   q=mm(p.GetPosition()); s=mm(p.GetSize())
   for l in (pcbnew.F_Cu,pcbnew.B_Cu):
    if p.GetLayerSet().Contains(l): mark(l,(q[0]-s[0]/2,q[1]-s[1]/2),(q[0]+s[0]/2,q[1]+s[1]/2),.18)
 s=G(start); g=G(target)
 # Preserve nearby no-net pads in the pad field.  Only the exact source and
 # destination cells may be occupied by the route endpoint itself.
 for layer in (pcbnew.F_Cu, pcbnew.B_Cu):
  occ[layer].discard((s[0],s[1])); occ[layer].discard((g[0],g[1]))
 # U7/support pads are F.Cu SMD pads; begin on the actual source layer so
 # the first transition is an explicit ordinary-via dogbone, not an
 # impossible B.Cu segment starting inside an F.Cu pad.
 start_layer=pcbnew.F_Cu
 q=[(0,(s[0],s[1],start_layer))]; prev={(s[0],s[1],start_layer):None}; cost={(s[0],s[1],start_layer):0}; lo=G((90,115)); hi=G((130,145))
 while q:
  _,cur=heappop(q); x,y0,l=cur
  if (x,y0,l)==(g[0],g[1],pcbnew.B_Cu): break
  for nx,ny,nl in ((x+1,y0,l),(x-1,y0,l),(x,y0+1,l),(x,y0-1,l),(x,y0,pcbnew.F_Cu if l==pcbnew.B_Cu else pcbnew.B_Cu)):
   if not(lo[0]<=nx<=hi[0] and lo[1]<=ny<=hi[1]): continue
   if (nx,ny) in occ[nl] and (nx,ny)!=(g[0],g[1]): continue
   if nl!=l and ((nx,ny) in occ[pcbnew.F_Cu] or (nx,ny) in occ[pcbnew.B_Cu]): continue
   ns=(nx,ny,nl); nc=cost[cur]+(12 if nl!=l else 1)
   if nc<cost.get(ns,10**9): cost[ns]=nc; prev[ns]=cur; heappush(q,(nc+abs(nx-g[0])+abs(ny-g[1]),ns))
 target_layer=pcbnew.F_Cu if target_pad.GetLayerSet().Contains(pcbnew.F_Cu) else pcbnew.B_Cu
 goal=(g[0],g[1],target_layer)
 if goal not in prev: raise RuntimeError(f'no XI passive path {start}->{target}')
 path=[]; cur=goal
 while cur is not None: path.append(cur); cur=prev[cur]
 path.reverse(); last=None
 for a,z in zip(path,path[1:]):
  if a[2]!=z[2]:
   p=XY(a); v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v); last=p
  else:
   if last is None: last=XY(a)
   e=XY(z); t=pcbnew.PCB_TRACK(b); t.SetStart(V(*last)); t.SetEnd(V(*e)); t.SetLayer(a[2]); t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(n); b.Add(t); last=e
 b.Save(str(OUT)); print(OUT,'steps',len(path),'start',start,'target',target)
if __name__=='__main__': main()
