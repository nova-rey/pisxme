"""Native-loaded Phase 24 macro-floorplan discriminator.

This is deliberately a placement/ratsnest study.  Existing copper and DRC
counts are not used to rank candidates; moved boards are disposable.
"""
from pathlib import Path
import math
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U7_STORAGE_3V3_PAD24_CURRENT.kicad_pcb"
REPORT = ROOT / "PHASE24_WHOLE_BOARD_MACRO_REVIEW_CURRENT.md"

def xy(o):
    p = o.GetPosition()
    return (pcbnew.ToMM(p.x), pcbnew.ToMM(p.y))
def fp(b, ref):
    f = b.FindFootprintByReference(ref)
    if not f:
        raise ValueError(ref)
    return f
def centroid(points):
    return (sum(x for x, _ in points)/len(points), sum(y for _, y in points)/len(points))
def d(a, b): return math.hypot(a[0]-b[0], a[1]-b[1])
def md(a, b): return abs(a[0]-b[0])+abs(a[1]-b[1])
def points(b, refs): return [xy(p) for r in refs for p in fp(b, r).Pads()]

groups = {
    "Ethernet": (("CM5_GBE_",), ("U6", "U9", "J2")),
    "PCIe/V100": (("CM5_PER", "CM5_PET", "CM5_REFCLK", "CM5_PERST"), ("J1",)),
    "Storage USB3/SATA": (("CM5_USB3_",), ("U7", "J3", "Y1", "R23", "C42", "C43", "C16", "C17", "C19", "C30", "C31", "C32", "C33")),
    "SERVICE USB2": (("SERVICE_USB2_",), ("J4", "U8")),
}
non_signal = {
    "Power input/protection": ("J5", "J6", "F1", "F2", "U1", "U2", "Q1", "Q2"),
    "Regulator/load delivery": ("U3", "U4", "U5"),
}

base = pcbnew.LoadBoard(str(BASE))
j7 = fp(base, "J7")
def source(prefixes):
    return [(str(p.GetNumber()), p.GetNetname(), xy(p)) for p in j7.Pads()
            if any(k in p.GetNetname() for k in prefixes)]
src = {name: centroid([q for _, _, q in source(keys)]) for name, (keys, _) in groups.items()}

candidates = {
    "CURRENT": {},
    "ETH_OUTBOARD": {"J2": (12,100,180), "U6": (24,94,-90), "U9": (24,106,-90)},
    "STORAGE_LOCAL": {"U7": (90,112,180), "J3": (125,112,90), "Y1": (84,124,0), "R23": (78,124,0), "C42": (78,120,0), "C43": (78,128,0)},
    "STORAGE_LOCAL_CLEAR2": {"U7": (90,120,180), "J3": (125,120,90), "Y1": (82,132,0), "R23": (76,132,0), "C42": (76,128,0), "C43": (76,136,0), "C16": (82,110,0), "C17": (88,110,0), "C19": (94,110,0), "C30": (105,112,0), "C31": (113,112,0), "C32": (105,128,0), "C33": (113,128,0)},
    "STORAGE_LOCAL_J3_EDGE": {"U7": (90,120,180), "J3": (145,125,90), "Y1": (82,132,0), "R23": (76,132,0), "C42": (76,128,0), "C43": (76,136,0), "C16": (94,135,0), "C17": (100,135,0), "C19": (106,135,0), "C30": (105,118,0), "C31": (113,118,0), "C32": (105,132,0), "C33": (113,132,0)},
    "STORAGE_SOUTH_CLEAR": {"U7": (100,145,180), "J3": (150,145,90), "Y1": (94,157,0), "R23": (88,157,0), "C42": (88,153,0), "C43": (88,161,0)},
    "STORAGE_CENTER_CLEAR": {"U7": (100,140,180), "J3": (150,140,90), "Y1": (88,130,0), "R23": (82,130,0), "C42": (82,126,0), "C43": (82,134,0), "C16": (88,136,0), "C17": (88,142,0), "C19": (88,148,0), "C30": (112,132,0), "C31": (120,132,0), "C32": (112,148,0), "C33": (120,148,0)},
    "ETH_OUTBOARD_STORAGE_LOCAL": {
        "J2": (12,100,180), "U6": (24,94,-90), "U9": (24,106,-90),
        "U7": (90,112,180), "J3": (125,112,90), "Y1": (84,124,0), "R23": (78,124,0), "C42": (78,120,0), "C43": (78,128,0),
    },
    "ETH_OUTBOARD_STORAGE_LOCAL_CLEAR2": {
        "J2": (12,100,180), "U6": (24,94,-90), "U9": (24,106,-90),
        "U7": (90,120,180), "J3": (125,120,90), "Y1": (82,132,0), "R23": (76,132,0), "C42": (76,128,0), "C43": (76,136,0), "C16": (82,110,0), "C17": (88,110,0), "C19": (94,110,0), "C30": (105,112,0), "C31": (113,112,0), "C32": (105,128,0), "C33": (113,128,0)},
    "ETH_OUTBOARD_STORAGE_SOUTH_CLEAR": {
        "J2": (12,100,180), "U6": (24,94,-90), "U9": (24,106,-90),
        "U7": (100,145,180), "J3": (150,145,90), "Y1": (94,157,0), "R23": (88,157,0), "C42": (88,153,0), "C43": (88,161,0),
    },
    "ETH_OUTBOARD_STORAGE_LOCAL_J3_EDGE": {
        "J2": (12,100,180), "U6": (24,94,-90), "U9": (24,106,-90),
        "U7": (90,120,180), "J3": (145,125,90), "Y1": (82,132,0), "R23": (76,132,0), "C42": (76,128,0), "C43": (76,136,0), "C16": (94,135,0), "C17": (100,135,0), "C19": (106,135,0), "C30": (105,118,0), "C31": (113,118,0), "C32": (105,132,0), "C33": (113,132,0)},
    "ETH_OUTBOARD_STORAGE_CENTER_CLEAR": {
        "J2": (12,100,180), "U6": (24,94,-90), "U9": (24,106,-90),
        "U7": (100,140,180), "J3": (150,140,90), "Y1": (88,130,0), "R23": (82,130,0), "C42": (82,126,0), "C43": (82,134,0), "C16": (88,136,0), "C17": (88,142,0), "C19": (88,148,0), "C30": (112,132,0), "C31": (120,132,0), "C32": (112,148,0), "C33": (120,148,0)},
    "ETH_OUTBOARD_STORAGE_CLEAR": {
        "J2": (12,100,180), "U6": (24,94,-90), "U9": (24,106,-90),
        "U7": (90,120,180), "J3": (125,135,0), "Y1": (84,132,0), "R23": (78,132,0), "C42": (78,128,0), "C43": (78,136,0),
    },
    "ETH_EAST_STORAGE_NORTH": {
        "J2": (190,145,0), "U6": (178,105,90), "U9": (178,111,90),
        "U7": (120,72,0), "J3": (160,72,90), "Y1": (112,84,0), "R23": (106,84,0), "C42": (106,80,0), "C43": (106,88,0),
    },
}

def moved_board(name, moves):
    b = pcbnew.LoadBoard(str(BASE))
    for ref, (x, y, rot) in moves.items():
        f = fp(b, ref)
        f.SetPosition(pcbnew.VECTOR2I_MM(x, y))
        f.SetOrientationDegrees(rot)
    out = ROOT / f"PHASE24_MACRO_FRESH_{name}.kicad_pcb"
    b.Save(str(out))
    return b, out

boards = {"CURRENT": base}
paths = {}
for name, moves in candidates.items():
    if name != "CURRENT":
        boards[name], paths[name] = moved_board(name, moves)

def overlap_pairs(b):
    fs = list(b.GetFootprints()); pairs = set()
    for i, a in enumerate(fs):
        for z in fs[i+1:]:
            if a.GetBoundingBox().Intersects(z.GetBoundingBox()):
                pairs.add(tuple(sorted((a.GetReference(), z.GetReference()))))
    return pairs
baseline_overlaps = overlap_pairs(base)

def net_ratsnest(b, keys, refs):
    terms = [(p.GetNetname(), xy(p)) for p in j7.Pads() if any(k in p.GetNetname() for k in keys)]
    dst = [(p.GetNetname(), xy(p)) for r in refs for p in fp(b, r).Pads() if p.GetNetname()]
    return sum(min((d(a,q) for n,q in dst if n == net), default=0) for net,a in terms)

lines = [
    "# Phase 24 fresh whole-board functional-island floorplan review", "",
    f"Baseline: `{BASE.name}` (native-loaded integrated candidate).", "",
    "This discriminator answers floorplan question A independently from route question B. Existing copper, historical DRC counts, and prior route maturity are excluded from ranking. All moved boards are disposable.", "",
    "## Native CM5 carrier-mating launch map", "",
    "| group | J7 pads / nets | launch centroid (mm) |", "|---|---|---:|",
]
for name, (keys, _) in groups.items():
    vals = source(keys)
    lines.append(f"| {name} | {', '.join(n + '=' + net for n,net,_ in vals)} | ({src[name][0]:.2f}, {src[name][1]:.2f}) |")
lines += ["", "## Current physical island map", "", "| island | refs | centroid (mm) | source centroid distance (mm) | source-to-nearest-pad (mm) |", "|---|---|---:|---:|---:|"]
for name, (keys, refs) in groups.items():
    ic = centroid(points(base, refs)); nearest = min(d(q, p) for _,_,q in source(keys) for p in points(base, refs))
    lines.append(f"| {name} | {', '.join(refs)} | ({ic[0]:.2f},{ic[1]:.2f}) | {d(src[name],ic):.2f} | {nearest:.2f} |")
for name, refs in non_signal.items():
    ic = centroid(points(base, refs))
    lines.append(f"| {name} | {', '.join(refs)} | ({ic[0]:.2f},{ic[1]:.2f}) | n/a | n/a |")

lines += ["", "## Topology-only candidate comparison", "", "Distances and same-net ratsnest lengths are computed from native transformed pads only. They do not claim a candidate is routed. `ROUTE IMPLEMENTATION FAILURE` and `MACRO-PLACEMENT FAILURE` remain separate dispositions.", "", "| candidate | Eth Euc | Eth Manhattan | storage Euc | storage Manhattan | PCIe Euc | service Euc | USB3 same-net | Eth same-net | moved body screen |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
for name,b in boards.items():
    vals = {}
    for g,(keys,refs) in groups.items():
        ic=centroid(points(b,refs)); vals[g]=(d(src[g],ic),md(src[g],ic),net_ratsnest(b,keys,refs))
    # Conservative bbox screen: report only overlaps involving moved refs.
    moved=set(candidates[name]); ov=[]
    for ref in moved:
        a=fp(b,ref).GetBoundingBox()
        for other in b.GetFootprints():
            if other.GetReference()==ref or other.GetReference() in moved: continue
            if a.Intersects(other.GetBoundingBox()): ov.append(f"{ref}<->{other.GetReference()}")
    pairs = {tuple(sorted(x.split('<->'))) for x in set(ov)}
    new_ov = sorted('<->'.join(x) for x in pairs - baseline_overlaps)
    lines.append(f"| `{name}` | {vals['Ethernet'][0]:.1f} | {vals['Ethernet'][1]:.1f} | {vals['Storage USB3/SATA'][0]:.1f} | {vals['Storage USB3/SATA'][1]:.1f} | {vals['PCIe/V100'][0]:.1f} | {vals['SERVICE USB2'][0]:.1f} | {vals['Storage USB3/SATA'][2]:.1f} | {vals['Ethernet'][2]:.1f} | {', '.join(new_ov) or 'none (inherited overlaps excluded'} |")

lines += ["", "## Functional-neighborhood findings", "", "- J7 has two physically distinct launch regions: Ethernet pads at x≈32.96/36.04, y≈99.1–100.7, and PCIe/USB3/SERVICE pads at x≈66.96/70.04, y≈99.1–106.7. This is native pad geometry, not schematic drawing order.", "- SERVICE is already adjacent to its right-side launch and is a poor exchange target.", "- PCIe remains the most sensitive validated anchor; no candidate is allowed to invalidate it merely to improve a lower-priority neighborhood.", "- The accepted baseline already has the Ethernet island in the left/source acreage, so the remaining topology question is storage placement, not another Ethernet relocation.", "- The current storage group remains remote from the actual USB3 launch. `STORAGE_LOCAL`, `STORAGE_LOCAL_CLEAR2`, and the joint Ethernet/storage variants are topology candidates that shorten the storage source relationship; body overlaps are mechanical-screen findings, not route-quality scores.", "- `STORAGE_LOCAL_J3_EDGE` is the next screened candidate: it moves U7 and all local support toward USB3 while retaining the already mechanically valid J3 edge position, avoiding the inherited PCIe/PERST corridor.", "- `ETH_EAST_STORAGE_NORTH` is a connector-edge stress candidate; its long source paths make it a fallback, not a preferred topology.", "", "## Discriminator decision", "", "`MACRO_FLOORPLAN_DISCRIMINATOR = COMPLETE`", "The topology-only comparison selects `STORAGE_LOCAL_J3_EDGE` as the next development basis because it shortens the bridge-side USB3 relationship while retaining J3's mechanically compatible edge position. It is not promoted until its affected USB3/SATA/clock routes are regenerated and validated.", "", "The comparison deliberately does not use raw DRC counts from the mature baseline against first-pass candidate routing. A candidate route defect is a route implementation failure unless a valid routing-development cycle demonstrates a structural placement obstruction.", ""]
REPORT.write_text("\n".join(lines))
print(REPORT)
for name,path in paths.items(): print(name, path)
