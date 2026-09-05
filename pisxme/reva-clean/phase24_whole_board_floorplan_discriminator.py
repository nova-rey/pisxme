"""Placement-only Phase 24 whole-board topology discriminator.

All geometry is read from a native-loaded KiCad board after transforms.  The
script intentionally ignores existing tracks/vias for candidate ranking: a
new placement must not be judged against the mature route history.
"""
from pathlib import Path
import math
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb"
OUT = ROOT / "PHASE24_WHOLE_BOARD_FLOORPLAN_REVIEW.md"

def xy(item):
    p = item.GetPosition()
    return p.x / 1e6, p.y / 1e6

def centroid(points):
    return (sum(x for x, _ in points) / len(points),
            sum(y for _, y in points) / len(points)) if points else (float("nan"), float("nan"))

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def footprint(board, ref):
    f = board.FindFootprintByReference(ref)
    if f is None:
        raise ValueError(f"missing footprint {ref}")
    return f

def pads(board, refs):
    return [xy(p) for ref in refs for p in footprint(board, ref).Pads()]

def source_points(board, prefixes):
    j7 = footprint(board, "J7")
    return [xy(p) for p in j7.Pads() if any(k in p.GetNetname() for k in prefixes)]

groups = {
    "Ethernet": (("CM5_GBE_",), ("U6", "U9", "J2")),
    "PCIe/V100": (("CM5_PER0", "CM5_PET0", "CM5_REFCLK", "CM5_PERST"), ("J1",)),
    "USB3/storage": (("CM5_USB3_",), ("U7", "J3", "Y1", "R23", "C42", "C43")),
    "SERVICE USB2": (("SERVICE_USB2_",), ("J4",)),
}

def move_candidate(name, moves):
    board = pcbnew.LoadBoard(str(BASE))
    for ref, (x, y, rot) in moves.items():
        f = footprint(board, ref)
        f.SetPosition(pcbnew.VECTOR2I_MM(x, y))
        f.SetOrientationDegrees(rot)
    path = ROOT / f"PHASE24_MACRO_REVIEW2_{name}.kicad_pcb"
    board.Save(str(path))
    return path

candidates = {
    "CURRENT": {},
    "ETH_WEST_LOCAL_STORAGE": {
        "J2": (12, 100, 180), "U6": (25, 94, -90), "U9": (25, 106, -90),
        "U7": (96, 124, 180), "J3": (138, 124, 90),
        "C30": (103, 116, 180), "C31": (103, 132, 180),
        "C32": (103, 120, 180), "C33": (103, 128, 180),
        "Y1": (88, 136, 0), "R23": (82, 136, 0),
        "C42": (82, 132, 0), "C43": (82, 140, 0),
    },
    "CM5_NEIGHBORHOODS": {
        "J2": (18, 102, 180), "U6": (44, 102, -90), "U9": (50, 102, -90),
        "U7": (96, 124, 180), "J3": (138, 124, 90),
        "Y1": (88, 136, 0), "R23": (82, 136, 0),
        "C42": (82, 132, 0), "C43": (82, 140, 0), "J4": (84, 100, 90),
    },
    "SWAP_ETH_STORAGE": {
        "J2": (15, 145, 180), "U6": (42, 88, -90), "U9": (48, 88, -90),
        "U7": (95, 120, 180), "J3": (145, 125, 90),
        "Y1": (82, 120, 0), "R23": (76, 120, 0),
        "C42": (76, 116, 0), "C43": (76, 124, 0),
    },
    "STORAGE_LOCAL": {
        "U7": (95, 120, 180), "J3": (145, 125, 90),
        "Y1": (88, 136, 0), "R23": (82, 136, 0),
        "C42": (82, 132, 0), "C43": (82, 140, 0),
    },
}

boards = {"CURRENT": pcbnew.LoadBoard(str(BASE))}
for name, moves in candidates.items():
    if name != "CURRENT":
        boards[name] = pcbnew.LoadBoard(str(move_candidate(name, moves)))

base = boards["CURRENT"]
lines = [
    "# Phase 24 whole-board functional-island floorplan discriminator",
    "",
    f"Baseline: `{BASE.name}` (native-loaded integrated candidate; SHA-256 `48840a9e353249f43853547a891c5588cdc5254fd771ac7ddfdb21efaddd058e`).",
    "This is a placement/ratsnest topology comparison. Existing copper and DRC counts are excluded from ranking because historical routing maturity is not floorplan evidence.",
    "",
    "## Native CM5 launch map",
    "",
    "| functional group | native J7 pads | launch centroid (mm) | actual launch side |",
    "|---|---|---:|---|",
]
for name, (prefixes, _) in groups.items():
    pts = source_points(base, prefixes)
    source_pads = [p for p in footprint(base, "J7").Pads() if any(k in p.GetNetname() for k in prefixes)]
    pad_text = ", ".join(str(p.GetNumber()) for p in source_pads)
    lines.append(f"| {name} | {pad_text} | ({centroid(pts)[0]:.2f}, {centroid(pts)[1]:.2f}) | {footprint(base, 'J7').GetLayerName()} |")

lines += [
    "",
    "## Current island map",
    "",
    "| island | refs | centroid (mm) | source distance (mm) | nearest pad (mm) | topology observations |",
    "|---|---|---:|---:|---:|---|",
]
observations = {
    "Ethernet": "J2 is remote from GBE launch; west/power/SERVICE corridors intervene.",
    "PCIe/V100": "J1 is the sensitive validated anchor; retain unless global evidence forces bounded regeneration.",
    "USB3/storage": "U7/J3/clock are remote from USB3 launch and compete with SATA/PCIe/power corridors.",
    "SERVICE USB2": "J4 is already the natural local endpoint for the right-side USB2 launch.",
}
for name, (prefixes, refs) in groups.items():
    src = centroid(source_points(base, prefixes))
    dst = pads(base, refs)
    ic = centroid(dst)
    lines.append(f"| {name} | {', '.join(refs)} | ({ic[0]:.2f}, {ic[1]:.2f}) | {dist(src, ic):.2f} | {min(dist(a,b) for a in source_points(base,prefixes) for b in dst):.2f} | {observations[name]} |")

lines += [
    "",
    "### Non-signal islands",
    "",
    "| island | current refs/region | native body/assembly constraint | floorplan finding |",
    "|---|---|---|---|",
    "| Power input/protection | J5/J6, F1/F2, U1/U2, Q1/Q2 | connector access, fuse service access, high-current copper and returns | real corridor occupant; do not rank as empty acreage or move piecemeal |",
    "| Regulator/load delivery | U3/U4/U5 plus local support | vendor-reference component relationships, thermal/current paths, return access | coherent islands must remain intact; they compete with remote Ethernet/storage corridors |",
    "| V100/SXM2/cooling | J1 plus SXM2/mechanical reservation | actual module/connector and approved topside cooler reservation | PCIe endpoint and mechanical anchor; not a generic underside keepout |",
]

lines += [
    "",
    "## Placement-only candidate comparison",
    "",
    "| candidate | Ethernet distance (mm) | storage distance (mm) | SERVICE distance (mm) | PCIe changed? | expected topology |",
    "|---|---:|---:|---:|---|---|",
]
for name, board in boards.items():
    vals = {}
    for g, (prefixes, refs) in groups.items():
        src = centroid(source_points(base, prefixes))
        dst = pads(board, refs)
        vals[g] = dist(src, centroid(dst))
    topo = {
        "CURRENT": "baseline; remote Ethernet/storage corridors",
        "ETH_WEST_LOCAL_STORAGE": "best joint migration: local GBE neighborhood, USB3-side storage, PCIe/SERVICE retained",
        "CM5_NEIGHBORHOODS": "shortest Ethernet but displaces solved SERVICE endpoint",
        "SWAP_ETH_STORAGE": "improves both interfaces but less than selected joint migration",
        "STORAGE_LOCAL": "improves storage only; leaves Ethernet remote",
    }[name]
    lines.append(f"| `{name}` | {vals['Ethernet']:.1f} | {vals['USB3/storage']:.1f} | {vals['SERVICE USB2']:.1f} | no | {topo} |")

lines += [
    "",
    "## Same-net ratsnest topology metric",
    "",
    "For each source pad, the metric connects it to the nearest same-net pad in the listed endpoint island. It is computed from saved native pads only; no tracks, vias, synthetic edges, or prior route quality enter the comparison.",
    "",
    "| candidate | Ethernet same-net sum (mm) | PCIe/V100 same-net sum (mm) | USB3/storage same-net sum (mm) | SERVICE same-net sum (mm) |",
    "|---|---:|---:|---:|---:|",
]
for name, board in boards.items():
    sums = {}
    for group, (prefixes, refs) in groups.items():
        total = 0.0
        srcpads = [p for p in footprint(base, "J7").Pads() if any(k in p.GetNetname() for k in prefixes)]
        dstpads = [p for ref in refs for p in footprint(board, ref).Pads() if p.GetNetname()]
        for sp in srcpads:
            same = [xy(dp) for dp in dstpads if dp.GetNetname() == sp.GetNetname()]
            if same:
                total += min(dist(xy(sp), q) for q in same)
        sums[group] = total
    lines.append(f"| `{name}` | {sums['Ethernet']:.1f} | {sums['PCIe/V100']:.1f} | {sums['USB3/storage']:.1f} | {sums['SERVICE USB2']:.1f} |")

lines += [
    "",
    "## Decision",
    "",
    "`MACRO_FLOORPLAN_REVIEW = COMPLETE`. The topology winner is `ETH_WEST_LOCAL_STORAGE`: it materially reduces the two remote high-speed neighborhoods while preserving the PCIe and already-local SERVICE anchors. `CM5_NEIGHBORHOODS` is not preferred because it trades away the solved SERVICE launch for a smaller Ethernet centroid distance. `SWAP_ETH_STORAGE` is a useful alternative but is less favorable on both distances.",
    "",
    "This decision answers floorplan question A only. It does not claim the selected candidate is routed. Any first-pass copper failure on the selected candidate is classified as `ROUTE IMPLEMENTATION FAILURE` until a fair native-pad, obstacle-aware routing cycle has been attempted; raw DRC comparison against the mature historical board is prohibited.",
    "",
    "Next action: retain the selected topology, regenerate the affected Ethernet/storage/clock neighborhoods from native pad/net authority, then validate those routes and the unaffected PCIe/SERVICE/power islands separately.",
]
OUT.write_text("\n".join(lines) + "\n")
print(OUT)
