"""Measure the native Phase 15 candidate against the TI layout checklist."""
from pathlib import Path
import math
import pcbnew

ROOT = Path(__file__).resolve().parents[2]
BOARD = ROOT / "ACREAGE_U5_VOUT_PHASE15.kicad_pcb"
RAILS = {
    "U3": ("/REGULATORS/CM5_5V", ("C7", "C8")),
    "U4": ("/REGULATORS/BRIDGE_3V3", ("C16", "C17", "C19")),
    "U5": ("/REGULATORS/BRIDGE_1V1", tuple(f"C{i}" for i in range(26, 42))),
}


def distance(a, b):
    return math.hypot(pcbnew.ToMM(a.x - b.x), pcbnew.ToMM(a.y - b.y))


def main():
    board = pcbnew.LoadBoard(str(BOARD))
    for regulator, (net, refs) in RAILS.items():
        center = board.FindFootprintByReference(regulator).GetPosition()
        points = []
        for ref in refs:
            footprint = board.FindFootprintByReference(ref)
            assert footprint is not None, ref
            assert any(p.GetNetname() == net for p in footprint.Pads()), ref
            assert any(p.GetNetname() == "POWER_GND" for p in footprint.Pads()), ref
            points.append(footprint.GetPosition())
        max_distance = max(distance(center, point) for point in points)
        print(f"{regulator}: {len(refs)} COUT parts; max center distance {max_distance:.1f} mm")
    for net, minimum in (("/REGULATORS/BRIDGE_1V1", 18),):
        count = sum(x.GetNetname() == net and x.Type() == pcbnew.PCB_VIA_T
                    for x in board.GetTracks())
        assert count >= minimum, (net, count)
    print("Phase 15 native overlay measurement: PASS; rail assignments and via minima verified")


if __name__ == "__main__":
    main()
