"""Regenerate the U7 clock island around the current storage obstacles.

Disposable Phase 24 experiment.  Paths are derived from serialized pads,
tracks and vias; no expected-connectivity edges are injected.
"""
from pathlib import Path
from heapq import heappush, heappop
import math
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_U7_CLOCK_SOURCE_ESCAPE.kicad_pcb"
OUT = R / "PHASE24_CLOCK_OBSTACLE_REGEN.kicad_pcb"
STEP = 0.25
WIDTH = 0.1321
CLOCK = {
    "XI": "/STORAGE/BRIDGE_XI",
    "VS": "/STORAGE/BRIDGE_VSSOSC",
    "XO": "/STORAGE/BRIDGE_XO",
}

def V(x, y):
    return pcbnew.VECTOR2I_MM(x, y)

def mm(p):
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)

def pad(fp, n):
    return next(p for p in fp.Pads() if str(p.GetNumber()) == str(n))

def grid(x, y):
    return round(x / STEP), round(y / STEP)

def xy(g):
    return g[0] * STEP, g[1] * STEP

def mark_box(occ, layer, x0, y0, x1, y1, inflate=0.20):
    if layer not in occ:
        return
    for ix in range(math.floor((min(x0, x1) - inflate) / STEP), math.ceil((max(x0, x1) + inflate) / STEP) + 1):
        for iy in range(math.floor((min(y0, y1) - inflate) / STEP), math.ceil((max(y0, y1) + inflate) / STEP) + 1):
            occ[layer].add((ix, iy))

def add_track(b, net, layer, a, z):
    t = pcbnew.PCB_TRACK(b)
    t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(WIDTH)); t.SetNet(net); b.Add(t)

def add_via(b, net, x, y):
    v = pcbnew.PCB_VIA(b)
    v.SetPosition(V(x, y)); v.SetWidth(pcbnew.FromMM(0.5))
    v.SetDrill(pcbnew.FromMM(0.3)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    v.SetNet(net); b.Add(v)

def ensure_via(b, net, x, y):
    for item in b.GetTracks():
        if isinstance(item, pcbnew.PCB_VIA):
            px, py = mm(item.GetPosition())
            if abs(px - x) < 0.01 and abs(py - y) < 0.01:
                return
    add_via(b, net, x, y)

def main():
    b = pcbnew.LoadBoard(str(BASE))
    u7 = b.FindFootprintByReference("U7")
    support = {r: b.FindFootprintByReference(r) for r in ("Y1", "R23", "C42", "C43")}
    nets = {k: b.FindNet(n) for k, n in CLOCK.items()}
    sources = {"XI": pad(u7, "52"), "VS": pad(u7, "53"), "XO": pad(u7, "54")}
    # Existing source-escape vias are the serialized, already validated launch
    # points from the oracle-derived source experiment.
    seeds = {"XI": (124.0, 125.5), "VS": (122.5, 126.5), "XO": (120.5, 137.5)}
    targets = {
        "XI": [(support["Y1"], "1", (105.5, 129.15)), (support["R23"], "1", (98.5, 130.0)), (support["C42"], "1", (98.5, 126.0))],
        "VS": [(support["Y1"], "2", (105.5, 130.85)), (support["Y1"], "4", (110.5, 129.15)), (support["C42"], "2", (103.5, 126.0)), (support["C43"], "2", (103.5, 134.0))],
        "XO": [(support["Y1"], "3", (110.5, 130.85)), (support["R23"], "2", (103.5, 130.0)), (support["C43"], "1", (98.5, 134.0))],
    }
    # Keep the footprint pads authoritative and ensure the pads are on the
    # surface layer reached by the short dogbone from each target via.
    for k, fp, pn, _ in sum(([ (k, fp, pn, off) for fp, pn, off in vals] for k, vals in targets.items()), []):
        p = pad(fp, pn); p.SetNet(nets[k]); p.SetNetCode(nets[k].GetNetCode())

    occ = {pcbnew.F_Cu: set(), pcbnew.B_Cu: set()}
    for item in b.GetTracks():
        if isinstance(item, pcbnew.PCB_VIA):
            continue
        if item.GetLayer() not in occ or item.GetNetname() in CLOCK.values():
            continue
        a, z = mm(item.GetStart()), mm(item.GetEnd())
        mark_box(occ, item.GetLayer(), a[0], a[1], z[0], z[1], 0.08)
    for fp in b.GetFootprints():
        for p in fp.Pads():
            layers = [l for l in occ if p.GetLayerSet().Contains(l)]
            px, py = mm(p.GetPosition()); sx, sy = mm(p.GetSize())
            for layer in layers:
                # Clock pads remain obstacles too; branches terminate at an
                # explicit offset via and use a short surface dogbone.
                    mark_box(occ, layer, px - sx / 2, py - sy / 2, px + sx / 2, py + sy / 2, 0.15)
    # Existing vias are obstacles on both external layers unless clock-net.
    for v in b.GetTracks():
        if not isinstance(v, pcbnew.PCB_VIA) or v.GetNetname() in CLOCK.values():
            continue
        px, py = mm(v.GetPosition())
        mark_box(occ, pcbnew.F_Cu, px, py, px, py, 0.35)
        mark_box(occ, pcbnew.B_Cu, px, py, px, py, 0.35)

    def route(net_name, start, goal):
        start = grid(*start); goal = grid(*goal)
        # The route begins at an intentional same-net via.  Its local
        # clearance reservation must not prevent the same-net departure.
        for dx in range(-3, 4):
            for dy in range(-3, 4):
                occ[pcbnew.B_Cu].discard((start[0] + dx, start[1] + dy))
        if goal in occ[pcbnew.B_Cu]:
            choices = []
            for radius in range(1, 13):
                for dx in range(-radius, radius + 1):
                    for dy in range(-radius, radius + 1):
                        candidate = (goal[0] + dx, goal[1] + dy)
                        if candidate not in occ[pcbnew.B_Cu]:
                            choices.append(candidate)
                if choices:
                    goal = min(choices, key=lambda g: abs(g[0] - start[0]) + abs(g[1] - start[1]))
                    break
        print("route", net_name, start, goal, "startblocked", start in occ[pcbnew.B_Cu], "blocked", goal in occ[pcbnew.B_Cu], "counts", len(occ[pcbnew.F_Cu]), len(occ[pcbnew.B_Cu]))
        bounds = (grid(80, 105), grid(150, 160))
        start_state = (start[0], start[1], pcbnew.B_Cu)
        goal_state = (goal[0], goal[1], pcbnew.B_Cu)
        q = [(0, start_state)]; cost = {start_state: 0}; prev = {start_state: None}
        while q:
            _, cur = heappop(q)
            if cur == goal_state:
                break
            x, y, layer = cur
            moves = [(x + 1, y, layer), (x - 1, y, layer), (x, y + 1, layer), (x, y - 1, layer),
                     (x, y, pcbnew.F_Cu if layer == pcbnew.B_Cu else pcbnew.B_Cu)]
            for nx, ny, nl in moves:
                if not (bounds[0][0] <= nx <= bounds[1][0] and bounds[0][1] <= ny <= bounds[1][1]):
                    continue
                if (nx, ny) in occ[nl] and (nx, ny) != goal:
                    continue
                step_cost = 10 if nl != layer else 1
                ns = (nx, ny, nl); nc = cost[cur] + step_cost
                if nc < cost.get(ns, 10**9):
                    cost[ns] = nc; prev[ns] = cur
                    h = abs(nx - goal[0]) + abs(ny - goal[1])
                    heappush(q, (nc + h, ns))
        if goal_state not in prev:
            raise RuntimeError(f"no route for {net_name} to {goal}")
        path = []; cur = goal_state
        while cur is not None:
            path.append(cur); cur = prev[cur]
        return list(reversed(path)), xy(goal)

    # Seed all source vias and reserve their clearances.
    for k, (sx, sy) in seeds.items():
        ensure_via(b, nets[k], sx, sy)

    anchors = dict(seeds)
    for k, vals in targets.items():
        for fp, pn, offset in vals:
            target = pad(fp, pn)
            tx, ty = mm(target.GetPosition())
            path, actual_offset = route(k, anchors[k], offset)
            last = None
            for a, z in zip(path, path[1:]):
                if a[2] != z[2]:
                    x, y = xy(a); add_via(b, nets[k], x, y)
                    for layer in occ:
                        mark_box(occ, layer, x, y, x, y, 0.35)
                    last = (x, y)
                else:
                    if last is None:
                        last = xy(a)
                    end = xy(z); add_track(b, nets[k], a[2], last, end)
                    mark_box(occ, a[2], last[0], last[1], end[0], end[1], 0.08)
                    last = end
            # Target via to SMD pad: short surface dogbone, with no via-in-pad.
            ox, oy = actual_offset
            ensure_via(b, nets[k], ox, oy)
            add_track(b, nets[k], pcbnew.F_Cu, (ox, oy), (tx, ty))
            mark_box(occ, pcbnew.F_Cu, ox, oy, tx, ty, 0.08)
            anchors[k] = (ox, oy)
            for layer in occ:
                mark_box(occ, layer, ox, oy, ox, oy, 0.35)
            print(k, fp.GetReference(), pn, "path", len(path), "target", offset)
    b.Save(str(OUT)); print(OUT)

if __name__ == "__main__":
    main()
