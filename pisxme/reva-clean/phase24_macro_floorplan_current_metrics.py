"""Native topology metrics for the currently selected Phase 24 candidate.

This is deliberately route-independent: it uses transformed pad locations and
net identity only. Existing copper is not used to rank the floorplan.
"""
from pathlib import Path
import math
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_SELECTED_MACRO_ETH_SUPPORT_V15_LOCAL.kicad_pcb"
OUT = R / "PHASE24_CURRENT_MACRO_TOPOLOGY_METRICS_20260905.md"

GROUPS = {
    "Ethernet complete": ["U6", "U9", "J2", "C48", "C49", "C50", "C51", "C52", "R26", "R27", "R28", "R29"],
    "Storage complete": ["U7", "J3", "Y1", "R23", "C42", "C43", "C16", "C17", "C19", "C30", "C31", "C32", "C33"],
    "PCIe/V100": ["J1"],
    "SERVICE USB2": ["J4", "U8"],
    "Power input/protection": ["J5", "J6", "F1", "F2", "U1", "U2", "Q1", "Q2"],
    "Regulator/load delivery": ["U3", "U4", "U5"],
}
SOURCE_KEYS = {
    "Ethernet complete": ("CM5_GBE_",),
    "Storage complete": ("CM5_USB3_",),
    "PCIe/V100": ("CM5_PER", "CM5_PET", "CM5_REFCLK", "CM5_PERST"),
    "SERVICE USB2": ("SERVICE_USB2_",),
}

def pos(item):
    p = item.GetPosition()
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def fp(board, ref):
    f = board.FindFootprintByReference(ref)
    if f is None:
        raise RuntimeError(f"missing footprint {ref}")
    return f
def centroid(points):
    return (sum(x for x, _ in points) / len(points), sum(y for _, y in points) / len(points))
def euclidean(a, b): return math.hypot(a[0] - b[0], a[1] - b[1])
def manhattan(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])

board = pcbnew.LoadBoard(str(BASE))
j7 = fp(board, "J7")
def sources(keys):
    return [(p.GetNetname(), pos(p)) for p in j7.Pads() if any(k in p.GetNetname() for k in keys)]
def island_points(refs): return [pos(p) for ref in refs for p in fp(board, ref).Pads()]
def same_net_ratsnest(src, refs):
    dst = [(p.GetNetname(), pos(p)) for ref in refs for p in fp(board, ref).Pads() if p.GetNetname()]
    return sum(min((euclidean(a, q) for n, q in dst if n == net), default=0.0) for net, a in src)

lines = [
    "# Phase 24 current selected macro topology metrics", "",
    f"Basis: `{BASE.name}` (native KiCad load).", "",
    "This supplemental table closes the provenance gap in the whole-board discriminator. It uses the selected candidate with the complete translated CM5IO Ethernet support island. Metrics are transformed native pad topology only; existing copper, DRC maturity, and route completeness are excluded.", "",
    "| island | source centroid | island centroid | Euclidean centroid distance | Manhattan centroid distance | nearest endpoint pad | same-net source-to-island ratsnest |", "|---|---:|---:|---:|---:|---:|---:|",
]
for name, refs in GROUPS.items():
    pts = island_points(refs)
    ic = centroid(pts)
    if name in SOURCE_KEYS:
        src = sources(SOURCE_KEYS[name])
        sc = centroid([q for _, q in src])
        nearest = min(euclidean(q, p) for _, q in src for p in pts)
        rats = same_net_ratsnest(src, refs)
        lines.append(f"| {name} | ({sc[0]:.2f},{sc[1]:.2f}) | ({ic[0]:.2f},{ic[1]:.2f}) | {euclidean(sc,ic):.2f} mm | {manhattan(sc,ic):.2f} mm | {nearest:.2f} mm | {rats:.2f} mm |")
    else:
        lines.append(f"| {name} | n/a | ({ic[0]:.2f},{ic[1]:.2f}) | n/a | n/a | n/a | n/a |")
lines += [
    "", "## Interpretation", "",
    "The selected candidate is the basis for route development, not a production pass. The complete Ethernet support references are included in the island centroid and ratsnest calculation; the complete storage island includes bridge, M.2, clock, reset, and local support references.", "",
    "This report answers floorplan question A only. It does not use the current candidate's immature DRC/open count to reject the topology. Route implementation question B remains separately gated by native connectivity, DRC, pair geometry, references, mechanics, and full-board validation.", "",
    "`CURRENT_MACRO_TOPOLOGY_METRICS = COMPLETE`", "",
]
OUT.write_text("\n".join(lines))
print(OUT)
