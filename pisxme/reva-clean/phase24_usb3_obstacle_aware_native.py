"""Disposable native-pad USB3 router for the selected Phase 24 macro.

Occupancy is derived from the saved PCB. Expected endpoints are only input
assertions; this script never adds synthetic connectivity edges.
"""
from pathlib import Path
from heapq import heappush, heappop
import os, math, pcbnew

R = Path(__file__).resolve().parent
BASE = Path(os.environ.get("P24_USB3_BASE", str(R / "PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb")))
OUT = Path(os.environ.get("P24_USB3_OUT", str(R / "PHASE24_USB3_OBSTACLE_AWARE_NATIVE.kicad_pcb")))
F, B = pcbnew.F_Cu, pcbnew.B_Cu
STEP, WIDTH = 0.25, 0.13208
LAYERS = (F, B)
JOBS = (("CM5_USB3_RX_N", "128", "42"), ("CM5_USB3_RX_P", "130", "43"),
        ("CM5_USB3_TX_N", "140", "45"), ("CM5_USB3_TX_P", "142", "46"))

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def mm(p): return (pcbnew.ToMM(p.x), pcbnew.ToMM(p.y))
def grid(p): return (round(p[0] / STEP), round(p[1] / STEP))
def point(g): return (g[0] * STEP, g[1] * STEP)
def layers(p): return [l for l in LAYERS if p.GetLayerSet().Contains(l)]

def add_disc(s, layer, p, radius):
    x, y = grid(p); r = max(1, math.ceil(radius / STEP))
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1): s[layer].add((x + dx, y + dy))

def add_line(s, layer, a, z, radius):
    ax, ay = grid(a); zx, zy = grid(z); n = max(abs(zx - ax), abs(zy - ay), 1)
    r = max(1, math.ceil(radius / STEP))
    for i in range(n + 1):
        x = round(ax + (zx - ax) * i / n); y = round(ay + (zy - ay) * i / n)
        for dx in range(-r, r + 1):
            for dy in range(-r, r + 1): s[layer].add((x + dx, y + dy))

def occupancy(board):
    out = {F: set(), B: set()}
    for t in board.GetTracks():
        if any(n in t.GetNetname() for n, _, _ in JOBS): continue
        if isinstance(t, pcbnew.PCB_VIA):
            p = mm(t.GetPosition()); add_disc(out, F, p, .38); add_disc(out, B, p, .38)
        else: add_line(out, t.GetLayer(), mm(t.GetStart()), mm(t.GetEnd()), .22)
    for fp in board.GetFootprints():
        for pad in fp.Pads():
            p = mm(pad.GetPosition()); size = pad.GetSize()
            radius = max(pcbnew.ToMM(size.x), pcbnew.ToMM(size.y)) / 2 + .30
            ls = layers(pad)
            if pad.GetDrillSize().x or pad.GetDrillSize().y:
                ls = list(set(ls) | set(LAYERS))
            for layer in ls: add_disc(out, layer, p, radius)
    return out

def astar(blocked, start, goal, start_layer=F, goal_layer=F):
    local = {F: set(blocked[F]), B: set(blocked[B])}
    s, t = (*grid(start), start_layer), (*grid(goal), goal_layer)
    # Bounded SMD/connector escape allowance around the actual terminal only.
    for layer, q in ((start_layer, s), (goal_layer, t)):
        r = math.ceil(1.5 / STEP)
        for dx in range(-r, r + 1):
            for dy in range(-r, r + 1): local[layer].discard((q[0] + dx, q[1] + dy))
    q, cost, prev = [(0, s)], {s: 0}, {s: None}
    bounds = (grid((1, 1)), grid((299, 179)))
    while q:
        _, cur = heappop(q)
        if cur == t: break
        x, y, layer = cur
        for nx, ny, nl in ((x+1,y,layer),(x-1,y,layer),(x,y+1,layer),(x,y-1,layer),
                           (x,y,B if layer == F else F)):
            if not (bounds[0][0] <= nx <= bounds[1][0] and bounds[0][1] <= ny <= bounds[1][1]): continue
            if (nx, ny) in local[nl] and (nx, ny, nl) != t: continue
            nxt = (nx, ny, nl); step = 1 + (36 if nl != layer else 0)
            new = cost[cur] + step
            if new < cost.get(nxt, 10**12):
                cost[nxt] = new; prev[nxt] = cur
                h = abs(nx - t[0]) + abs(ny - t[1]) + (36 if nl != t[2] else 0)
                heappush(q, (new + h, nxt))
    if t not in prev: raise RuntimeError(f"no native route {start}->{goal}")
    path, cur = [], t
    while cur is not None: path.append(cur); cur = prev[cur]
    return list(reversed(path))

def via(board, net, p):
    v = pcbnew.PCB_VIA(board); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F, B); v.SetNet(net); board.Add(v)

def emit(board, net, path, blocked):
    last = None
    for a, z in zip(path, path[1:]):
        if a[2] != z[2]:
            p = point(a[:2]); via(board, net, p); add_disc(blocked, F, p, .40); add_disc(blocked, B, p, .40); last = None
        else:
            if last is None: last = point(a[:2])
            end = point(z[:2]); t = pcbnew.PCB_TRACK(board); t.SetStart(V(*last)); t.SetEnd(V(*end)); t.SetLayer(a[2]); t.SetWidth(pcbnew.FromMM(WIDTH)); t.SetNet(net); board.Add(t)
            add_line(blocked, a[2], last, end, .22); last = end

board = pcbnew.LoadBoard(str(BASE))
if board is None: raise RuntimeError(f"cannot load {BASE}")
terms = []
for name, jpad, upad in JOBS:
    j = board.FindFootprintByReference("J7").FindPadByNumber(jpad)
    u = board.FindFootprintByReference("U7").FindPadByNumber(upad)
    if j is None or u is None: raise RuntimeError(f"missing native terminal for {name}")
    terms.append((name, mm(j.GetPosition()), mm(u.GetPosition())))
for t in list(board.GetTracks()):
    if any(n in t.GetNetname() for n, _, _ in JOBS): board.Remove(t)
# Re-load after mutation to avoid stale KiCad 10 SWIG track wrappers.
reload_path = OUT.with_suffix('.routing_base.kicad_pcb')
board.Save(str(reload_path))
board = pcbnew.LoadBoard(str(reload_path))
blocked = occupancy(board)
for name, start, goal in terms:
    net = board.FindNet('/CORE_CM5/' + name)
    path = astar(blocked, start, goal)
    emit(board, net, path, blocked)
    print(name, 'length_mm', round(sum(math.hypot(point(a[:2])[0]-point(z[:2])[0], point(a[:2])[1]-point(z[:2])[1]) for a,z in zip(path,path[1:])) , 3), 'transitions', sum(a[2] != z[2] for a,z in zip(path,path[1:])))
board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
