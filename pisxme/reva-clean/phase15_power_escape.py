"""Add the repeatable pad-edge VIN/VOUT escape for TPSM63606 modules."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "ACREAGE_REGULATOR_PHASE15.kicad_pcb"
OUTPUT = ROOT / "ACREAGE_REGULATOR_POWER_ESCAPE_PHASE15.kicad_pcb"

MODULES = {
    "U3": {"vin": ("C5", "C6"), "vout": ("C7", "C8"),
           "xy": {"C5": (47, 76), "C6": (47, 78.25), "C7": (57, 81.5), "C8": (57, 83.5)}},
    "U4": {"vin": ("C14", "C15"), "vout": ("C16", "C17", "C19"),
           "xy": {"C14": (219, 103), "C15": (219, 105.25),
                  "C16": (220, 112), "C17": (220, 114), "C19": (220, 116)}},
}

U5_VIN = (("C23", (229, 112), ("1",), ((232.05, 103), (230.75, 103), (230.75, 111.5), (230.1, 112))),
          ("C24", (229, 115), ("5",), ((232.30, 105.25), (230.25, 105.25), (230.25, 114.5), (230.1, 115))),
          ("C25", (229, 118), ("5",), ((232.30, 105.25), (230.0, 105.25), (230.0, 117.5), (230.1, 118))))


def add_track(board, start, end, net):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(start); t.SetEnd(end); t.SetLayer(pcbnew.F_Cu)
    t.SetWidth(pcbnew.FromMM(0.30)); t.SetNet(net); board.Add(t)


def add_polyline(board, points, net):
    for a, b in zip(points, points[1:]):
        add_track(board, pcbnew.VECTOR2I_MM(*a), pcbnew.VECTOR2I_MM(*b), net)


def main():
    b = pcbnew.LoadBoard(str(INPUT))
    for uref, spec in MODULES.items():
        u = b.FindFootprintByReference(uref)
        upads = {p.GetNumber(): p for p in u.Pads()}
        groups = ((spec["vin"], ("1", "5"), -1),
                  (spec["vout"], ("8",) if uref == "U4" else ("9",),
                   -1 if uref == "U4" else 1))
        for refs, target_numbers, side in groups:
            for ref in refs:
                fp = b.FindFootprintByReference(ref)
                fp.SetPosition(pcbnew.VECTOR2I_MM(*spec["xy"][ref]))
                fp.SetOrientationDegrees(180 if (side < 0) else 0)
                active = next(p for p in fp.Pads()
                              if p.GetNetname() not in ("/REGULATORS/POWER_GND", ""))
                targets = [upads[n] for n in target_numbers
                           if upads[n].GetNetname() == active.GetNetname()]
                if not targets:
                    raise SystemExit(f"no target for {uref}:{ref} {active.GetNetname()}")
                target = min(targets, key=lambda p: abs(p.GetPosition().y - active.GetPosition().y))
                edge = pcbnew.VECTOR2I(
                    target.GetPosition().x + int(target.GetSize().x / 2) * side,
                    target.GetPosition().y)
                add_track(b, edge, active.GetPosition(), target.GetNet())
    # U5's three VIN capacitors escape down the left side of the package to
    # stay clear of U4's output island and the U7 storage bridge above it.
    u5 = b.FindFootprintByReference("U5")
    u5pads = {p.GetNumber(): p for p in u5.Pads()}
    for ref, pos, target_nums, route in U5_VIN:
        fp = b.FindFootprintByReference(ref)
        fp.SetPosition(pcbnew.VECTOR2I_MM(*pos)); fp.SetOrientationDegrees(180)
        active = next(p for p in fp.Pads() if p.GetNetname() not in ("/REGULATORS/POWER_GND", ""))
        target = next(u5pads[n] for n in target_nums if u5pads[n].GetNetname() == active.GetNetname())
        add_polyline(b, route, target.GetNet())
    pcbnew.ZONE_FILLER(b).Fill(b.Zones())
    b.Save(str(OUTPUT))
    print("Phase 15 pad-edge power escape: candidate generated for U3/U4")


if __name__ == "__main__":
    main()
