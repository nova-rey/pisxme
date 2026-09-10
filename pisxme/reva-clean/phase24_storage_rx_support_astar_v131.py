"""V131: obstacle-aware native RX support escape for U11 to U12."""
from heapq import heappop, heappush
from pathlib import Path
import math
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb'
OUT = R / 'PHASE24_STORAGE_RX_SUPPORT_ASTAR_V131.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
STEP, WIDTH = .25, .13208
JOBS = (('USB_RXP1', '26', '23', (138, 137), (160, 139)),
        ('USB_RXN1', '27', '22', (140, 140), (161, 141)))


def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p):
    p = p.GetPosition() if hasattr(p, 'GetPosition') else p
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def pad(b, ref, n): return b.FindFootprintByReference(ref).FindPadByNumber(str(n))
def grid(p): return round(p[0] / STEP), round(p[1] / STEP)
def point(g): return g[0] * STEP, g[1] * STEP


def mark_line(blocked, a, z, radius=.22):
    ax, ay, zx, zy = (*grid(a), *grid(z))
    count = max(abs(zx - ax), abs(zy - ay), 1)
    q = max(1, math.ceil(radius / STEP))
    for k in range(count + 1):
        x = round(ax + (zx - ax) * k / count)
        y = round(ay + (zy - ay) * k / count)
        for dx in range(-q, q + 1):
            for dy in range(-q, q + 1): blocked.add((x + dx, y + dy))


def obstacles(b, ignored):
    blocked = set()
    for t in b.GetTracks():
        if t.GetNetname().rsplit('/', 1)[-1] in ignored: continue
        if isinstance(t, pcbnew.PCB_VIA):
            p = xy(t.GetPosition()); mark_line(blocked, p, p, .35)
        elif t.GetLayer() == B:
            mark_line(blocked, xy(t.GetStart()), xy(t.GetEnd()), .24)
    for f in b.GetFootprints():
        for p in f.Pads():
            if not p.GetLayerSet().Contains(B): continue
            q = p.GetSize()
            x, y = xy(p); rx = pcbnew.ToMM(q.x) / 2 + .18; ry = pcbnew.ToMM(q.y) / 2 + .18
            gx, gy = grid((x, y))
            for i in range(-math.ceil(rx / STEP), math.ceil(rx / STEP) + 1):
                for j in range(-math.ceil(ry / STEP), math.ceil(ry / STEP) + 1): blocked.add((gx + i, gy + j))
    return blocked


def route(blocked, a, z):
    s, t = grid(a), grid(z)
    for p in (s, t):
        for i in range(-1, 2):
            for j in range(-1, 2): blocked.discard((p[0] + i, p[1] + j))
    queue, cost, previous = [(0, s)], {s: 0}, {s: None}
    while queue:
        _, c = heappop(queue)
        if c == t: break
        for n in ((c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1)):
            if not (400 <= n[0] <= 900 and 350 <= n[1] <= 800) or n in blocked: continue
            value = cost[c] + 1
            if value < cost.get(n, 10**9):
                cost[n] = value; previous[n] = c
                heappush(queue, (value + abs(n[0] - t[0]) + abs(n[1] - t[1]), n))
    if t not in previous: raise RuntimeError(f'no native B.Cu route {a}->{z}')
    result, c = [], t
    while c is not None: result.append(point(c)); c = previous[c]
    return result[::-1]


def track(b, n, a, z, layer):
    q = pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z)); q.SetLayer(layer)
    q.SetWidth(pcbnew.FromMM(WIDTH)); q.SetNet(n); b.Add(q)
def via(b, n, p):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(n); b.Add(q)


b = pcbnew.LoadBoard(str(BASE))
for name, _, _, _, _ in JOBS:
    for t in list(b.GetTracks()):
        if t.GetNetname().rsplit('/', 1)[-1] == name: b.RemoveNative(t)
blocked = obstacles(b, {j[0] for j in JOBS})
for name, u11n, u12n, source_via, target_via in JOBS:
    n = b.FindNet(name) or b.FindNet('/STORAGE/' + name)
    if n is None: raise RuntimeError('missing ' + name)
    src, dst = xy(pad(b, 'U11', u11n)), xy(pad(b, 'U12', u12n))
    if name == 'USB_RXP1':
        track(b, n, src, (138.8, 138.6), F); track(b, n, (138.8, 138.6), source_via, F)
        track(b, n, target_via, (157.6, target_via[1]), F)
    else:
        track(b, n, src, (139.8, 138.6), F); track(b, n, (139.8, 138.6), source_via, F)
        track(b, n, target_via, (157.6, target_via[1]), F)
    via(b, n, source_via)
    path = route(blocked, source_via, target_via)
    for a, z in zip(path, path[1:]): track(b, n, a, z, B); mark_line(blocked, a, z)
    via(b, n, target_via)
    track(b, n, (157.6, target_via[1]), (157.6, dst[1]), F)
    track(b, n, (157.6, dst[1]), dst, F)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
