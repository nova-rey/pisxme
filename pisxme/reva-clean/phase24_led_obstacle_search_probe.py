"""Disposable native-pad/obstacle-aware Ethernet LED support probe."""
from pathlib import Path
from heapq import heappush, heappop
import math
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_LED_BASE", str(R / "PHASE24_OFFICIAL_ETH_FULL_SUPPORT_ROUTE.kicad_pcb")))
OUT = Path(os.environ.get("PISXME_LED_OUT", str(R / "PHASE24_OFFICIAL_ETH_LED_ASTAR_PROBE.kicad_pcb")))
LIB = R / "PiSXMe_RevA_Clean.pretty"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
STEP, WIDTH = 0.5, 0.20
VIA_W, VIA_D = 0.50, 0.30

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def mm(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def G(p):
    x, y = p
    return round(x / STEP), round(y / STEP)
def XY(g): return g[0] * STEP, g[1] * STEP
def pad(b, ref, num): return b.FindFootprintByReference(ref).FindPadByNumber(str(num))
def pxy(p): return mm(p if hasattr(p, 'x') else p.GetPosition())
def layers(p): return [l for l in (F, B) if p.GetLayerSet().Contains(l)]
def ensure(b, name):
    net = b.FindNet(name)
    if net is None:
        net = pcbnew.NETINFO_ITEM(b, name); net.SetNetCode(b.GetNetCount() + 1); b.Add(net)
    return net

def point_block(occ, layer, p, radius=0.20):
    gx, gy = G(p); r = max(1, math.ceil(radius / STEP))
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            occ[layer].add((gx + dx, gy + dy))

def line_block(occ, layer, a, z, radius=0.20):
    ax, ay = G(a); zx, zy = G(z)
    count = max(abs(zx - ax), abs(zy - ay), 1)
    for i in range(count + 1):
        p = (round(ax + (zx - ax) * i / count), round(ay + (zy - ay) * i / count))
        r = max(1, math.ceil(radius / STEP))
        for dx in range(-r, r + 1):
            for dy in range(-r, r + 1): occ[layer].add((p[0] + dx, p[1] + dy))

def make_occ(b, ignored):
    occ = {F: set(), B: set()}
    # Do not turn whole footprint bounding boxes into routing keepouts: that
    # is a conservative 2-D approximation which hid usable acreage in prior
    # experiments. Copper pads and existing tracks below are the electrical
    # obstacles; native DRC remains the mechanical/copper authority.
    for item in b.GetTracks():
        if isinstance(item, pcbnew.PCB_VIA):
            q = pxy(item.GetPosition())
            point_block(occ, F, q, .35); point_block(occ, B, q, .35)
        else:
            line_block(occ, item.GetLayer(), mm(item.GetStart()), mm(item.GetEnd()), .20)
    for fp in b.GetFootprints():
        if fp.GetReference() in ignored: continue
        for p in fp.Pads():
            q = pxy(p); sx, sy = mm(p.GetSize()); drill = mm(p.GetDrillSize())[0]
            # Include the native hole-clearance envelope for large mounting
            # NPTHs/PTHs.  A pad-only point obstacle is not sufficient around
            # J7's 3.5 mm mounting holes.
            extra = 1.40 if drill >= 1.5 else .30
            r = max(sx, sy) / 2 + extra
            for layer in layers(p): point_block(occ, layer, q, r)
    return occ

def route(occ, start, goal, start_layer=F, goal_layer=F):
    s = (*G(start), start_layer); t = (*G(goal), goal_layer)
    # Only the exact endpoint cells are opened; adjacent native pads remain
    # obstacles, so dense J7/J2 fields cannot be crossed by the search.
    for layer, q in ((start_layer, s), (goal_layer, t)):
        # Open a small native pad-escape halo.  The endpoint pad itself is
        # authoritative; nearby pads remain subject to the final DRC.
        for dx in range(-2, 3):
            for dy in range(-2, 3): occ[layer].discard((q[0] + dx, q[1] + dy))
    # Use the full acreage boundary for the disposable search.  The previous
    # hand-authored probes accidentally made the search area itself a hidden
    # keepout and therefore could not distinguish routing from placement.
    bounds = (G((1, 1)), G((269, 179)))
    q = [(0, s)]; cost = {s: 0}; prev = {s: None}
    while q:
        _, cur = heappop(q)
        if cur == t: break
        x, y, layer = cur
        choices = [(x+1,y,layer),(x-1,y,layer),(x,y+1,layer),(x,y-1,layer),
                   (x,y,B if layer == F else F)]
        for nx, ny, nl in choices:
            if not (bounds[0][0] <= nx <= bounds[1][0] and bounds[0][1] <= ny <= bounds[1][1]): continue
            if (nx, ny) in occ[nl] and (nx, ny, nl) != t: continue
            step = 1 + (24 if nl != layer else 0)
            ns = (nx, ny, nl); nc = cost[cur] + step
            if nc < cost.get(ns, 10**9):
                cost[ns] = nc; prev[ns] = cur
                h = abs(nx-t[0]) + abs(ny-t[1]) + (24 if nl != t[2] else 0)
                heappush(q, (nc + h, ns))
    if t not in prev: raise RuntimeError(f"no native obstacle route {start}->{goal}")
    result = []; cur = t
    while cur is not None: result.append(cur); cur = prev[cur]
    return list(reversed(result))

def add_via(b, net, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(VIA_W)); v.SetDrill(pcbnew.FromMM(VIA_D))
    v.SetLayerPair(F, B); v.SetNet(net); b.Add(v)

def emit(b, net, path, occ):
    last = None
    for a, z in zip(path, path[1:]):
        if a[2] != z[2]:
            q = XY(a[:2]); add_via(b, net, q); point_block(occ, F, q, .35); point_block(occ, B, q, .35); last = None
            continue
        if last is None: last = XY(a[:2])
        end = XY(z[:2]); t = pcbnew.PCB_TRACK(b); t.SetStart(V(*last)); t.SetEnd(V(*end)); t.SetLayer(a[2]); t.SetWidth(pcbnew.FromMM(WIDTH)); t.SetNet(net); b.Add(t)
        line_block(occ, a[2], last, end, .20); last = end

def direct(b, net, a, z, layer=F, occ=None):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(WIDTH)); t.SetNet(net); b.Add(t)
    if occ is not None: line_block(occ, layer, a, z, .20)

b = pcbnew.LoadBoard(str(BASE)); io = pcbnew.PCB_IO_KICAD_SEXPR()
names = ('ETH_LEDY', 'ETH_LEDG', '/ETHERNET/GBE_LED_Y_K', '/ETHERNET/GBE_LED_G_K')
nets = {n: ensure(b, n) for n in names}
for n, net in nets.items():
    if net is None: raise RuntimeError(f"missing native net {n}")
for pn, n in {'15':'ETH_POWER','16':'/ETHERNET/GBE_LED_Y_K','17':'ETH_POWER','18':'/ETHERNET/GBE_LED_G_K'}.items():
    power = ensure(b, n); p = pad(b, 'J2', pn); p.SetNet(power); p.SetNetCode(power.GetNetCode())
for pn, n in {'15':'ETH_LEDG','17':'ETH_LEDY'}.items():
    p = pad(b, 'J7', pn); p.SetNet(nets[n]); p.SetNetCode(nets[n].GetNetCode())

for ref, x, y in [('R30', 38, 110), ('R31', 33, 110)]:
    fp = io.FootprintLoad(str(LIB), 'R_0402_1005Metric'); fp.SetReference(ref); fp.SetPosition(V(x, y)); fp.SetLayer(F); b.Add(fp)
    ls = pcbnew.LSET(); ls.AddLayer(F); ls.AddLayer(pcbnew.F_Mask); ls.AddLayer(pcbnew.F_Paste)
    for p in fp.Pads(): p.SetLayerSet(ls)
P = lambda ref, num: pad(b, ref, num)
for ref, a, c in [('R30','ETH_LEDY','/ETHERNET/GBE_LED_Y_K'), ('R31','ETH_LEDG','/ETHERNET/GBE_LED_G_K')]:
    P(ref, 1).SetNet(nets[a]); P(ref, 1).SetNetCode(nets[a].GetNetCode()); P(ref, 2).SetNet(nets[c]); P(ref, 2).SetNetCode(nets[c].GetNetCode())

occ = make_occ(b, {'J7','J2','R30','R31'})
for ref in ('J7','J2','R30','R31'):
    for p in b.FindFootprintByReference(ref).Pads():
        sx, sy = mm(p.GetSize()); drill = mm(p.GetDrillSize())[0]
        extra = 1.40 if drill >= 1.5 else .30
        for layer in layers(p): point_block(occ, layer, pxy(p), max(sx, sy) / 2 + extra)

jobs = [
    ('ETH_LEDY','17','R30','1','J2','16',(30.0,101.9),(37.5,109.0),(19.09,139.5),(37.5,110.5)),
    ('ETH_LEDG','15','R31','1','J2','18',(30.0,101.5),(32.5,109.0),(8.37,139.5),(32.5,110.5)),
]
for name, src_ref, rref, rnum, jref, jnum, src_exit, r1_exit, j_exit, r2_exit in jobs:
    net = nets[name]; src = pxy(P('J7', src_ref)); target = pxy(P(rref, rnum))
    direct(b, net, src, src_exit, occ=occ)
    path = route(occ, src_exit, r1_exit); emit(b, net, path, occ); direct(b, net, r1_exit, target, occ=occ)
    cath = '/ETHERNET/GBE_LED_Y_K' if name == 'ETH_LEDY' else '/ETHERNET/GBE_LED_G_K'
    cnet = nets[cath]; csrc = pxy(P(jref, jnum)); ctarget = pxy(P(rref, '2'))
    direct(b, cnet, csrc, j_exit, occ=occ)
    # Keep the long low-speed trunk on B.Cu.  Only the connector/resistor
    # dogbones are F.Cu; explicit ordinary vias make the layer contract
    # visible and prevent the search from consuming an F.Cu MDI lane.
    add_via(b, cnet, j_exit); add_via(b, cnet, r2_exit)
    path = route(occ, j_exit, r2_exit, B, B); emit(b, cnet, path, occ)
    direct(b, cnet, r2_exit, ctarget, occ=occ)
    print(name, 'source', src, 'R', target, 'cathode', csrc, 'R', ctarget)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
