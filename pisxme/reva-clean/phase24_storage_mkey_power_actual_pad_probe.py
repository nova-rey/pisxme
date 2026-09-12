#!/usr/bin/env python3
"""Disposable actual-pad J3 power handoff probe.

Coordinates are read from the saved candidate pads; the script adds only
same-net power copper and ordinary through vias. It is not a router or a
production promotion path.
"""
from pathlib import Path
import argparse
import pcbnew

POWER_PADS = ("2", "4", "12", "14", "16", "18", "70", "72", "74")


def pmm(x, y):
    return pcbnew.VECTOR2I(pcbnew.FromMM(x), pcbnew.FromMM(y))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output", type=Path)
    args = ap.parse_args()
    b = pcbnew.LoadBoard(str(args.input))
    if b is None:
        raise SystemExit("cannot load board")
    net = b.FindNet("STORAGE_3V3")
    if net is None:
        raise SystemExit("STORAGE_3V3 net missing")
    j3 = b.FindFootprintByReference("J3")
    u14 = b.FindFootprintByReference("U14")
    if j3 is None or u14 is None:
        raise SystemExit("J3/U14 missing")
    pads = {n: j3.FindPadByNumber(n) for n in POWER_PADS}
    if any(p is None for p in pads.values()):
        raise SystemExit("required J3 power pad missing")
    source = u14.FindPadByNumber("5")
    if source is None:
        raise SystemExit("U14.5 missing")

    def track(a, z, layer=pcbnew.F_Cu, width=0.20):
        t = pcbnew.PCB_TRACK(b)
        t.SetStart(a); t.SetEnd(z); t.SetLayer(layer)
        t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net); t.SetNetCode(net.GetNetCode())
        b.Add(t)

    def via(pos, diameter=0.60, drill=0.30):
        v = pcbnew.PCB_VIA(b); v.SetPosition(pos)
        v.SetWidth(pcbnew.FromMM(diameter)); v.SetDrill(pcbnew.FromMM(drill))
        v.SetNet(net); v.SetNetCode(net.GetNetCode())
        v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); b.Add(v)

    xy = {n: p.GetPosition() for n, p in pads.items()}
    sxy = source.GetPosition()
    # Use two native-coordinate-derived launch groups, keeping the 0.5-mm
    # socket pitch on the surface and transitioning outside the pad row.
    left = pmm(sum(xy[n].x for n in POWER_PADS[:6]) / 6 / 1_000_000,
               pcbnew.ToMM(xy[POWER_PADS[0]].y) + 3.0)
    right = pmm(sum(xy[n].x for n in POWER_PADS[6:]) / 3 / 1_000_000,
                pcbnew.ToMM(xy[POWER_PADS[0]].y) + 3.0)
    for group, junction in ((POWER_PADS[:6], left), (POWER_PADS[6:], right)):
        for n in group:
            track(xy[n], pmm(pcbnew.ToMM(xy[n].x), pcbnew.ToMM(junction.y)))
        for a, z in zip(group, group[1:]):
            track(pmm(pcbnew.ToMM(xy[a].x), pcbnew.ToMM(junction.y)),
                  pmm(pcbnew.ToMM(xy[z].x), pcbnew.ToMM(junction.y)))
        via(junction)
    trunk = pmm((left.x + right.x) / 2 / 1_000_000, pcbnew.ToMM(left.y) + 2.0)
    track(left, trunk, pcbnew.B_Cu, 0.60); track(right, trunk, pcbnew.B_Cu, 0.60)
    via(trunk)
    source_via = pmm(pcbnew.ToMM(sxy.x), pcbnew.ToMM(sxy.y) + 3.0)
    track(sxy, source_via, pcbnew.F_Cu, 0.60); via(source_via)
    track(source_via, trunk, pcbnew.B_Cu, 0.60)
    pcbnew.ZONE_FILLER(b).Fill(b.Zones())
    b.Save(str(args.output))
    print(args.output)


if __name__ == "__main__":
    main()
