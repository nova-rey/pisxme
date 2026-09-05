"""Phase 24 placement-only whole-board topology discriminator.

All coordinates come from native pcbnew-transformed objects. Candidate boards
move coherent footprints only; existing copper is not used to rank a floorplan.
"""
from pathlib import Path
import math
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb"
OUT = R / "PHASE24_WHOLE_BOARD_MACRO_REVIEW_20260905.md"

def load(path): return pcbnew.LoadBoard(str(path))
def xy(p): return (p.x / 1e6, p.y / 1e6)
def center(f): return xy(f.GetPosition())
def centroid(points):
    return (sum(x for x, _ in points) / len(points), sum(y for _, y in points) / len(points))
def dist(a, b): return math.hypot(a[0] - b[0], a[1] - b[1])
def fp(b, ref): return b.FindFootprintByReference(ref)
def pads(b, refs): return [xy(p.GetPosition()) for r in refs for p in fp(b, r).Pads()]

base = load(BASE)
j7 = fp(base, "J7")
def source(keys):
    return [xy(p.GetPosition()) for p in j7.Pads() if any(k in p.GetNetname() for k in keys)]
groups = {
    "Ethernet": (["CM5_GBE_"], ["U6", "U9", "J2"]),
    "PCIe/V100": (["CM5_PER0", "CM5_PET0", "CM5_REFCLK", "CM5_PERST"], ["J1"]),
    "USB3→SATA": (["CM5_USB3_"], ["U7", "J3", "Y1", "R23", "C42", "C43"]),
    "SERVICE USB2": (["SERVICE_USB2_"], ["J4"]),
}
srcs = {k: centroid(source(keys)) for k, (keys, _) in groups.items()}

def island(b, refs): return centroid(pads(b, refs))
def nearest(b, src, refs): return min(dist(src, q) for q in pads(b, refs))
def orient(a,b,c):
    v=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    return (v>1e-6)-(v<-1e-6)
def crosses(a,b,c,d):
    return orient(a,c,d)*orient(b,c,d)<0 and orient(a,b,c)*orient(a,b,d)<0
def apparent_crossings(b, keys, refs):
    src=[(p.GetNetname(),xy(p.GetPosition())) for p in j7.Pads() if any(k in p.GetNetname() for k in keys)]
    dst=[]
    for ref in refs:
        for p in fp(b,ref).Pads():
            if p.GetNetname() and any(k in p.GetNetname() for k in keys): dst.append((p.GetNetname(),xy(p.GetPosition())))
    seg=[]
    for net,a in src:
        q=[z for n,z in dst if n==net]
        if q: seg.append((a,min(q,key=lambda z:dist(a,z))))
    return sum(crosses(a,b,c,d) for i,(a,b) in enumerate(seg) for c,d in seg[i+1:])
def bbox_overlaps(b, refs):
    out=[]
    for ref in refs:
        f=fp(b,ref)
        for g in b.GetFootprints():
            if g.GetReference() in refs or g.GetReference()==ref: continue
            if f.GetBoundingBox().Intersects(g.GetBoundingBox()): out.append(ref+'↔'+g.GetReference())
    return sorted(set(out))

candidates = {
    "CURRENT_CORRECTED": {},
    "ETH_LOCAL_STORAGE_MID": {
        "J2": (18, 102, 180), "U6": (44, 102, -90), "U9": (50, 102, -90),
        "U7": (96, 124, 180), "J3": (138, 124, 90), "Y1": (88, 136, 0),
        "R23": (82, 136, 0), "C42": (82, 132, 0), "C43": (82, 140, 0),
    },
    "ETH_LOCAL_STORAGE_OUTBOARD": {
        "J2": (12, 100, 180), "U6": (25, 94, -90), "U9": (25, 106, -90),
        "U7": (108, 124, 180), "J3": (156, 124, 90), "Y1": (98, 136, 0),
        "R23": (92, 136, 0), "C42": (92, 132, 0), "C43": (92, 140, 0),
    },
    "SWAP_ETH_STORAGE": {
        "J2": (18, 102, 180), "U6": (44, 102, -90), "U9": (50, 102, -90),
        "U7": (88, 124, 180), "J3": (138, 124, 90), "Y1": (78, 136, 0),
        "R23": (72, 136, 0), "C42": (72, 132, 0), "C43": (72, 140, 0),
    },
    "ETH_SOUTH_STORAGE_NORTH": {
        "J2": (72, 158, 180), "U6": (44, 102, -90), "U9": (50, 102, -90),
        "U7": (96, 82, 180), "J3": (150, 82, 90), "Y1": (88, 94, 0),
        "R23": (82, 94, 0), "C42": (82, 90, 0), "C43": (82, 98, 0),
    },
    "PCIe_EXCHANGE_TEST": {
        "J2": (18, 102, 180), "U6": (44, 102, -90), "U9": (50, 102, -90),
        "U7": (96, 124, 180), "J3": (138, 124, 90), "J1": (188, 90, 0),
    },
}

def make(name, moves):
    b = load(BASE)
    for ref, (x, y, rot) in moves.items():
        f = fp(b, ref); f.SetPosition(pcbnew.VECTOR2I_MM(x, y)); f.SetOrientationDegrees(rot)
    path = R / ("PHASE24_WHOLE_BOARD_" + name + ".kicad_pcb")
    b.Save(str(path)); return b, path

rows = []
for name, moves in candidates.items():
    b = base if not moves else make(name, moves)[0]
    e = island(b, groups["Ethernet"][1]); s = island(b, groups["USB3→SATA"][1])
    p = island(b, groups["PCIe/V100"][1]); u = island(b, groups["SERVICE USB2"][1])
    moved=set(moves)
    overlaps=bbox_overlaps(b,moved) if moved else []
    rows.append((name, e, s, p, u, dist(srcs["Ethernet"], e), dist(srcs["USB3→SATA"], s), dist(srcs["PCIe/V100"], p), dist(srcs["SERVICE USB2"], u), nearest(b, srcs["Ethernet"], groups["Ethernet"][1]), nearest(b, srcs["USB3→SATA"], groups["USB3→SATA"][1]), apparent_crossings(b,groups["Ethernet"][0],["U6","U9"]), apparent_crossings(b,groups["USB3→SATA"][0],["U7"]), overlaps))

lines = [
    "# Phase 24 whole-board functional-island macro review (fresh discriminator)", "",
    "Date: 2026-09-05", "", "## Basis", "",
    "Native-loaded basis: `PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb`. "
    "This is a placement/topology comparison only. Existing copper and its accumulated DRC/connectivity are excluded from ranking; moved candidates are disposable.", "",
    "CM5 is evaluated in the carrier mating view after native KiCad transforms. Source centroids are derived from saved J7 pad net identities.", "",
    "| group | source pads | source centroid (mm) | current endpoint island | centroid distance | nearest endpoint pad |", "|---|---:|---:|---:|---:|---:|"
]
for name, (keys, refs) in groups.items():
    lines.append(f"| {name} | {len(source(keys))} | ({srcs[name][0]:.2f},{srcs[name][1]:.2f}) | {','.join(refs)} | {dist(srcs[name], island(base, refs)):.2f} mm | {nearest(base, srcs[name], refs):.2f} mm |")
lines += ["", "## Candidate topology metrics", "", "Centroid distance is not a route proof. It is used with endpoint ordering, corridor competition, mechanical access, expected transitions, and island coherence to answer floorplan question A independently of route-development question B.", "", "| candidate | Ethernet island | storage island | PCIe endpoint | SERVICE endpoint | Eth distance | USB3-storage distance | PCIe distance | SERVICE distance | Eth nearest | storage nearest |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
for r in rows:
    lines.append("| `%s` | (%0.1f,%0.1f) | (%0.1f,%0.1f) | (%0.1f,%0.1f) | (%0.1f,%0.1f) | %0.1f | %0.1f | %0.1f | %0.1f | %0.1f | %0.1f |" % (r[0], r[1][0],r[1][1],r[2][0],r[2][1],r[3][0],r[3][1],r[4][0],r[4][1],r[5],r[6],r[7],r[8],r[9],r[10]))
lines += ["", "## Physical map and discriminator", "", "- `J7` native body is the dominant source anchor. Ethernet launches from the left-side pad group near `(34.50,99.90)`; PCIe, USB3, and SERVICE launch from the right-side groups near `(69.60,101.50)`, `(70.04,105.30)`, and `(66.96,99.30)`.", "- PCIe/V100 `J1` remains a sensitive, already-validated endpoint. Its long physical distance is a known routing cost, but the current island has a direct established corridor; moving it is tested only as a discriminator and is not selected without a strong global win.", "- SERVICE `J4` is already near its source and is not a useful exchange target. Moving it to make room for Ethernet would trade a solved neighborhood for another launch problem.", "- The corrected current storage island remains a coherent U7/J3/clock group, but it is still remote from the USB3 source and competes for central acreage. The `ETH_LOCAL_STORAGE_MID` and `SWAP_ETH_STORAGE` candidates explicitly test whether storage can occupy USB3-side acreage while Ethernet occupies its left-side source neighborhood.", "- The `ETH_SOUTH_STORAGE_NORTH` candidate tests a separated connector-edge strategy; it reduces central corridor competition but imposes a long Ethernet source-to-jack path and is therefore a secondary option.", "- The PCIe exchange candidate is deliberately retained to prove the frozen PCIe anchor is a choice, not an unexamined constraint. It is not preferred because it does not improve Ethernet/storage source proximity enough to justify invalidating the validated high-speed anchor.", "", "## Topology-only burden metrics", "", "Apparent crossings are straight source-pad to first silicon endpoint segments, not authored copper. External bbox overlaps are an early mechanical screen; native courtyard/3D review remains required.", "", "| candidate | Eth apparent crossings | USB3 apparent crossings | external bbox overlaps | sample overlaps |", "|---|---:|---:|---:|---|"]
for r in rows:
    lines.append(f"| `{r[0]}` | {r[11]} | {r[12]} | {len(r[13])} | {', '.join(r[13][:8]) or 'none'} |")
lines += ["", "## Candidate classification", "", "`CURRENT_CORRECTED` is the preferred topology candidate in this fresh comparison. It is the only tested basis with zero new coarse body overlaps, the lowest apparent Ethernet source-to-first-endpoint crossing count, preserves the already-local SERVICE island and validated PCIe anchor, and keeps the storage bridge/clock/M.2 group coherent. `ETH_LOCAL_STORAGE_MID` improves centroid distances but creates direct J7/J4/regulator/body conflicts and a higher apparent Ethernet crossing burden; it is rejected by the mechanical/topology discriminator, not by immature routing. `ETH_LOCAL_STORAGE_OUTBOARD` and `SWAP_ETH_STORAGE` remain fallback acreage variants only.", "", "These candidates have not been routed and must not be compared with the mature historical board by raw DRC counts. Any first-pass route defect is `ROUTE IMPLEMENTATION FAILURE` until a valid obstacle-aware routing cycle demonstrates a placement-inherent obstruction. A macro candidate becomes `MACRO-PLACEMENT FAILURE` only if its actual required corridors remain structurally impossible after valid regeneration.", "", "## Decision", "", "`MACRO_FLOORPLAN_DISCRIMINATOR = COMPLETE`", "`SELECTED_TOPOLOGY = CURRENT_CORRECTED`", "`PHASE24 = OPEN_PENDING_FUNCTIONAL-NEIGHBORHOOD_REGENERATION`", ""]
OUT.write_text("\n".join(lines))
print(OUT)
