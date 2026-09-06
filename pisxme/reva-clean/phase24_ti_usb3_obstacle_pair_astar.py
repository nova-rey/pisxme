"""Obstacle-aware disposable USB3 escape for the selected TI-U7 macro.

All terminals are read from native pads.  The expected pair ordering only
controls job order; it does not create connectivity.  Existing pads/tracks
and already-emitted paths are physical obstacles, while signal copper is
restricted to F.Cu/B.Cu and transitions use ordinary through-vias.
"""
from pathlib import Path
from heapq import heappush, heappop
import os, math, pcbnew

R = Path(__file__).resolve().parent
BASE = R / os.environ.get("PISXME_TI_ASTAR_BASE", "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI.kicad_pcb")
OUT = R / os.environ.get("PISXME_TI_ASTAR_OUT", "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_USB3_OBSTACLE_ASTAR.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu
STEP, WIDTH = .25, .15
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(o):
    p = o if hasattr(o, "x") else o.GetPosition()
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def net(b,name):
    for q in (name,"/CORE_CM5/"+name,"/STORAGE/"+name):
        n=b.FindNet(q)
        if n is not None:return n
    raise RuntimeError("missing "+name)
def grid(p): return round(p[0]/STEP),round(p[1]/STEP)
def point(g): return g[0]*STEP,g[1]*STEP
def add_track(b,n,a,z,l):
    if a==z:return
    t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(n);b.Add(t)
def add_via(b,n,p):
    v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
def raster_line(blocked,a,z,r=.22):
    ax,ay=grid(a);zx,zy=grid(z);steps=max(abs(zx-ax),abs(zy-ay),1);q=max(1,math.ceil(r/STEP))
    for k in range(steps+1):
        x=round(ax+(zx-ax)*k/steps);y=round(ay+(zy-ay)*k/steps)
        for i in range(-q,q+1):
                for j in range(-q,q+1):blocked.add((x+i,y+j))
def raster_rect(blocked,p,rx,ry):
    x,y=grid(p);qx=max(1,math.ceil(rx/STEP));qy=max(1,math.ceil(ry/STEP))
    for i in range(-qx,qx+1):
        for j in range(-qy,qy+1):blocked.add((x+i,y+j))
def obstacle_map(b,layer):
    blocked=set()
    for t in b.GetTracks():
        if isinstance(t,pcbnew.PCB_VIA):
            p=xy(t.GetPosition());raster_line(blocked,p,p,.42)
        elif t.GetLayer()==layer:raster_line(blocked,xy(t.GetStart()),xy(t.GetEnd()),.23)
    for f in b.GetFootprints():
        for p in f.Pads():
            # The four routed terminals are intentional goals.  Their local
            # dogbone approach must be allowed to enter the native land field;
            # KiCad DRC, not the raster planner, decides the final clearance.
            if f.GetReference() == "U7" and str(p.GetNumber()) in {"42","43","45","46"}:
                continue
            if p.GetLayerSet().Contains(layer):
                q=p.GetSize()
                raster_rect(blocked,xy(p),pcbnew.ToMM(q.x)/2+.16,pcbnew.ToMM(q.y)/2+.16)
    return blocked
def astar(blocked,start,goal):
    s=grid(start);g=grid(goal)
    # Exempt the two intentional terminals only; all other occupied cells stay blocked.
    for c in (s,g):
        for i in range(-2,3):
            for j in range(-2,3):blocked.discard((c[0]+i,c[1]+j))
    q=[(0,s)];cost={s:0};prev={s:None}
    while q:
        _,c=heappop(q)
        if c==g:break
        x,y=c
        for n in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if not (4<=n[0]<=1000 and 4<=n[1]<=700) or n in blocked:continue
            v=cost[c]+1
            if v<cost.get(n,10**9):cost[n]=v;prev[n]=c;heappush(q,(v+abs(n[0]-g[0])+abs(n[1]-g[1]),n))
    if g not in prev:raise RuntimeError(f"no F.Cu route {start}->{goal}")
    out=[];c=g
    while c is not None:out.append(point(c));c=prev[c]
    out.reverse();return out
def emit(b,n,path,blocked):
    for a,z in zip(path,path[1:]):add_track(b,n,a,z,F)
    for a,z in zip(path,path[1:]):raster_line(blocked,a,z,.24)

b=pcbnew.LoadBoard(str(BASE))
jobs=[("CM5_USB3_RX_N","128","42"),("CM5_USB3_RX_P","130","43"),("CM5_USB3_TX_N","140","45"),("CM5_USB3_TX_P","142","46")]
terms=[]
for name,jp,up in jobs:
    n=net(b,name);pad(b,"J7",jp).SetNet(n)
    terms.append((name,xy(pad(b,"J7",jp)),xy(pad(b,"U7",up))))
for t in list(b.GetTracks()):
    if "CM5_USB3_" in t.GetNetname():b.RemoveNative(t)
blocked=obstacle_map(b,F)
for idx,(name,src,dst) in enumerate(terms):
    n=net(b,name)
    sx=84.0+idx*2.0
    sy=(100.0,102.0,106.0,108.0)[idx]
    sv=(sx,sy);tv=dst
    # J7 source pads are on B.Cu in the carrier-mating view.
    add_track(b,n,src,sv,B);add_via(b,n,sv)
    p=astar(blocked,sv,tv);emit(b,n,p,blocked)
    # TI USB3 lands are F.Cu SMD pads; no target via is necessary.
    print(name,"segments",len(p),"source",src,"target",dst)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
