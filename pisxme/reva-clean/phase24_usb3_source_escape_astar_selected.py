"""Route USB3 on the selected macro from explicit native source escapes.

The source dogbones are bounded CM5IO-derived geometry. A* begins at the
actual source transition vias, not inside the J7 pad field, and derives all
remaining occupancy from saved pads/tracks/vias.
"""
from pathlib import Path
from heapq import heappush, heappop
import math, pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb'; OUT=R/'PHASE24_USB3_SELECTED_SOURCE_ESCAPE_ASTAR.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; STEP=.25; W=.13208
JOBS=(('CM5_USB3_RX_N','128','42',(72.,103.9)),('CM5_USB3_RX_P','130','43',(72.,104.8)),('CM5_USB3_TX_N','140','45',(72.,108.)),('CM5_USB3_TX_P','142','46',(71.,109.)))
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):
 p=p.GetPosition() if hasattr(p,'GetPosition') else p;return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def g(p):return round(p[0]/STEP),round(p[1]/STEP)
def p(q):return q[0]*STEP,q[1]*STEP
def add_disc(s,l,q,r=.3):
 x,y=g(q);rr=max(1,math.ceil(r/STEP))
 for dx in range(-rr,rr+1):
  for dy in range(-rr,rr+1):s[l].add((x+dx,y+dy))
def add_line(s,l,a,z,r=.2):
 ax,ay=g(a);zx,zy=g(z);n=max(abs(zx-ax),abs(zy-ay),1);rr=max(1,math.ceil(r/STEP))
 for i in range(n+1):
  x=round(ax+(zx-ax)*i/n);y=round(ay+(zy-ay)*i/n)
  for dx in range(-rr,rr+1):
   for dy in range(-rr,rr+1):s[l].add((x+dx,y+dy))
def occupied(b):
 s={F:set(),B:set()}
 for t in b.GetTracks():
  if any(n in t.GetNetname() for n,_,_,_ in JOBS):continue
  if isinstance(t,pcbnew.PCB_VIA):add_disc(s,F,xy(t.GetPosition()),.38);add_disc(s,B,xy(t.GetPosition()),.38)
  else:add_line(s,t.GetLayer(),xy(t.GetStart()),xy(t.GetEnd()),.22)
 for fp in b.GetFootprints():
  for q in fp.Pads():
   r=max(pcbnew.ToMM(q.GetSize().x),pcbnew.ToMM(q.GetSize().y))/2+.3;ls=[l for l in (F,B) if q.GetLayerSet().Contains(l)]
   if q.GetDrillSize().x or q.GetDrillSize().y:ls=list(set(ls)|{F,B})
   for l in ls:add_disc(s,l,xy(q),r)
 return s
def route(blocked,start,goal,start_layer=B,goal_layer=F):
 s={F:set(blocked[F]),B:set(blocked[B])}; a=(*g(start),start_layer);z=(*g(goal),goal_layer)
 # Clear only bounded terminal halos; source is an explicit via, not a
 # connector-pad-field authorization.
 rr=math.ceil(1.0/STEP)
 for dx in range(-math.ceil(.5/STEP),math.ceil(.5/STEP)+1):
  for dy in range(-math.ceil(.5/STEP),math.ceil(.5/STEP)+1):s[start_layer].discard((a[0]+dx,a[1]+dy))
 for dx in range(-rr,rr+1):
  for dy in range(-rr,rr+1):s[goal_layer].discard((z[0]+dx,z[1]+dy))
 q=[(0,a)];cost={a:0};prev={a:None};bounds=(g((1,1)),g((299,179)))
 while q:
  _,c=heappop(q)
  if c==z:break
  x,y,l=c
  for nx,ny,nl in ((x+1,y,l),(x-1,y,l),(x,y+1,l),(x,y-1,l),(x,y,B if l==F else F)):
   if not(bounds[0][0]<=nx<=bounds[1][0] and bounds[0][1]<=ny<=bounds[1][1]):continue
   if (nx,ny) in s[nl] and (nx,ny,nl)!=z:continue
   n=(nx,ny,nl);v=cost[c]+1+(36 if nl!=l else 0)
   if v<cost.get(n,10**12):cost[n]=v;prev[n]=c;heappush(q,(v+abs(nx-z[0])+abs(ny-z[1]),n))
 if z not in prev:raise RuntimeError(f'no route {start}->{goal}')
 out=[];c=z
 while c is not None:out.append(c);c=prev[c]
 return out[::-1]
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*q));v.SetWidth(pcbnew.FromMM(.50));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
def emit(b,n,path,blocked):
 last=None
 for a,z in zip(path,path[1:]):
  if a[2]!=z[2]:q=p(a[:2]);via(b,n,q);add_disc(blocked,F,q,.4);add_disc(blocked,B,q,.4);last=None
  else:
   if last is None:last=p(a[:2])
   e=p(z[:2]);t=pcbnew.PCB_TRACK(b);t.SetStart(V(*last));t.SetEnd(V(*e));t.SetLayer(a[2]);t.SetWidth(pcbnew.FromMM(W));t.SetNet(n);b.Add(t);add_line(blocked,a[2],last,e,.22);last=e
b=pcbnew.LoadBoard(str(BASE));j7=b.FindFootprintByReference('J7');u7=b.FindFootprintByReference('U7');ends=[]
for n,jp,up,vp in JOBS:
 j=j7.FindPadByNumber(jp);u=u7.FindPadByNumber(up)
 if j is None or u is None:raise RuntimeError(n)
 ends.append((n,xy(j),xy(u),vp))
for t in list(b.GetTracks()):
 if any(n in t.GetNetname() for n,_,_,_ in JOBS):b.Remove(t)
blocked=occupied(b)
landings={'CM5_USB3_RX_N':(98.0,122.0),'CM5_USB3_RX_P':(98.0,124.0),'CM5_USB3_TX_N':(98.0,126.0),'CM5_USB3_TX_P':(98.0,128.0)}
for n,src,goal,sv in ends:
 net=b.FindNet('/CORE_CM5/'+n)
 # Explicit source escape; TX separation follows the validated oracle geometry.
 if n=='CM5_USB3_TX_N':
  a=(71.2,106.3);q=(72.5,106.3);r=(72.5,108.0)
  t=pcbnew.PCB_TRACK(b);t.SetStart(V(*src));t.SetEnd(V(*a));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(W));t.SetNet(net);b.Add(t)
  for x,y in ((a[0],a[1]),(q[0],q[1]),(r[0],r[1])):pass
  # use the designated source via after a separated F.Cu dogbone
  tt=pcbnew.PCB_TRACK(b);tt.SetStart(V(*a));tt.SetEnd(V(*r));tt.SetLayer(F);tt.SetWidth(pcbnew.FromMM(W));tt.SetNet(net);b.Add(tt)
 elif n=='CM5_USB3_TX_P':
  a=(70.8,106.7);r=(70.8,109.0)
  tt=pcbnew.PCB_TRACK(b);tt.SetStart(V(*src));tt.SetEnd(V(*a));tt.SetLayer(F);tt.SetWidth(pcbnew.FromMM(W));tt.SetNet(net);b.Add(tt)
  tt=pcbnew.PCB_TRACK(b);tt.SetStart(V(*a));tt.SetEnd(V(*r));tt.SetLayer(F);tt.SetWidth(pcbnew.FromMM(W));tt.SetNet(net);b.Add(tt)
 else:
  r=sv;tt=pcbnew.PCB_TRACK(b);tt.SetStart(V(*src));tt.SetEnd(V(*r));tt.SetLayer(F);tt.SetWidth(pcbnew.FromMM(W));tt.SetNet(net);b.Add(tt)
 via(b,net,r);add_disc(blocked,F,r,.4);add_disc(blocked,B,r,.4)
 landing=landings[n]
 path=route(blocked,r,landing);emit(b,net,path,blocked)
 # The landing is an explicit via outside the U7 pad field.  Only the final
 # short F.Cu dogbone touches the authoritative native pad center.
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*landing));t.SetEnd(V(*goal));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(W));t.SetNet(net);b.Add(t)
 print(n,src,goal,'landing',landing,'transitions',sum(a[2]!=z[2] for a,z in zip(path,path[1:])))
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
