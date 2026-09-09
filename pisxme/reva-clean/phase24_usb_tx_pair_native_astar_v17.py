"""V17: native-pad A* regeneration of the complete U11 USB TX pair field."""
from pathlib import Path
from heapq import heappush, heappop
import math, pcbnew

R=Path(__file__).resolve().parent
b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb'))
F,B=pcbnew.F_Cu,pcbnew.B_Cu; STEP=.2; WIDTH=.15
JOBS=(('USB_TXP1','U11','21','C86','1'),('USB_TXN1','U11','22','C87','1'))

def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def grid(p): return round(p[0]/STEP),round(p[1]/STEP)
def point(q): return q[0]*STEP,q[1]*STEP
def mark_disc(s,l,p,r=.30):
 x,y=grid(p); rr=max(1,math.ceil(r/STEP))
 for dx in range(-rr,rr+1):
  for dy in range(-rr,rr+1): s[l].add((x+dx,y+dy))
def mark_line(s,l,a,z,r=.18):
 ax,ay=grid(a); zx,zy=grid(z); n=max(abs(zx-ax),abs(zy-ay),1); rr=max(1,math.ceil(r/STEP))
 for i in range(n+1):
  x=round(ax+(zx-ax)*i/n); y=round(ay+(zy-ay)*i/n)
  for dx in range(-rr,rr+1):
   for dy in range(-rr,rr+1): s[l].add((x+dx,y+dy))
def occupied(skip):
 s={F:set(),B:set()}
 for t in b.GetTracks():
  if t.GetNetname() in skip: continue
  if isinstance(t,pcbnew.PCB_VIA):
   p=mm(t.GetPosition()); mark_disc(s,F,p,.38); mark_disc(s,B,p,.38)
  else: mark_line(s,t.GetLayer(),mm(t.GetStart()),mm(t.GetEnd()),.22)
 for fp in b.GetFootprints():
  for p in fp.Pads():
   q=mm(p.GetPosition()); sz=p.GetSize(); r=max(pcbnew.ToMM(sz.x),pcbnew.ToMM(sz.y))/2+.28
   ls=[F,B] if p.GetDrillSize().x or p.GetDrillSize().y else [l for l in (F,B) if p.GetLayerSet().Contains(l)]
   for l in ls: mark_disc(s,l,q,r)
 return s
def route(s,start,goal):
 a=(*grid(start),F); z=(*grid(goal),F); q=[(0,a)]; cost={a:0}; prev={a:None}
 for l,t in ((F,a),(F,z)):
  rr=math.ceil(.5/STEP)
  for dx in range(-rr,rr+1):
   for dy in range(-rr,rr+1): s[l].discard((t[0]+dx,t[1]+dy))
 while q:
  _,c=heappop(q)
  if c==z: break
  x,y,l=c
  for nx,ny,nl in ((x+1,y,l),(x-1,y,l),(x,y+1,l),(x,y-1,l),(x,y,B if l==F else F)):
   if not (5<=nx<=1495 and 5<=ny<=895): continue
   if (nx,ny) in s[nl] and (nx,ny,nl)!=z: continue
   n=(nx,ny,nl); v=cost[c]+1+(45 if nl!=l else 0)
   if v<cost.get(n,10**12):
    cost[n]=v;prev[n]=c;heappush(q,(v+abs(nx-z[0])+abs(ny-z[1]),n))
 if z not in prev: raise RuntimeError(f'no route {start}->{goal}')
 out=[];c=z
 while c is not None: out.append(c);c=prev[c]
 return out[::-1]
def via(net,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(net);v.SetNetCode(net.GetNetCode());b.Add(v)
def emit(net,path,s):
 last=None
 for a,z in zip(path,path[1:]):
  if a[2]!=z[2]:
   p=point(a[:2]);via(net,p);mark_disc(s,F,p,.42);mark_disc(s,B,p,.42);last=None
  else:
   if last is None:last=point(a[:2])
   end=point(z[:2]); t=pcbnew.PCB_TRACK(b);t.SetStart(V(*last));t.SetEnd(V(*end));t.SetLayer(a[2]);t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(net);t.SetNetCode(net.GetNetCode());b.Add(t);mark_line(s,a[2],last,end,.20);last=end

names={x[0] for x in JOBS}
for t in list(b.GetTracks()):
 if t.GetNetname() in names: b.RemoveNative(t)
s=occupied(names)
for name,sref,spad,dref,dpad in JOBS:
 net=b.FindNet(name); start=mm(b.FindFootprintByReference(sref).FindPadByNumber(spad).GetPosition()); goal=mm(b.FindFootprintByReference(dref).FindPadByNumber(dpad).GetPosition())
 path=route(s,start,goal); emit(net,path,s)
 print(name,'length_mm',round(sum(math.hypot(point(a[:2])[0]-point(z[:2])[0],point(a[:2])[1]-point(z[:2])[1]) for a,z in zip(path,path[1:])),3),'transitions',sum(a[2]!=z[2] for a,z in zip(path,path[1:])))
b.BuildListOfNets();out=R/'PHASE24_STORAGE_USB_TX_PAIR_NATIVE_ASTAR_V17.kicad_pcb';b.Save(str(out));print(out)
