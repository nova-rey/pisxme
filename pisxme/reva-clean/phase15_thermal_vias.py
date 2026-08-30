"""Add TI-recommended TPSM63606 thermal-via arrays to the Phase 15 base.

The source is the closed Phase 14 power candidate.  This step intentionally
adds no regulator signal copper; it establishes the package thermal/ground
geometry before the separate local VIN/VOUT loop routing is accepted.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "ACREAGE_POWER_PHASE14.kicad_pcb"
OUTPUT = ROOT / "ACREAGE_REGULATOR_PHASE15.kicad_pcb"
VIA_POSITIONS = {
    "U3": (52, 78), "U4": (225, 105), "U5": (235, 105),
}


def main():
    board = pcbnew.LoadBoard(str(INPUT))
    ground = next((n for name, n in board.GetNetsByName().items()
                   if str(name) == "/REGULATORS/POWER_GND"), None)
    if ground is None:
        raise SystemExit("missing regulator ground net")
    for ref, (cx, cy) in VIA_POSITIONS.items():
        fp = board.FindFootprintByReference(ref)
        if fp is None:
            raise SystemExit(f"missing regulator {ref}")
        # Keep the vias adjacent to, rather than on top of, the solder lands;
        # this preserves ordinary through-via assembly and a tentable mask.
        # The RDL0020 thermal lands are four narrow central PGND lands at
        # x=0 and y=-1.125/-0.375/+0.375/+1.125 mm.  Place one via in each
        # land; placing them outside this strip would overlap perimeter pads
        # and inherit those pads' unrelated net during board serialization.
        for dx, dy in ((0.0, -1.125), (0.0, -0.375),
                       (0.0, 0.375), (0.0, 1.125)):
            via = pcbnew.PCB_VIA(board)
            via.SetPosition(pcbnew.VECTOR2I_MM(cx + dx, cy + dy))
            # The board's ordinary-through-via rule is 0.5 mm diameter and
            # 0.3 mm minimum drill.  This keeps the 0.1 mm annulus while the
            # 0.5 mm finished via still fits the central PGND land.
            via.SetWidth(pcbnew.FromMM(0.50))
            via.SetDrill(pcbnew.FromMM(0.30))
            # Set the BOARD_NET object as well as the code.  KiCad's Python
            # binding can leave a newly-created track primitive associated
            # with the wrong net after serialization when only SetNetCode is
            # used on a board with hierarchical and legacy net aliases.
            via.SetNet(ground)
            via.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
            board.Add(via)
        # The four exposed PGND lands are separate copper islands in the
        # package footprint.  Join their one-via-per-land array with narrow
        # same-net F.Cu links in the intervening 0.25 mm gaps.
        for y0, y1 in ((-0.875, -0.625), (-0.125, 0.125), (0.625, 0.875)):
            link = pcbnew.PCB_TRACK(board)
            link.SetStart(pcbnew.VECTOR2I_MM(cx, cy + y0))
            link.SetEnd(pcbnew.VECTOR2I_MM(cx, cy + y1))
            link.SetWidth(pcbnew.FromMM(0.25))
            link.SetLayer(pcbnew.F_Cu)
            link.SetNet(ground)
            board.Add(link)
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    board.Save(str(OUTPUT))
    print("Phase 15 thermal base: PASS; 12 ordinary 0.50/0.30 mm PGND vias added")


if __name__ == "__main__":
    main()
