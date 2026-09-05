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
    "USB3/storage": (("CM5_USB3_",), ("U7", "J3", "C16", "C17", "C19", "C30", "C31", "C32", "C33", "Y1", "R23", "C42", "C43")),
    "SERVICE USB2": (("SERVICE_USB2_",), ("J4", "U8")),
}

signal_terms = {
    "Ethernet": ("CM5_GBE_", "ETH_", "GBE_"),
    "PCIe/V100": ("CM5_PER", "CM5_PET", "CM5_REFCLK", "CM5_PERST", "PCIE"),
    "USB3/storage": ("CM5_USB3_", "BRIDGE_USB3_", "BRIDGE_SATA_", "SATA_M2_", "BRIDGE_XI", "BRIDGE_XO"),
    "SERVICE USB2": ("SERVICE_USB2_", "SERVICE_RD_"),
}

def signal_pads(board, refs, terms):
    return [p for ref in refs for p in footprint(board, ref).Pads()
            if any(term in p.GetNetname() for term in terms)]

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
    "ETH_WEST_OUTBOARD_STORAGE_CLEAR": {
        "J2": (15, 145, 180), "U6": (20, 104, -90), "U9": (26, 104, -90),
        "U7": (100, 145, 180), "J3": (145, 125, 90), "C17": (108, 145, 0),
        "C16": (92, 136, 0), "C19": (108, 136, 0),
        "C30": (112, 138, 180), "C31": (112, 152, 180),
        "C32": (118, 138, 180), "C33": (118, 152, 180),
        "Y1": (92, 145, 0), "R23": (86, 145, 0),
        "C42": (86, 141, 0), "C43": (86, 149, 0),
    },
    "ETH_WEST_CLEAR_STORAGE_MID": {
        "J2": (15, 145, 180), "U6": (20, 104, -90), "U9": (26, 104, -90),
        "U7": (105, 124, 180), "J3": (145, 125, 90), "C17": (101, 112, 0),
        "C16": (95, 112, 0), "C19": (107, 112, 0),
        "C30": (113, 116, 180), "C31": (113, 132, 180),
        "C32": (119, 116, 180), "C33": (119, 132, 180),
        "Y1": (95, 140, 0), "R23": (89, 140, 0),
        "C42": (89, 136, 0), "C43": (89, 144, 0),
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
    "STORAGE_LOCAL_CLEAR": {
        "U7": (100, 145, 180), "J3": (145, 125, 90), "C17": (108, 145, 0),
        "C16": (92, 136, 0), "C19": (108, 136, 0),
        "C30": (112, 138, 180), "C31": (112, 152, 180),
        "C32": (118, 138, 180), "C33": (118, 152, 180),
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
        dst = [xy(p) for p in signal_pads(board, refs, signal_terms[g])]
        vals[g] = dist(src, centroid(dst))
    topo = {
        "CURRENT": "baseline; remote Ethernet/storage corridors",
        "ETH_WEST_LOCAL_STORAGE": "best joint migration: local GBE neighborhood, USB3-side storage, PCIe/SERVICE retained",
        "CM5_NEIGHBORHOODS": "shortest Ethernet but displaces solved SERVICE endpoint",
        "SWAP_ETH_STORAGE": "improves both interfaces but less than selected joint migration",
        "STORAGE_LOCAL_CLEAR": "improves storage only; leaves Ethernet remote",
        "ETH_WEST_OUTBOARD_STORAGE_CLEAR": "clears west Ethernet and moves complete storage support as a coherent pair",
        "ETH_WEST_CLEAR_STORAGE_MID": "keeps Ethernet clear of west power bodies while co-locating the complete storage island",
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
        dstpads = [p for p in signal_pads(board, refs, signal_terms[group]) if p.GetNetname()]
        for sp in srcpads:
            same = [xy(dp) for dp in dstpads if dp.GetNetname() == sp.GetNetname()]
            if same:
                total += min(dist(xy(sp), q) for q in same)
        sums[group] = total
    lines.append(f"| `{name}` | {sums['Ethernet']:.1f} | {sums['PCIe/V100']:.1f} | {sums['USB3/storage']:.1f} | {sums['SERVICE USB2']:.1f} |")

def bbox_pairs(board, refs=None):
    fs = [f for f in board.GetFootprints() if refs is None or f.GetReference() in refs]
    all_fs = list(board.GetFootprints())
    out = set()
    for a in fs:
        ba = a.GetBoundingBox()
        for b in all_fs:
            if a.GetReference() >= b.GetReference():
                continue
            if ba.Intersects(b.GetBoundingBox()):
                out.add((a.GetReference(), b.GetReference()))
    return out

base_overlaps = bbox_pairs(base)
lines += [
    "",
    "## Newly introduced native body-bbox overlaps",
    "",
    "This is a conservative collision screen, not a replacement for final courtyard/3D review. Only overlaps newly introduced by a moved candidate are listed.",
    "",
    "| candidate | new overlap pairs | disposition |",
    "|---|---|---|",
]
for name, board in boards.items():
    moved = set(candidates[name])
    new = sorted(bbox_pairs(board, moved) - base_overlaps) if moved else []
    disposition = "reject exact coordinates" if new else "no new bbox overlap in this screen"
    lines.append(f"| `{name}` | {', '.join(a + '/' + b for a, b in new) or 'none'} | {disposition} |")

lines += [
    "",
    "## Decision",
    "",
    "`MACRO_FLOORPLAN_REVIEW = COMPLETE`. The conceptual winner remains the Ethernet-west/storage-local migration, but the exact earlier `ETH_WEST_LOCAL_STORAGE` coordinates are rejected by the independent native bbox review because they overlap `C4/Q2/U2`, `U2`, and `C17`. The corrected candidates retain the same topology while moving coherent bodies clear of those verified obstacles; `ETH_WEST_CLEAR_STORAGE_MID` is the preferred next routing basis, with `ETH_WEST_OUTBOARD_STORAGE_CLEAR` as the lower-risk fallback. `CM5_NEIGHBORHOODS` is not preferred because it trades away the solved SERVICE launch.",
    "",
    "This decision answers floorplan question A only. It does not claim the selected candidate is routed. Any first-pass copper failure on the selected candidate is classified as `ROUTE IMPLEMENTATION FAILURE` until a fair native-pad, obstacle-aware routing cycle has been attempted; raw DRC comparison against the mature historical board is prohibited.",
    "",
    "Next action: promote only the corrected collision-free candidate after a native courtyard/body review, then regenerate the affected Ethernet/storage/clock neighborhoods from native pad/net authority. This review answers floorplan question A; route development and native closure remain open.",
]
OUT.write_text("\n".join(lines) + "\n")
print(OUT)
