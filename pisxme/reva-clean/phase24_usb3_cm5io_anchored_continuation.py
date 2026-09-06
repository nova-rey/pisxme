"""Disposable CM5IO-anchored USB3 continuation for the selected macro."""
from pathlib import Path
from heapq import heappush, heappop
import math, pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_REVIEW.kicad_pcb"
ORACLE = R / "authority-inventory/cm5io-rev2/CM5IO.kicad_pcb"
OUT = R / "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_CM5IO_ANCHORED.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
STEP, WIDTH = .25, .15
JOBS = (("CM5_USB3_RX_N", "128", "42", "/CM5_HighSpeed/USB3-0-RX_N"),
        ("CM5_USB3_RX_P", "130", "43", "/CM5_HighSpeed/USB3-0-RX_P"),
        ("CM5_USB3_TX_N", "140", "45", "/CM5_HighSpeed/USB3-0-TX_N"),
        ("CM5_USB3_TX_P", "142", "46", "/CM5_HighSpeed/USB3-0-TX_P"))

def V(p): return pcbnew.VECTOR2I_MM(float(p[0]), float(p[1]))
def mm(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def net(board, name): return board.FindNet(name) or board.FindNet("/CORE_CM5/" + name)
def transform(p):
    x, y = mm(p); return (230.50 - x, 203.50 - y)
def grid(p): return round(p[0]/STEP), round(p[1]/STEP)
def point(g): return g[0]*STEP, g[1]*STEP
def add_line(blocked, layer, a, z, radius):
    ax, ay = grid(a); zx, zy = grid(z); count=max(abs(zx-ax),abs(zy-ay),1)
    r=max(1,math.ceil(radius/STEP))
    for i in range(count+1):
        x=round(ax+(zx-ax)*i/count); y=round(ay+(zy-ay)*i/count)
        for dx in range(-r,r+1):
            for dy in range(-r,r+1): blocked[layer].add((x+dx,y+dy))
def add_disc(blocked, layer, p, radius):
    x,y=grid(p); r=max(1,math.ceil(radius/STEP))
    for dx in range(-r,r+1):
        for dy in range(-r,r+1): blocked[layer].add((x+dx,y+dy))
def occupancy(board):
    out={F:set(),B:set()}
    for t in board.GetTracks():
        if any(n in t.GetNetname() for n,_,_,_ in JOBS): continue
        if isinstance(t,pcbnew.PCB_VIA):
            add_disc(out,F,mm(t.GetPosition()),.42); add_disc(out,B,mm(t.GetPosition()),.42)
        else: add_line(out,t.GetLayer(),mm(t.GetStart()),mm(t.GetEnd()),.38)
    for fp in board.GetFootprints():
        for p in fp.Pads():
            q=mm(p.GetPosition()); s=p.GetSize(); r=max(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y))/2+.30
            ls=[l for l in (F,B) if p.GetLayerSet().Contains(l)]
            if p.GetDrillSize().x or p.GetDrillSize().y: ls=[F,B]
            for l in ls: add_disc(out,l,q,r)
    return out
def astar(blocked, start, goal, start_layer=B):
    local={F:set(blocked[F]),B:set(blocked[B])}; s=(*grid(start),start_layer); t=(*grid(goal),B)
    for layer,q in ((start_layer,s),(B,t)):
        r=math.ceil(1.5/STEP)
        for dx in range(-r,r+1):
            for dy in range(-r,r+1): local[layer].discard((q[0]+dx,q[1]+dy))
    q=[(0,s)]; cost={s:0}; prev={s:None}; bounds=(grid((1,1)),grid((299,179)))
    while q:
        _,cur=heappop(q)
        if cur==t: break
        x,y,l=cur
        ns=((x+1,y,l),(x-1,y,l),(x,y+1,l),(x,y-1,l),(x,y,F if l==B else B))
        for nxt in ns:
            nx,ny,nl=nxt
            if not(bounds[0][0]<=nx<=bounds[1][0] and bounds[0][1]<=ny<=bounds[1][1]): continue
            if (nx,ny) in local[nl] and nxt!=t: continue
            new=cost[cur]+1+(36 if nl!=l else 0)
            if new<cost.get(nxt,10**12):
                cost[nxt]=new; prev[nxt]=cur
                heappush(q,(new+abs(nx-t[0])+abs(ny-t[1])+(36 if nl!=t[2] else 0),nxt))
    if t not in prev: raise RuntimeError(f"no continuation {start}->{goal}")
    out=[]; cur=t
    while cur is not None: out.append(cur); cur=prev[cur]
    return out[::-1]
def track(board,n,a,z,l):
    if a==z:return
    t=pcbnew.PCB_TRACK(board);t.SetStart(V(a));t.SetEnd(V(z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(n);board.Add(t)
def via(board,n,p):
    v=pcbnew.PCB_VIA(board);v.SetPosition(V(p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);board.Add(v)
def first_path(oracle,name,padno):
    f=oracle.FindFootprintByReference("Module1"); start=f.FindPadByNumber(padno).GetPosition()
    items=[]; vias=set()
    for t in oracle.GetTracks():
        if t.GetNetname()!=name:continue
        if isinstance(t,pcbnew.PCB_VIA): vias.add((t.GetPosition().x,t.GetPosition().y))
        else: items.append((t.GetStart(),t.GetEnd(),t.GetLayer(),t.GetWidth()))
    frontier={(start.x,start.y)}; used=set(); result=[]; reached=None
    while frontier:
        new=set()
        for i,(a,z,l,w) in enumerate(items):
            if i in used or (a.x,a.y) not in frontier and (z.x,z.y) not in frontier:continue
            used.add(i); result.append((a,z,l,w)); other=z if (a.x,a.y) in frontier else a
            if (other.x,other.y) in vias: reached=other; break
            new.add((other.x,other.y))
        if reached is not None:break
        frontier=new
    if reached is None:raise RuntimeError(name)
    return result,reached

oracle=pcbnew.LoadBoard(str(ORACLE)); board=pcbnew.LoadBoard(str(BASE))
for t in list(board.GetTracks()):
    if any(n in t.GetNetname() for n,_,_,_ in JOBS): board.Remove(t)
paths={name:first_path(oracle,on,jp) for name,jp,_,on in JOBS}
for name,jp,up,_ in JOBS:
    n=net(board,name); j=board.FindFootprintByReference("J7"); u=board.FindFootprintByReference("U7")
    src=mm(j.FindPadByNumber(jp).GetPosition()); dst=mm(u.FindPadByNumber(up).GetPosition())
    copied, first=paths[name]
    for a,z,l,w in copied: track(board,n,transform(a),transform(z),l)
    sv=transform(first); via(board,n,sv)
    target=(88.0,124.6 + (0.9 * (int(up)-42)))
    blocked=occupancy(board); route=astar(blocked,sv,target)
    last=None
    for a,z in zip(route,route[1:]):
        if a[2]!=z[2]: via(board,n,point(a[:2])); last=None
        else:
            if last is None:last=point(a[:2])
            end=point(z[:2]);track(board,n,last,end,a[2]);add_line(blocked,a[2],last,end,.38);last=end
    via(board,n,target); track(board,n,target,dst,F)
    print(name,'source_via',sv,'target',target,'route_nodes',len(route))
board.BuildListOfNets();board.Save(str(OUT));print(OUT)
