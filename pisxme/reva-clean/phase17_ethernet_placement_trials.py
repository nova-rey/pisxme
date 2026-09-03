"""Generate disposable Phase 17 Ethernet placement/routing-feasibility trials."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "ACREAGE_PCIE_PHASE16.kicad_pcb"
WIDTH = 0.13208


def mm(x, y):
    return pcbnew.VECTOR2I_MM(x, y)


def net(board, name):
    n = board.FindNet(name)
    if n is None:
        raise RuntimeError(name)
    return n


def track(board, a, b, n, layer):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(mm(*a)); t.SetEnd(mm(*b)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(WIDTH)); t.SetNet(n); board.Add(t)


def via(board, p, n):
    v = pcbnew.PCB_VIA(board)
    v.SetPosition(mm(*p)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30))
    v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); v.SetNet(n); board.Add(v)


def pad_center(board, ref, signal):
    fp = board.FindFootprintByReference(ref)
    for p in fp.Pads():
        if p.GetNetname().removeprefix("/ETHERNET/") == signal:
            q = p.GetPosition()
            return (q.x / 1e6, q.y / 1e6)
    raise RuntimeError(f"{ref}: {signal}")


def add_feasibility_route(board, source, target, n, layer):
    # Keep the trial conservative: a single bend corridor, no maze routing.
    sx, sy = source; tx, ty = target
    midx = (sx + tx) / 2
    track(board, source, (midx, sy), n, layer)
    track(board, (midx, sy), (midx, ty), n, layer)
    track(board, (midx, ty), target, n, layer)


def make(name, positions, orientations):
    board = pcbnew.LoadBoard(str(INPUT))
    for ref, (x, y) in positions.items():
        fp = board.FindFootprintByReference(ref)
        fp.SetPosition(mm(x, y)); fp.SetOrientationDegrees(orientations.get(ref, 0))

    # All four CM5 pairs are trialed to their corresponding ESD pad.  The
    # selected left-side trials use the same layer for the short source escape
    # so native DRC exposes any real connector breakout conflict.
    pairs = [
        ("CM5_GBE_TD0_P", "U6", pcbnew.F_Cu),
        ("CM5_GBE_TD0_N", "U6", pcbnew.B_Cu),
        ("CM5_GBE_TD1_P", "U6", pcbnew.F_Cu),
        ("CM5_GBE_TD1_N", "U6", pcbnew.B_Cu),
        ("CM5_GBE_TD2_P", "U9", pcbnew.F_Cu),
        ("CM5_GBE_TD2_N", "U9", pcbnew.B_Cu),
        ("CM5_GBE_TD3_P", "U9", pcbnew.F_Cu),
        ("CM5_GBE_TD3_N", "U9", pcbnew.B_Cu),
    ]
    j7 = board.FindFootprintByReference("J7")
    for signal, ref, layer in pairs:
        n = net(board, signal)
        source = pad_center(board, "J7", signal)
        target = pad_center(board, ref, signal)
        if layer == pcbnew.B_Cu:
            # Trial a normal through-via transition just outside the ESD body.
            tx, ty = target
            transition = (tx + (2.0 if tx < source[0] else -2.0), ty)
            via(board, transition, n)
            add_feasibility_route(board, source, transition, n, layer)
            track(board, transition, target, n, pcbnew.F_Cu)
        else:
            add_feasibility_route(board, source, target, n, layer)

    out = ROOT / f"{name}.kicad_pcb"
    board.Save(str(out))
    print(out.name)


def make_side_by_side():
    """Trial the CM5-adjacent pair-column arrangement with explicit channels."""
    board = pcbnew.LoadBoard(str(INPUT))
    for ref, pos in (("U9", (26, 100)), ("U6", (29, 101)), ("J2", (14, 119))):
        fp = board.FindFootprintByReference(ref)
        fp.SetPosition(mm(*pos)); fp.SetOrientationDegrees(90 if ref != "J2" else 180)

    # F.Cu carries the pair-1 columns (TD3 and TD1).  Each CM5 source column
    # receives its own breakout channel, so no two same-layer tracks share a
    # horizontal source corridor.
    fpaths = {
        "CM5_GBE_TD3_P": ((32.96,99.10),(31.5,99.10),(31.5,98.5),(26.75,99.25)),
        "CM5_GBE_TD3_N": ((32.96,99.50),(31.0,99.50),(31.0,101.5),(26.75,100.75)),
        "CM5_GBE_TD1_P": ((36.04,99.10),(34.5,99.10),(34.5,99.5),(29.75,100.25)),
        "CM5_GBE_TD1_N": ((36.04,99.50),(34.0,99.50),(34.0,102.0),(29.75,101.75)),
    }
    for signal, points in fpaths.items():
        route = net(board, signal)
        for a, b in zip(points, points[1:]): track(board, a, b, route, pcbnew.F_Cu)

    # B.Cu carries the pair-0 columns (TD2 and TD0).  The ordinary vias are
    # outside the ESD package; only short F.Cu dogbones touch the SMD lands.
    bpaths = {
        "CM5_GBE_TD2_N": (((32.96,100.30),(31.0,100.30),(31.0,97.5),(23.5,98.5)), (25.25,99.25)),
        "CM5_GBE_TD2_P": (((32.96,100.70),(31.5,100.70),(31.5,102.5),(23.5,101.5)), (25.25,100.75)),
        "CM5_GBE_TD0_N": (((36.04,100.30),(34.0,100.30),(34.0,99.0),(30.0,99.5)), (28.25,100.25)),
        "CM5_GBE_TD0_P": (((36.04,100.70),(34.5,100.70),(34.5,103.0),(30.0,102.5)), (28.25,101.75)),
    }
    for signal, (points, pad) in bpaths.items():
        route = net(board, signal); transition = points[-1]
        via(board, transition, route)
        for a, b in zip(points, points[1:]): track(board, a, b, route, pcbnew.B_Cu)
        track(board, transition, pad, route, pcbnew.F_Cu)

    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    out = ROOT / "ACREAGE_ETHERNET_TRIAL_CM5_ADJACENT_D2.kicad_pcb"
    board.Save(str(out)); print(out.name)


def make_side_by_side_rot180():
    """Trial one ESD per CM5 column with pair rows aligned to J7."""
    board = pcbnew.LoadBoard(str(INPUT))
    for ref, pos in (("U9", (26, 100)), ("U6", (30, 100)), ("J2", (14, 119))):
        fp = board.FindFootprintByReference(ref)
        fp.SetPosition(mm(*pos)); fp.SetOrientationDegrees(180 if ref != "J2" else 180)

    # U9 owns the left CM5 column and is kept entirely on F.Cu.
    fpaths = {
        "CM5_GBE_TD3_P": ((32.96,99.10),(31.5,98.5),(24.25,98.5),(24.25,99.25)),
        "CM5_GBE_TD3_N": ((32.96,99.50),(31.0,100.0),(25.75,100.0),(25.75,99.25)),
        "CM5_GBE_TD2_N": ((32.96,100.30),(31.0,100.5),(24.25,100.5),(24.25,100.75)),
        "CM5_GBE_TD2_P": ((32.96,100.70),(31.5,101.5),(25.75,101.5),(25.75,100.75)),
    }
    for signal, points in fpaths.items():
        n = net(board, signal)
        for a, b in zip(points, points[1:]): track(board, a, b, n, pcbnew.F_Cu)

    # U6 owns the right CM5 column.  B.Cu provides the independent layer
    # corridor; short F.Cu dogbones terminate on the rotated ESD lands.
    bpaths = {
        "CM5_GBE_TD1_P": (((36.04,99.10),(35.0,98.5),(28.0,98.5)), (29.25,99.25)),
        "CM5_GBE_TD1_N": (((36.04,99.50),(35.0,100.0),(32.0,100.0)), (30.75,99.25)),
        "CM5_GBE_TD0_N": (((36.04,100.30),(35.0,100.5),(28.0,100.5)), (29.25,100.75)),
        "CM5_GBE_TD0_P": (((36.04,100.70),(35.0,101.5),(32.0,101.5)), (30.75,100.75)),
    }
    for signal, (points, pad) in bpaths.items():
        n = net(board, signal); transition = points[-1]
        via(board, transition, n)
        for a, b in zip(points, points[1:]): track(board, a, b, n, pcbnew.B_Cu)
        track(board, transition, pad, n, pcbnew.F_Cu)

    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    out = ROOT / "ACREAGE_ETHERNET_TRIAL_CM5_ADJACENT_E.kicad_pcb"
    board.Save(str(out)); print(out.name)


def make_column_split():
    """Trial split by CM5 column: U9 B.Cu, U6 F.Cu."""
    board = pcbnew.LoadBoard(str(INPUT))
    for ref, pos in (("U9", (26, 100)), ("U6", (30, 100)), ("J2", (14, 119))):
        fp = board.FindFootprintByReference(ref)
        fp.SetPosition(mm(*pos)); fp.SetOrientationDegrees(180)
    fpaths = {
        "CM5_GBE_TD1_P": ((36.04,99.10),(34.0,98.5),(29.25,98.5),(29.25,99.25)),
        "CM5_GBE_TD1_N": ((36.04,99.50),(35.0,100.0),(30.75,100.0),(30.75,99.25)),
        "CM5_GBE_TD0_N": ((36.04,100.30),(34.0,100.5),(29.25,100.5),(29.25,100.75)),
        "CM5_GBE_TD0_P": ((36.04,100.70),(35.0,101.5),(30.75,101.5),(30.75,100.75)),
    }
    for signal, points in fpaths.items():
        n = net(board, signal)
        for a, b in zip(points, points[1:]): track(board, a, b, n, pcbnew.F_Cu)
    bpaths = {
        "CM5_GBE_TD3_P": (((32.96,99.10),(30.5,98.5),(22.5,98.5)), (24.25,99.25)),
        "CM5_GBE_TD3_N": (((32.96,99.50),(30.0,100.0),(27.5,100.0)), (25.75,99.25)),
        "CM5_GBE_TD2_N": (((32.96,100.30),(30.0,100.5),(22.5,100.5)), (24.25,100.75)),
        "CM5_GBE_TD2_P": (((32.96,100.70),(30.5,101.5),(27.5,101.5)), (25.75,100.75)),
    }
    for signal, (points, pad) in bpaths.items():
        n = net(board, signal); transition = points[-1]
        via(board, transition, n)
        for a, b in zip(points, points[1:]): track(board, a, b, n, pcbnew.B_Cu)
        track(board, transition, pad, n, pcbnew.F_Cu)
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    out = ROOT / "ACREAGE_ETHERNET_TRIAL_CM5_ADJACENT_F.kicad_pcb"
    board.Save(str(out)); print(out.name)


def make_breakout_clean():
    """Trial source-escape fanout with layer-separated CM5 columns."""
    board = pcbnew.LoadBoard(str(INPUT))
    for ref, pos in (("U9", (26, 100)), ("U6", (30, 100)), ("J2", (14, 119))):
        fp = board.FindFootprintByReference(ref)
        fp.SetPosition(mm(*pos)); fp.SetOrientationDegrees(180)

    # Leave each 0.4 mm CM5 signal pad on the side away from its adjacent
    # ground land before spreading.  U9 remains on F.Cu and U6 on B.Cu so
    # the two connector columns cannot cross in the shared escape window.
    fpaths = {
        "CM5_GBE_TD3_P": ((32.96,99.10),(32.5,99.22),(31.5,99.22),(25.25,99.25)),
        "CM5_GBE_TD3_N": ((32.96,99.50),(32.5,99.38),(31.2,99.38),(26.75,99.25)),
        "CM5_GBE_TD2_N": ((32.96,100.30),(32.5,100.20),(31.2,100.20),(25.25,100.75)),
        "CM5_GBE_TD2_P": ((32.96,100.70),(32.5,100.58),(31.5,100.58),(26.75,100.75)),
    }
    for signal, points in fpaths.items():
        n = net(board, signal)
        for a, b in zip(points, points[1:]): track(board, a, b, n, pcbnew.F_Cu)

    bpaths = {
        "CM5_GBE_TD1_P": (((36.04,99.10),(36.5,99.22),(34.5,99.22),(28.0,98.5)), (29.25,99.25)),
        "CM5_GBE_TD1_N": (((36.04,99.50),(36.5,99.38),(34.5,99.38),(32.0,99.0)), (30.75,99.25)),
        "CM5_GBE_TD0_N": (((36.04,100.30),(36.5,100.20),(34.5,100.20),(28.0,100.5)), (29.25,100.75)),
        "CM5_GBE_TD0_P": (((36.04,100.70),(36.5,100.58),(34.5,100.58),(32.0,101.5)), (30.75,100.75)),
    }
    for signal, (points, pad) in bpaths.items():
        n = net(board, signal); transition = points[-1]
        via(board, transition, n)
        for a, b in zip(points, points[1:]): track(board, a, b, n, pcbnew.B_Cu)
        track(board, transition, pad, n, pcbnew.F_Cu)
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    out = ROOT / "ACREAGE_ETHERNET_TRIAL_CM5_ADJACENT_G.kicad_pcb"
    board.Save(str(out)); print(out.name)


def make_outboard_fanout():
    """Trial outward-facing WSON pads with separated top/bottom corridors."""
    board = pcbnew.LoadBoard(str(INPUT))
    for ref, pos in (("U9", (25, 100)), ("U6", (29, 100)), ("J2", (13, 119))):
        fp = board.FindFootprintByReference(ref)
        fp.SetPosition(mm(*pos)); fp.SetOrientationDegrees(0 if ref != "J2" else 180)
    paths = {
        # U9 / left CM5 column: top corridor to pair 2, bottom corridor to pair 3.
        "CM5_GBE_TD2_P": ((32.96,100.70),(32.0,98.0),(24.25,98.0),(24.25,99.25)),
        "CM5_GBE_TD2_N": ((32.96,100.30),(33.0,97.5),(25.75,97.5),(25.75,99.25)),
        "CM5_GBE_TD3_P": ((32.96,99.10),(32.0,102.0),(25.75,102.0),(25.75,100.75)),
        "CM5_GBE_TD3_N": ((32.96,99.50),(31.0,103.0),(24.25,103.0),(24.25,100.75)),
        # U6 / right CM5 column, same topology on an independent x corridor.
        "CM5_GBE_TD0_P": ((36.04,100.70),(35.0,98.0),(28.25,98.0),(28.25,99.25)),
        "CM5_GBE_TD0_N": ((36.04,100.30),(36.0,97.5),(29.75,97.5),(29.75,99.25)),
        "CM5_GBE_TD1_P": ((36.04,99.10),(35.0,102.0),(29.75,102.0),(29.75,100.75)),
        "CM5_GBE_TD1_N": ((36.04,99.50),(34.0,103.0),(28.25,103.0),(28.25,100.75)),
    }
    for signal, points in paths.items():
        n = net(board, signal)
        for a, b in zip(points, points[1:]): track(board, a, b, n, pcbnew.F_Cu)
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    out = ROOT / "ACREAGE_ETHERNET_TRIAL_CM5_ADJACENT_H.kicad_pcb"
    board.Save(str(out)); print(out.name)


def make_ordered_west_island():
    """Complete feasibility trial: monotonic CM5 escape plus west-edge J2."""
    board = pcbnew.LoadBoard(str(INPUT))
    for ref, pos in (("U9", (25, 100)), ("U6", (29, 106)), ("J2", (12, 119))):
        fp = board.FindFootprintByReference(ref)
        fp.SetPosition(mm(*pos)); fp.SetOrientationDegrees(180)

    # The narrow segments are connector-only breakout geometry.  They are
    # intentionally confined to the J7 pad escape window; the outer channel
    # uses the normal 100R class width.
    def narrow_track(a, b, n, layer):
        t = pcbnew.PCB_TRACK(board)
        t.SetStart(mm(*a)); t.SetEnd(mm(*b)); t.SetLayer(layer)
        t.SetWidth(pcbnew.FromMM(.10)); t.SetNet(n); board.Add(t)

    def escape(signal, source, via_pos, target, layer):
        n = net(board, signal)
        narrow_track(source, via_pos, n, pcbnew.F_Cu)
        via(board, via_pos, n)
        track(board, via_pos, target, n, layer)

    # Left CM5 column -> U9, in source and package order.  Keep this entire
    # island on F.Cu after the local escapes.
    left = {
        "CM5_GBE_TD3_P": ((32.96,99.10),(31.90,99.10),(24.25,99.25)),
        "CM5_GBE_TD3_N": ((32.96,99.50),(31.55,99.50),(25.75,99.25)),
        "CM5_GBE_TD2_N": ((32.96,100.30),(31.20,100.30),(24.25,100.75)),
        "CM5_GBE_TD2_P": ((32.96,100.70),(30.85,100.70),(25.75,100.75)),
    }
    for signal, (source, vp, target) in left.items():
        escape(signal, source, vp, target, pcbnew.F_Cu)

    # Right CM5 column -> U6, using B.Cu for the outer channel.  The escape
    # leaves the J7 footprint at x=31 and drops below U9 before turning west.
    right = {
        "CM5_GBE_TD1_P": ((36.04,99.10),(35.40,99.10),(27.75,105.25)),
        "CM5_GBE_TD1_N": ((36.04,99.50),(34.95,99.50),(29.25,105.25)),
        "CM5_GBE_TD0_N": ((36.04,100.30),(34.50,100.30),(27.75,106.75)),
        "CM5_GBE_TD0_P": ((36.04,100.70),(34.05,100.70),(29.25,106.75)),
    }
    for signal, (source, vp, target) in right.items():
        n = net(board, signal)
        narrow_track(source, vp, n, pcbnew.B_Cu)
        via(board, vp, n)
        # Explicit dogleg keeps the right-column group outside U9's footprint.
        tx, ty = target
        xmid = 31.0 if ty < 106 else 31.5
        track(board, vp, (xmid, 103.5 if ty < 106 else 108.5), n, pcbnew.B_Cu)
        track(board, (xmid, 103.5 if ty < 106 else 108.5), target, n, pcbnew.B_Cu)
        via(board, target, n)

    # West-edge MDI corridors.  Pair groups use separate y lanes and P/N
    # layers; all runs remain left of the frozen J7/power geometry.
    j2_targets = {
        "CM5_GBE_TD3_N": (17.715,122.830), "CM5_GBE_TD3_P": (15.175,121.560),
        "CM5_GBE_TD2_N": (8.825,121.560), "CM5_GBE_TD2_P": (6.285,122.830),
        "CM5_GBE_TD1_N": (18.630,114.940), "CM5_GBE_TD1_P": (16.090,114.940),
        "CM5_GBE_TD0_N": (7.910,114.940), "CM5_GBE_TD0_P": (5.370,114.940),
    }
    esd_targets = {
        "CM5_GBE_TD3_P": (25.75,100.75), "CM5_GBE_TD3_N": (24.25,100.75),
        "CM5_GBE_TD2_N": (24.25,99.25), "CM5_GBE_TD2_P": (25.75,99.25),
        "CM5_GBE_TD1_P": (27.75,105.25), "CM5_GBE_TD1_N": (29.25,105.25),
        "CM5_GBE_TD0_N": (27.75,106.75), "CM5_GBE_TD0_P": (29.25,106.75),
    }
    for signal, target in j2_targets.items():
        n = net(board, signal); sx, sy = esd_targets[signal]; tx, ty = target
        lane = 111.0 + (0.55 if "TD3" in signal else 0.0) if "TD2" in signal or "TD3" in signal else 112.5 + (0.55 if "TD1" in signal else 0.0)
        layer = pcbnew.F_Cu if signal.endswith("_P") else pcbnew.B_Cu
        track(board, (sx, sy), (21.0, lane), n, layer)
        track(board, (21.0, lane), (tx, lane), n, layer)
        track(board, (tx, lane), target, n, layer)
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    out = ROOT / "ACREAGE_ETHERNET_TRIAL_ORDERED_WEST.kicad_pcb"
    board.Save(str(out)); print(out.name)


def main():
    make("ACREAGE_ETHERNET_TRIAL_LEFT_A",
         {"U6": (27, 95), "U9": (27, 106), "J2": (12, 118)},
         {"U6": 180, "U9": 180, "J2": 180})
    make("ACREAGE_ETHERNET_TRIAL_LEFT_B",
         {"U6": (27, 91), "U9": (27, 103), "J2": (12, 118)},
         {"U6": 180, "U9": 180, "J2": 180})
    make("ACREAGE_ETHERNET_TRIAL_LEFT_C",
         {"U6": (25, 94), "U9": (25, 106), "J2": (10, 119)},
         {"U6": 0, "U9": 0, "J2": 180})
    # Side-by-side 90-degree arrangement: pair-1 columns line up with the
    # upper CM5 pair rows and pair-0 columns with the lower rows.
    make("ACREAGE_ETHERNET_TRIAL_CM5_ADJACENT_D",
         {"U9": (25, 100), "U6": (29, 100), "J2": (14, 118)},
         {"U6": 90, "U9": 90, "J2": 180})
    make_side_by_side()
    make_side_by_side_rot180()
    make_column_split()
    make_breakout_clean()
    make_outboard_fanout()
    make_ordered_west_island()


if __name__ == "__main__":
    main()
