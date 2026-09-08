"""Native-pad obstacle-aware JMS583 support routing experiment."""
from pathlib import Path
from heapq import heappush, heappop
import math
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_DUAL_MODE_STORAGE_USB3_LOCAL_FROM_FULL7.kicad_pcb'
OUT = R / 'PHASE24_DUAL_MODE_STORAGE_USB3_SUPPORT_ASTAR.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
STEP, WIDTH = .25, .20
LAYERS = (F, B)

def V(q): return pcbnew.VECTOR2I_MM(float(q[0]), float(q[1]))
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def pad(b, r, n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def pos(b, r, n): return xy(pad(b, r, n).GetPosition())
def grid(q): return round(q[0] / STEP), round(q[1] / STEP)
def point(g): return g[0] * STEP, g[1] * STEP

def block(s, q, radius=.25):
    x, y = grid(q); r = max(1, math.ceil(radius / STEP))
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1): s.add((x + dx, y + dy))
def line_block(s, a, z, radius=.22):
    ax, ay = grid(a); zx, zy = grid(z); count = max(abs(zx-ax), abs(zy-ay), 1)
    for i in range(count + 1):
        q = (ax + (zx-ax)*i/count, ay + (zy-ay)*i/count)
        block(s, point((round(q[0]), round(q[1]))), radius)

def occupancy(b):
    occ = {F: set(), B: set()}
    for item in b.GetTracks():
        if isinstance(item, pcbnew.PCB_VIA):
            q = xy(item.GetPosition()); block(occ[F], q, .38); block(occ[B], q, .38)
        else:
            line_block(occ[item.GetLayer()], xy(item.GetStart()), xy(item.GetEnd()), .24)
    for f in b.GetFootprints():
        for p in f.Pads():
            q = xy(p.GetPosition()); size = xy(p.GetSize())
            radius = max(size) / 2 + (.35 if p.GetDrillSize().x == 0 else .75)
            for l in LAYERS: block(occ[l], q, radius)
    return occ

def astar(occ, start, goal):
    s = (*grid(start), F); t = (*grid(goal), F)
    local = {F: set(occ[F]), B: set(occ[B])}
    for l, q in ((F, s), (F, t)):
        cells = 8  # 2 mm bounded escape allowance for the active terminal only
        for dx in range(-cells, cells + 1):
            for dy in range(-cells, cells + 1): local[l].discard((q[0]+dx, q[1]+dy))
    bounds = (grid((5, 95)), grid((180, 170)))
    queue = [(0, s)]; cost = {s: 0}; prev = {s: None}; closed = set()
    while queue:
        _, cur = heappop(queue)
        if cur in closed: continue
        closed.add(cur)
        if cur == t: break
        x, y, l = cur
        for nx, ny, nl in ((x+1,y,l),(x-1,y,l),(x,y+1,l),(x,y-1,l),
                           (x,y,B if l == F else F)):
            if not (bounds[0][0] <= nx <= bounds[1][0] and bounds[0][1] <= ny <= bounds[1][1]): continue
            if (nx, ny) in local[nl] and (nx, ny, nl) != t: continue
            ns = (nx, ny, nl); nc = cost[cur] + 1 + (35 if nl != l else 0)
            if nc < cost.get(ns, 10**12):
                cost[ns] = nc; prev[ns] = cur
                h = abs(nx-t[0]) + abs(ny-t[1]) + (35 if nl != t[2] else 0)
                heappush(queue, (nc+h, ns))
    if t not in prev: raise RuntimeError(f'no route {start}->{goal}')
    out = []; cur = t
    while cur is not None: out.append(cur); cur = prev[cur]
    return list(reversed(out))

def emit(b, n, route, occ):
    last = None; vias = set()
    for a, z in zip(route, route[1:]):
        if a[2] != z[2]:
            q = point(a[:2])
            if q not in vias:
                v = pcbnew.PCB_VIA(b); v.SetPosition(V(q)); v.SetWidth(pcbnew.FromMM(.55)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F, B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v); vias.add(q)
            last = None; continue
        a1, z1 = point(a[:2]), point(z[:2])
        if last is None: last = a1
        if last != z1:
            t = pcbnew.PCB_TRACK(b); t.SetStart(V(last)); t.SetEnd(V(z1)); t.SetLayer(a[2]); t.SetWidth(pcbnew.FromMM(WIDTH)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
            line_block(occ[a[2]], last, z1, .24); last = z1

b = pcbnew.LoadBoard(str(BASE))
jobs = [
 ('JMS_VDDREG_5V','U11','1','L10','2'), ('LXO','U11','64','L10','1'),
 ('XIN','U11','50','Y10','1'), ('XOUT','U11','51','Y10','2'),
 ('JMS_REXT','U11','39','R80','1'), ('JMS_AVDD33','U11','19','C80','1'),
 ('JMS_RESET_N','U11','15','R81','1'), ('JMS_RESET_N','R81','1','C85','1'),
 ('VBUS','U11','16','R82','1'), ('JMS_VBUS_SENSE','R82','2','R83','1'),
 ('JMS_AVDDL','U11','20','C83','1'), ('JMS_VCCO','U11','6','C81','1'),
 ('JMS_VCCK','U11','2','C82','1'), ('JMS_XAVDDH','U11','52','C84','1'),
]
for name, ra, pa, rb, pb in jobs:
    n = b.FindNet(name)
    for item in list(b.GetTracks()):
        if item.GetNetCode() == n.GetNetCode(): b.RemoveNative(item)
occ = occupancy(b)
for name, ra, pa, rb, pb in jobs:
    n = b.FindNet(name); route = astar(occ, pos(b, ra, pa), pos(b, rb, pb)); emit(b, n, route, occ)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
