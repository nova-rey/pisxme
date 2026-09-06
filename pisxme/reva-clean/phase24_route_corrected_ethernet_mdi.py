"""Disposable obstacle-aware Ethernet MDI development route.

Endpoints and nets come only from the saved PCB pads.  This is deliberately a
routing experiment on the corrected macro basis; it never changes schematic
authority or inserts synthetic connectivity.
"""
from pathlib import Path
from heapq import heappush, heappop
import math
import os
import sys
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb")
OUT = ROOT / (sys.argv[2] if len(sys.argv) > 2 else "PHASE24_CORRECTED_ETHERNET_MDI_ROUTE.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu
STEP, WIDTH = 0.25, 0.127
VIA_W, VIA_D = 0.45, 0.20

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def mm(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def grid(x, y): return round(x / STEP), round(y / STEP)
def xy(g): return g[0] * STEP, g[1] * STEP
def pad(board, ref, number):
    p = board.FindFootprintByReference(ref).FindPadByNumber(str(number))
    if p is None: raise RuntimeError(f"missing {ref}.{number}")
    return p
def pos(p): return mm(p.GetPosition())
def pad_layer(p, preferred=F):
    """Return a real copper layer from the saved pad layer set."""
    if p.GetLayerSet().Contains(preferred): return preferred
    if p.GetLayerSet().Contains(F): return F
    if p.GetLayerSet().Contains(B): return B
    raise RuntimeError(f"pad {p.GetNumber()} has no F.Cu/B.Cu copper layer")

def mark_line(occ, layer, a, z, inflate=0.15):
    ax, ay = grid(*a); zx, zy = grid(*z)
    steps = max(abs(zx-ax), abs(zy-ay), 1)
    for i in range(steps+1):
        x = round(ax + (zx-ax)*i/steps); y = round(ay + (zy-ay)*i/steps)
        r = max(1, math.ceil(inflate/STEP))
        for dx in range(-r, r+1):
            for dy in range(-r, r+1): occ[layer].add((x+dx,y+dy))

def mark_pad(occ, layer, pad, clearance=0.08):
    """Mark a native pad using its transformed rectangular dimensions.

    The prior max(size.x,size.y) radius turned 0.30x0.55 mm ESD pads into
    circular 0.55 mm obstacles, sealing legal side escapes and encouraging
    the router to cross neighboring pads.  Keep the two axes independent.
    """
    x, y = pos(pad)
    sx, sy = mm(pad.GetSize())
    gx, gy = grid(x, y)
    rx = max(1, math.ceil((sx / 2 + clearance) / STEP))
    ry = max(1, math.ceil((sy / 2 + clearance) / STEP))
    for dx in range(-rx, rx + 1):
        for dy in range(-ry, ry + 1):
            occ[layer].add((gx + dx, gy + dy))

def open_pad(occ, layer, pad):
    """Open only the native terminal pad footprint for route departure."""
    x, y = pos(pad)
    sx, sy = mm(pad.GetSize())
    gx, gy = grid(x, y)
    rx = max(0, math.ceil((sx / 2) / STEP))
    ry = max(0, math.ceil((sy / 2) / STEP))
    for dx in range(-rx, rx + 1):
        for dy in range(-ry, ry + 1):
            occ[layer].discard((gx + dx, gy + dy))

def build_occupancy(board, ignore_refs):
    occ = {F:set(), B:set()}
    for fp in board.GetFootprints():
        if fp.GetReference() in ignore_refs: continue
        bb = fp.GetBoundingBox(); x0,y0=mm(bb.GetPosition()); x1=x0+pcbnew.ToMM(bb.GetWidth()); y1=y0+pcbnew.ToMM(bb.GetHeight())
        for layer in (F,B):
            for x in range(math.floor((x0-.25)/STEP), math.ceil((x1+.25)/STEP)+1):
                for y in range(math.floor((y0-.25)/STEP), math.ceil((y1+.25)/STEP)+1): occ[layer].add((x,y))
    for item in board.GetTracks():
        if isinstance(item, pcbnew.PCB_VIA):
            x,y=grid(*mm(item.GetPosition()))
            for layer in (F,B):
                # 0.45 mm via plus 0.15 mm clearance requires at least 0.60
                # mm center spacing; reserve a two-cell radius on the 0.25
                # mm routing grid.
                for dx in range(-2,3):
                    for dy in range(-2,3): occ[layer].add((x+dx,y+dy))
        else:
            mark_line(occ,item.GetLayer(),mm(item.GetStart()),mm(item.GetEnd()),.18)
    # Preserve all pads as copper obstacles, except the explicit endpoints.
    for fp in board.GetFootprints():
        if fp.GetReference() in ignore_refs: continue
        for p in fp.Pads():
            for layer in (F,B):
                if p.GetLayerSet().Contains(layer): mark_pad(occ, layer, p, .23)
    return occ

def route_path(occ, start, goal, start_layer, goal_layer):
    s=(grid(*start)[0],grid(*start)[1],start_layer); g=(grid(*goal)[0],grid(*goal)[1],goal_layer)
    # Permit departure/arrival only at the actual endpoint copper layers.
    # The previous implementation cleared a broad 7x7-cell neighborhood on
    # both layers, erasing neighboring endpoint pads in dense J7/ESD fields
    # and allowing native shorts.  Keep every other pad-field obstacle real.
    for layer, (cx,cy) in ((start_layer,(s[0],s[1])),(goal_layer,(g[0],g[1]))):
        # Remove only the terminal cell.  A broad halo erased neighboring
        # native pads in dense J7/ESD fields and let the search emit tracks
        # through power or opposite-polarity pads.
        occ[layer].discard((cx,cy))
    bounds=(grid(0,94),grid(45,162))
    q=[(0,s)]; cost={s:0}; prev={s:None}
    while q:
        _,cur=heappop(q)
        if cur==g: break
        x,y,layer=cur
        moves=[(x+1,y,layer),(x-1,y,layer),(x,y+1,layer),(x,y-1,layer),
               (x,y,F if layer==B else B)]
        for nx,ny,nl in moves:
            if not(bounds[0][0]<=nx<=bounds[1][0] and bounds[0][1]<=ny<=bounds[1][1]): continue
            if nl != layer and (nx, ny) in VIA_OCC[layer]: continue
            if (nx,ny) in occ[nl] and (nx,ny,nl)!=g: continue
            nc=cost[cur]+(18 if nl!=layer else 1)
            ns=(nx,ny,nl)
            if nc<cost.get(ns,10**9):
                cost[ns]=nc;prev[ns]=cur
                heappush(q,(nc+abs(nx-g[0])+abs(ny-g[1]),ns))
    if g not in prev: raise RuntimeError(f"no route {start}->{goal} {start_layer}->{goal_layer}")
    path=[];cur=g
    while cur is not None:path.append(cur);cur=prev[cur]
    return list(reversed(path))

def add_via(board, net, x, y):
    # Do not serialize duplicate same-net vias when the search revisits a
    # transition coordinate. A different-net via at the same point remains a
    # real collision and is intentionally not coalesced.
    for item in board.GetTracks():
        if isinstance(item, pcbnew.PCB_VIA) and item.GetNetname() == net.GetNetname():
            px, py = mm(item.GetPosition())
            if abs(px-x) < 1e-6 and abs(py-y) < 1e-6:
                return
    v=pcbnew.PCB_VIA(board);v.SetPosition(V(x,y));v.SetWidth(pcbnew.FromMM(VIA_W));v.SetDrill(pcbnew.FromMM(VIA_D));v.SetLayerPair(F,B);v.SetNet(net);board.Add(v)

def emit(board, net, path, occ):
    last=None; last_layer=None
    for a,z in zip(path,path[1:]):
        if a[2]!=z[2]:
            x,y=xy(a); add_via(board,net,x,y)
            for layer in (F,B):
                occ[layer].update((grid(x,y)[0]+dx,grid(x,y)[1]+dy) for dx in range(-2,3) for dy in range(-2,3))
                VIA_OCC[layer].update((grid(x,y)[0]+dx,grid(x,y)[1]+dy) for dx in range(-2,3) for dy in range(-2,3))
            # Continue the next-layer segment from the via itself.  Dropping
            # this start coordinate serialized dangling vias and disconnected
            # otherwise valid source-to-connector routes.
            last=(x,y);last_layer=z[2]
        else:
            if last is None: last=xy(a);last_layer=a[2]
            end=xy(z);t=pcbnew.PCB_TRACK(board);t.SetStart(V(*last));t.SetEnd(V(*end));t.SetLayer(a[2]);t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(net);board.Add(t);mark_line(occ,a[2],last,end,.14);last=end

board=pcbnew.LoadBoard(str(BASE))
VIA_OCC = {F:set(), B:set()}
for footprint in board.GetFootprints():
    for native_pad in footprint.Pads():
        for layer in (F, B):
            if native_pad.GetLayerSet().Contains(layer):
                mark_pad(VIA_OCC, layer, native_pad, .375)
mapping=[
 ('CM5_GBE_TD1_P','4','U6','6','J2','3',B),('CM5_GBE_TD1_N','6','U6','7','J2','6',B),
 ('CM5_GBE_TD0_N','10','U6','9','J2','2',F),('CM5_GBE_TD0_P','12','U6','10','J2','1',F),
 ('CM5_GBE_TD3_P','3','U9','5','J2','9',B),('CM5_GBE_TD3_N','5','U9','4','J2','10',F),
 ('CM5_GBE_TD2_N','9','U9','2','J2','8',B),('CM5_GBE_TD2_P','11','U9','1','J2','7',F)]
if os.environ.get('PISXME_ETH_RETURN_ALL_F') == '1':
    mapping = [(*entry[:-1], F) for entry in mapping]
if os.environ.get('PISXME_ETH_ROUTE_REVERSE') == '1':
    mapping = list(reversed(mapping))
occ=build_occupancy(board,{'J7','U6','U9','J2'})
# Endpoint footprints may be ignored as body obstacles for escape routing, but
# their other copper pads remain real obstacles.  The prior trial exempted the
# whole endpoint footprint and native DRC consequently found pad-field shorts.
for ref in ('J7','U6','U9','J2'):
    for p in board.FindFootprintByReference(ref).Pads():
        for layer in (F,B):
            if p.GetLayerSet().Contains(layer): mark_pad(occ, layer, p, .08)
for name,j7,esd,ep,jack,jp,return_layer in mapping:
    net=board.FindNet(name)
    if net is None: raise RuntimeError(f"missing net {name}")
    src_pad=pad(board,'J7',j7); esd_pad=pad(board,esd,ep); jack_pad=pad(board,jack,jp)
    src=pos(src_pad); mid=pos(esd_pad); dst=pos(jack_pad)
    same_esd = [p for p in board.FindFootprintByReference(esd).Pads() if p.GetNetname() == name]
    # Use the upper native pad for approach and the lower native pad for
    # departure.  This models a real package-edge dogbone instead of asking a
    # grid search to tunnel through the duplicate-pad field.
    approach_pad = min(same_esd, key=lambda p: pos(p)[1])
    depart_pad = max(same_esd, key=lambda p: pos(p)[1])
    approach = pos(approach_pad); depart = pos(depart_pad)
    open_pad(occ, pad_layer(src_pad), src_pad)
    open_pad(occ, pad_layer(approach_pad), approach_pad)
    approach_seed=(approach[0], approach[1]-0.75)
    p1=route_path(occ,src,approach_seed,pad_layer(src_pad),pad_layer(approach_pad));emit(board,net,p1,occ)
    t=pcbnew.PCB_TRACK(board);t.SetStart(V(*approach_seed));t.SetEnd(V(*approach));t.SetLayer(pad_layer(approach_pad));t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(net);board.Add(t)
    mid=approach
    # Connect duplicate same-net ESD pads from the selected pad with local
    # native-pad-aware paths, then continue to the connector.
    for other in same_esd:
        if other.GetNetname()==name and other.GetNumber()!=ep:
            po=pos(other)
            # The duplicated same-net ESD pads are adjacent package pads;
            # connect them with a native short surface segment rather than
            # asking the global router to treat the pad field as open space.
            t=pcbnew.PCB_TRACK(board);t.SetStart(V(*mid));t.SetEnd(V(*po));t.SetLayer(pad_layer(esd_pad));t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(net);board.Add(t);mark_line(occ,pad_layer(esd_pad),mid,po,.14)
            # Keep the routed terminal at the selected ESD pad. Chaining
            # duplicate package pads made the next pair's route start inside
            # the neighboring pad field and caused false self-weaving.
    # Through-hole MagJack signal pads form a dense two-row field.  Route to
    # an explicit outside-of-field entry point, then use a short native-pad
    # dogbone; routing directly to the pad center made the search model weave
    # through neighboring barrels.
    entry=(dst[0], dst[1] + (1.0 if dst[1] > 152.0 else -1.0))
    open_pad(occ, pad_layer(depart_pad), depart_pad)
    depart_seed=(depart[0], depart[1]+0.75)
    t=pcbnew.PCB_TRACK(board);t.SetStart(V(*depart));t.SetEnd(V(*depart_seed));t.SetLayer(pad_layer(depart_pad));t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(net);board.Add(t)
    p2=route_path(occ,depart_seed,entry,pad_layer(depart_pad),return_layer);emit(board,net,p2,occ)
    t=pcbnew.PCB_TRACK(board);t.SetStart(V(*entry));t.SetEnd(V(*dst));t.SetLayer(return_layer);t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(net);board.Add(t);mark_line(occ,return_layer,entry,dst,.14)
    print(name,'source',src,'esd',esd,ep,'jack',dst,'segments',len(p1)+len(p2))
board.BuildListOfNets();board.Save(str(OUT));print(OUT)
