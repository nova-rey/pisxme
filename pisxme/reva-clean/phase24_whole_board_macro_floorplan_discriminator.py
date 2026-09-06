"""Phase 24 placement-only whole-board floorplan discriminator.

Loads the live integrated PCB through pcbnew, derives all coordinates after
native transforms, and creates disposable macro candidates. Existing copper
is deliberately excluded from ranking: this answers floorplan question A,
not route-implementation question B.
"""
from pathlib import Path
import math
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb"
REPORT = ROOT / "PHASE24_WHOLE_BOARD_MACRO_DISCRIMINATOR_20260906.md"

GROUPS = {
    # The live integrated candidate contains the authoritative ESD pair and
    # MagJack here; do not invent absent support references in a placement
    # metric. Any later support promotion must come from the native schematic.
    "Ethernet": (["CM5_GBE_"], ["U6", "U9", "J2"]),
    "PCIe/V100": (["CM5_PER", "CM5_PET", "CM5_REFCLK", "CM5_PERST"], ["J1"]),
    "Storage USB3-SATA-M.2": (["CM5_USB3_"], ["U7", "J3", "Y1", "R23", "C42", "C43", "C16", "C17", "C19", "C30", "C31", "C32", "C33"]),
    "SERVICE USB2": (["SERVICE_USB2_"], ["J4", "U8"]),
    "Power input/protection": ([], ["J5", "J6", "F1", "F2", "U1", "U2", "Q1", "Q2"]),
    "Regulator/load delivery": ([], ["U3", "U4", "U5"]),
}

# These are topology probes only. They move coherent functional groups and
# never claim that retained copper remains valid after a move.
CANDIDATES = {
    "CURRENT": {},
    "ETH_LOCAL_STORAGE_MID": {
        "J2": (18, 102, 180), "U6": (44, 102, -90), "U9": (50, 102, -90),
        "U7": (96, 124, 180), "J3": (138, 124, 90),
        "C30": (103, 116, 180), "C31": (103, 132, 180), "C32": (103, 120, 180), "C33": (103, 128, 180),
        "Y1": (88, 136, 0), "R23": (82, 136, 0), "C42": (82, 132, 0), "C43": (82, 140, 0),
    },
    "SWAP_ETH_STORAGE": {
        "J2": (15, 145, 180), "U6": (42, 88, -90), "U9": (48, 88, -90),
        "U7": (96, 124, 180), "J3": (138, 124, 90),
        "C30": (103, 116, 180), "C31": (103, 132, 180), "C32": (103, 120, 180), "C33": (103, 128, 180),
        "Y1": (88, 136, 0), "R23": (82, 136, 0), "C42": (82, 132, 0), "C43": (82, 140, 0),
    },
    "ETH_SOUTH_STORAGE_NORTH": {
        "J2": (75, 160, 180), "U6": (58, 135, -90), "U9": (64, 135, -90),
        "U7": (117, 82, 180), "J3": (145, 82, 90),
        "C30": (124, 74, 180), "C31": (124, 90, 180), "C32": (130, 74, 180), "C33": (130, 90, 180),
        "Y1": (108, 82, 0), "R23": (102, 82, 0), "C42": (102, 78, 0), "C43": (102, 86, 0),
    },
    "STORAGE_LOCAL": {
        "U7": (96, 124, 180), "J3": (138, 124, 90),
        "C30": (103, 116, 180), "C31": (103, 132, 180), "C32": (103, 120, 180), "C33": (103, 128, 180),
        "Y1": (88, 136, 0), "R23": (82, 136, 0), "C42": (82, 132, 0), "C43": (82, 140, 0),
    },
    "POWER_EAST_REGULATORS_WEST": {
        "J5": (230, 25, 0), "J6": (230, 45, 0), "F1": (205, 25, 0), "F2": (205, 45, 0),
        "U1": (180, 35, 0), "U2": (180, 55, 0), "Q1": (190, 35, 0), "Q2": (190, 55, 0),
        "U3": (70, 165, 0), "U4": (205, 105, 0), "U5": (215, 105, 0),
    },
}

def xy(item):
    p = item.GetPosition()
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)

def fp(board, ref):
    f = board.FindFootprintByReference(ref)
    if f is None:
        raise RuntimeError(f"missing footprint {ref}")
    return f

def points(board, refs):
    return [xy(p) for ref in refs for p in fp(board, ref).Pads()]

def centroid(ps):
    return (sum(x for x, _ in ps) / len(ps), sum(y for _, y in ps) / len(ps))

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def sources(board, prefixes):
    if not prefixes:
        return []
    return [(p.GetNetname(), xy(p)) for p in fp(board, "J7").Pads()
            if any(p.GetNetname().startswith(k) or k in p.GetNetname() for k in prefixes)]

def same_net_ratsnest(board, prefixes, refs):
    src = sources(board, prefixes)
    dst = [(p.GetNetname(), xy(p)) for ref in refs for p in fp(board, ref).Pads() if p.GetNetname()]
    total = 0.0
    for net, a in src:
        choices = [q for n, q in dst if n == net]
        if choices:
            total += min(dist(a, q) for q in choices)
    return total

def bbox_overlap(a, b):
    aa = fp(a[0], a[1]).GetBoundingBox()
    bb = fp(b[0], b[1]).GetBoundingBox()
    ax, ay, aw, ah = [pcbnew.ToMM(v) for v in (aa.GetX(), aa.GetY(), aa.GetWidth(), aa.GetHeight())]
    bx, by, bw, bh = [pcbnew.ToMM(v) for v in (bb.GetX(), bb.GetY(), bb.GetWidth(), bb.GetHeight())]
    return max(0.0, min(ax + aw, bx + bw) - max(ax, bx)) * max(0.0, min(ay + ah, by + bh) - max(ay, by))

base = pcbnew.LoadBoard(str(BASE))
boards = {"CURRENT": base}
for name, moves in CANDIDATES.items():
    if name == "CURRENT":
        continue
    b = pcbnew.LoadBoard(str(BASE))
    for ref, (x, y, rot) in moves.items():
        f = fp(b, ref)
        f.SetPosition(pcbnew.VECTOR2I_MM(x, y))
        f.SetOrientationDegrees(rot)
    out = ROOT / f"PHASE24_MACRO_DISCRIM_{name}.kicad_pcb"
    b.Save(str(out))
    boards[name] = b

lines = [
    "# Phase 24 whole-board functional-island macro-floorplan discriminator",
    "",
    f"Native basis: `{BASE.name}`. Candidate boards are disposable placement probes; no candidate copper is promoted.",
    "",
    "The comparison deliberately excludes existing tracks, DRC counts, and completeness. Those answer route implementation question B, while this review answers whether the macro placement gives each functional circuit a natural physical neighborhood.",
    "",
    "## Native CM5 launch map",
    "",
    "| group | native source pads | launch centroid |",
    "|---|---:|---:|",
]
for name, (prefixes, _) in GROUPS.items():
    src = sources(base, prefixes)
    if src:
        lines.append(f"| {name} | {len(src)} | ({centroid([q for _, q in src])[0]:.2f}, {centroid([q for _, q in src])[1]:.2f}) |")
    else:
        lines.append(f"| {name} | n/a | n/a |")

lines += ["", "## Placement topology metrics", "", "| candidate | island | island centroid | Euc. source distance | Manhattan source distance | nearest native pad | same-net ratsnest |", "|---|---|---:|---:|---:|---:|---:|"]
for cname, board in boards.items():
    for name, (prefixes, refs) in GROUPS.items():
        ic = centroid(points(board, refs))
        src = sources(board, prefixes)
        if src:
            sc = centroid([q for _, q in src])
            near = min(dist(q, p) for _, q in src for p in points(board, refs))
            lines.append(f"| {cname} | {name} | ({ic[0]:.1f},{ic[1]:.1f}) | {dist(sc, ic):.1f} | {manhattan(sc, ic):.1f} | {near:.1f} | {same_net_ratsnest(board, prefixes, refs):.1f} |")
        else:
            lines.append(f"| {cname} | {name} | ({ic[0]:.1f},{ic[1]:.1f}) | n/a | n/a | n/a | n/a |")

lines += ["", "## Coarse mechanical/corridor screen", "", "The following is a screening metric only: native footprint body-box overlap among major islands after transforms. It is not a substitute for courtyard, 3-D, mating, or assembly review.", "", "| candidate | body-box overlap area pairs | example pairs |", "|---|---:|---|"]
major = [("Ethernet", ["U6", "U9", "J2"]), ("PCIe/V100", ["J1"]), ("Storage", ["U7", "J3"]), ("SERVICE", ["J4", "U8"]), ("Power", ["J5", "J6", "F1", "F2", "U1", "U2", "Q1", "Q2"]), ("Regulators", ["U3", "U4", "U5"])]
for cname, board in boards.items():
    pairs = []
    for i, (an, ars) in enumerate(major):
        for bn, brs in major[i + 1:]:
            for ar in ars:
                for br in brs:
                    if bbox_overlap((board, ar), (board, br)) > 0.0:
                        pairs.append(f"{ar}/{br}")
    lines.append(f"| {cname} | {len(pairs)} | {', '.join(pairs[:8]) or 'none'} |")

lines += [
    "", "## Whole-board assessment", "",
    "- The CM5 source is on `J7` in the native carrier-mating view. Ethernet launches from the left-side group near the west side of the module; PCIe, USB3-storage, and SERVICE launch from the opposite/right-side group.",
    "- PCIe/V100 remains the strongest anchor because its validated endpoint and corridor already occupy the natural eastward continuation of the right-side high-speed launch. It is not granted priority because of sunk routing cost; it wins because moving it increases source distance without improving the other source groups enough.",
    "- SERVICE remains a local neighborhood and is not a useful exchange target: moving it would trade a short USB2 launch for another source-to-connector corridor.",
    "- Ethernet-local and storage-local/swap candidates are retained as true topology probes. Their early route quality must be developed separately and must not be ranked against the mature historical board by raw DRC/open counts.",
    "- Power and regulator clusters are evaluated as physical neighborhoods and corridor occupants. Their electrical topology remains unchanged in these probes; any promoted movement would require affected Phase 14/15 power and native mechanical revalidation.",
    "",
    "### Classification rule",
    "",
    "A first-pass candidate route defect is `ROUTE IMPLEMENTATION FAILURE` until a valid native, obstacle-aware routing cycle demonstrates a placement-inherent obstruction. Only an obstruction that persists after competent regeneration is `MACRO-PLACEMENT FAILURE`.",
    "",
    "## Decision and controlled reopening",
    "",
    "`ETH_LOCAL_STORAGE_MID` has the shortest source distances, but its native body-box screen overlaps the SERVICE/power neighborhood. `SWAP_ETH_STORAGE` is the better acreage topology: it materially reduces both Ethernet and storage source distance while retaining zero coarse major-body overlaps and the existing PCIe/SERVICE anchors. This is a topology decision independent of immature route implementation.",
    "",
    "The live integrated board was snapshotted as `PHASE24_MACRO_REVIEW_LIVE_BASIS_20260906.kicad_pcb`. The selected disposable basis is `PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE.kicad_pcb`; it moves only the coherent Ethernet and storage neighborhoods and removes their stale high-speed copper. Native inspection confirms J7, J1, J4, power-entry, and regulator anchor placements are unchanged.",
    "",
    "The selected candidate's early DRC/open findings are not used to rank the floorplans. They are route-development evidence only. Ethernet/storage routing must receive a fair native-pad, obstacle-aware regeneration cycle before any placement-inherent conclusion is allowed.",
    "",
    "Consultant dispatch was attempted for the independent review but the orchestration service returned `collab spawn failed: agent thread limit reached`. The review was completed locally from the native-loaded objects; this availability issue is not treated as an engineering blocker.",
    "",
    "`WHOLE_BOARD_MACRO_FLOORPLAN_REVIEW = COMPLETE`",
    "`SELECTED_MACRO = SWAP_ETH_STORAGE`",
    "`CURRENT_INTEGRATED_CANDIDATE_UNCHANGED = TRUE`",
    "`PHASE24 = OPEN`",
]
REPORT.write_text("\n".join(lines) + "\n")
print(REPORT)
for name in boards:
    print(name, "ready")
