"""Disposable obstacle-aware CM5 J7 to storage USB-selector escape."""
from pathlib import Path
from heapq import heappush, heappop
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_NETLIST_REGENERATED_V3.kicad_pcb'; OUT=R/'PHASE24_STORAGE_USB3_SELECTOR_ASTAR_V3.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; STEP=.5; W=.15
JOBS=(('CM5_USB3_RX_N','128','16'),('CM5_USB3_RX_P','130','15'),('CM5_USB3_TX_N','140','12'),('CM5_USB3_TX_P','142','11'))
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p):
    q=p.GetPosition() if hasattr(p,'GetPosition') else p
    return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def q(p): return round(p[0]/STEP),round(p[1]/STEP)
def mm(x): return x*STEP
def mark(s,l,a,z=None,r=.35):
    x,y=q(a); z=q(z or a); n=max(abs(z[0]-x),abs(z[1]-y),1)
    for i in range(n+1):
        xx=round(x+(z[0]-x)*i/n); yy=round(y+(z[1]-y)*i/n)
        for dx in range(-1,2):
            for dy in range(-1,2): s[l].add((xx+dx,yy+dy))
def occupied(b, skip):
    s={F:set(),B:set()}
    for t in list(b.GetTracks()):
        if t.GetNetname() in skip: continue
        if isinstance(t,pcbnew.PCB_VIA):
            mark(s,F,xy(t.GetPosition())); mark(s,B,xy(t.GetPosition()))
        else: mark(s,t.GetLayer(),xy(t.GetStart()),xy(t.GetEnd()))
    for fp in b.GetFootprints():
        for p in fp.Pads():
            a=xy(p); r=max(pcbnew.ToMM(p.GetSize().x),pcbnew.ToMM(p.GetSize().y))/2+.3
            for l in (F,B): mark(s,l,a,r=r)
    return s
def route(blocked,start,goal,start_layer=B,goal_layer=B):
    a=(*q(start),start_layer); z=(*q(goal),goal_layer); todo=[(0,a)]; cost={a:0}; prev={a:None}
    while todo:
        _,c=heappop(todo)
        if c==z: break
        x,y,l=c
        for nx,ny,nl in ((x+1,y,l),(x-1,y,l),(x,y+1,l),(x,y-1,l),(x,y,B if l==F else F)):
            if not (2<=nx<=590 and 2<=ny<=390): continue
            if (nx,ny) in blocked[nl] and (nx,ny,nl)!=z: continue
            n=(nx,ny,nl); v=cost[c]+1+(30 if nl!=l else 0)
            if v<cost.get(n,10**9): cost[n]=v; prev[n]=c; heappush(todo,(v+abs(nx-z[0])+abs(ny-z[1]),n))
    if z not in prev: raise RuntimeError(f'no native route {start}->{goal}')
    out=[]; c=z
    while c is not None: out.append(c); c=prev[c]
    return out[::-1]
def emit(b,n,path):
    last=None
    for a,z in zip(path,path[1:]):
        if a[2]!=z[2]:
            v=pcbnew.PCB_VIA(b); v.SetPosition(V(mm(a[0]),mm(a[1]))); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v); last=None
        else:
            if last is None: last=(mm(a[0]),mm(a[1]))
            t=pcbnew.PCB_TRACK(b); t.SetStart(V(*last)); t.SetEnd(V(mm(z[0]),mm(z[1]))); t.SetLayer(a[2]); t.SetWidth(pcbnew.FromMM(W)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t); last=(mm(z[0]),mm(z[1]))
b=pcbnew.LoadBoard(str(BASE)); j=b.FindFootprintByReference('J7'); u=b.FindFootprintByReference('U12')
names={x[0] for x in JOBS}
for t in list(b.GetTracks()):
    if t.GetNetname() in names: b.RemoveNative(t)
blocked=occupied(b,names)
for index,(name,jp,up) in enumerate(JOBS):
    n=b.FindNet(name); pad_start=xy(j.FindPadByNumber(jp)); pad_goal=xy(u.FindPadByNumber(up))
    offset=(-.8 if index%2==0 else .8)
    start=(pad_start[0]+2.0,pad_start[1]+offset); goal=(pad_goal[0]-2.0,pad_goal[1]+offset)
    for l in (F,B):
        for dx in range(-3,4):
            for dy in range(-3,4): blocked[l].discard((q(start)[0]+dx,q(start)[1]+dy)); blocked[l].discard((q(goal)[0]+dx,q(goal)[1]+dy))
    # Explicit ordinary-via dogbones keep both vias outside the QFN/CM5 pads.
    for a,z in ((pad_start,start),(goal,pad_goal)):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(pcbnew.FromMM(W)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
    for a in (start,goal):
        v=pcbnew.PCB_VIA(b); v.SetPosition(V(*a)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
    path=route(blocked,start,goal,B,B); emit(b,n,path)
    for a,z in zip(path,path[1:]):
        if a[2]==z[2]: mark(blocked,a[2],(mm(a[0]),mm(a[1])),(mm(z[0]),mm(z[1])))
    print(name,'transitions',sum(a[2]!=z[2] for a,z in zip(path,path[1:])))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
