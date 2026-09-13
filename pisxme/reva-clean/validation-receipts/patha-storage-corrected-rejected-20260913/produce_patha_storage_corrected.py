#!/usr/bin/env python3
"""One bounded, native-pad-derived Path-A storage route producer.

This is a disposable candidate generator.  Every endpoint is looked up from
the loaded board; no coordinate is used for a component pad.  It routes the
four U7-to-cap legs, four cap-to-U13 TUSB legs, and four U13-to-J3 SATA legs.
"""
from pathlib import Path
from heapq import heappush, heappop
import math
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / 'PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb'
OUT = ROOT / 'PHASE24_PATHA_STORAGE_CORRECTED_U13_NATIVE.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
STEP = 0.25
WIDTH = pcbnew.FromMM(0.20)

def vec(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(pos): return (pcbnew.ToMM(pos.x), pcbnew.ToMM(pos.y))
def pad(board, ref, num):
    fp = board.FindFootprintByReference(ref)
    if fp is None: raise RuntimeError(f'missing footprint {ref}')
    p = fp.FindPadByNumber(str(num))
    if p is None: raise RuntimeError(f'missing pad {ref}.{num}')
    return p
def pos(board, ref, num): return xy(pad(board, ref, num).GetPosition())
def grid(p): return (int(round(p[0] / STEP)), int(round(p[1] / STEP)))
def point(g): return (g[0] * STEP, g[1] * STEP)
def mark_disc(occ, p, radius):
    gx, gy = grid(p); r = max(1, int(math.ceil(radius / STEP)))
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            if (dx * dx + dy * dy) ** 0.5 <= r + 0.25:
                occ.add((gx + dx, gy + dy))
def mark_line(occ, a, z, radius=0.30):
    ga, gz = grid(a), grid(z)
    n = max(abs(gz[0] - ga[0]), abs(gz[1] - ga[1]), 1)
    for i in range(n + 1):
        q = (round(ga[0] + (gz[0] - ga[0]) * i / n),
             round(ga[1] + (gz[1] - ga[1]) * i / n))
        mark_disc(occ, point(q), radius)
def occupied(board):
    out = {F: set(), B: set()}
    for t in board.GetTracks():
        if isinstance(t, pcbnew.PCB_VIA):
            p = xy(t.GetPosition()); mark_disc(out[F], p, 0.45); mark_disc(out[B], p, 0.45)
        else:
            layer = t.GetLayer()
            if layer in out: mark_line(out[layer], xy(t.GetStart()), xy(t.GetEnd()), 0.30)
    for fp in board.GetFootprints():
        for p in fp.Pads():
            q = xy(p.GetPosition())
            # Pad clearances are kept on their actual layer set, with a
            # conservative 0.30 mm expansion around the native land.
            radius = max(pcbnew.ToMM(p.GetSize().x), pcbnew.ToMM(p.GetSize().y)) / 2 + 0.30
            if p.IsOnLayer(F): mark_disc(out[F], q, radius)
            if p.IsOnLayer(B): mark_disc(out[B], q, radius)
    return out
def astar(board, a, z, start=F, goal=F):
    occ = occupied(board)
    s = (*grid(a), start); t = (*grid(z), goal)
    # Endpoint pads are legal copper targets.  Clear only their local
    # expansion; all neighbouring pads and all retained board copper remain
    # obstacles.
    for layer, p in ((start, a), (goal, z)):
        gx, gy = grid(p)
        for dx in range(-4, 5):
            for dy in range(-4, 5):
                occ[layer].discard((gx + dx, gy + dy))
    xmin, ymin, xmax, ymax = grid((70, 95))[0], grid((70, 95))[1], grid((230, 175))[0], grid((230, 175))[1]
    pq = [(0, s)]; prev = {s: None}; cost = {s: 0}
    while pq:
        _, cur = heappop(pq)
        if cur == t: break
        x, y, layer = cur
        for nx, ny, nl in ((x+1,y,layer),(x-1,y,layer),(x,y+1,layer),(x,y-1,layer),
                           (x,y,B if layer == F else F)):
            if not (xmin <= nx <= xmax and ymin <= ny <= ymax): continue
            if (nx, ny) in occ[nl] and (nx, ny, nl) != t: continue
            nxt = (nx, ny, nl); nc = cost[cur] + 1 + (50 if nl != layer else 0)
            if nc < cost.get(nxt, 10**12):
                cost[nxt] = nc
                h = abs(nx - t[0]) + abs(ny - t[1]) + (50 if nl != t[2] else 0)
                heappush(pq, (nc + h, nxt)); prev[nxt] = cur
    if t not in prev: raise RuntimeError(f'no obstacle-aware route {a}->{z}')
    path = []; cur = t
    while cur is not None: path.append(cur); cur = prev[cur]
    return path[::-1]
def emit(board, net, route):
    last = None; seen = set()
    for a, z in zip(route, route[1:]):
        if a[2] != z[2]:
            p = point(a[:2])
            if p not in seen:
                v = pcbnew.PCB_VIA(board); v.SetPosition(vec(*p)); v.SetWidth(pcbnew.FromMM(0.50)); v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(F, B)
                v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v); seen.add(p)
            last = None
            continue
        p1, p2, layer = point(a[:2]), point(z[:2]), a[2]
        if last is None: last = p1
        if last != p2:
            t = pcbnew.PCB_TRACK(board); t.SetStart(vec(*last)); t.SetEnd(vec(*p2)); t.SetLayer(layer); t.SetWidth(WIDTH); t.SetNet(net); t.SetNetCode(net.GetNetCode()); board.Add(t)
            last = p2

board = pcbnew.LoadBoard(str(BASE))
jobs = [
    ('BRIDGE_SATA_TX_P', ('U7','57'), ('C30','2')),
    ('BRIDGE_SATA_TX_N', ('U7','56'), ('C31','2')),
    ('BRIDGE_SATA_RX_P', ('U7','60'), ('C32','2')),
    ('BRIDGE_SATA_RX_N', ('U7','59'), ('C33','2')),
    ('TUSB_SATA_TXP', ('C30','1'), ('U13','38')),
    ('TUSB_SATA_TXN', ('C31','1'), ('U13','37')),
    ('TUSB_SATA_RXP', ('C32','1'), ('U13','36')),
    ('TUSB_SATA_RXN', ('C33','1'), ('U13','35')),
    ('M2_SATA_A_P_PCIE_TXP0', ('U13','2'), ('J3','49')),
    ('M2_SATA_A_N_PCIE_TXN0', ('U13','3'), ('J3','47')),
    ('M2_SATA_B_P_PCIE_RXN0', ('U13','6'), ('J3','41')),
    ('M2_SATA_B_N_PCIE_RXP0', ('U13','7'), ('J3','43')),
]
for name, src, dst in jobs:
    net = board.FindNet(name)
    if net is None: raise RuntimeError(f'missing net {name}')
    for t in list(board.GetTracks()):
        if t.GetNetname() == name: board.RemoveNative(t)
    a, z = pos(board, *src), pos(board, *dst)
    route = astar(board, a, z)
    emit(board, net, route)
    print(name, src, a, '->', dst, z, 'grid_points', len(route))
board.BuildListOfNets()
board.Save(str(OUT))
print('saved', OUT)
