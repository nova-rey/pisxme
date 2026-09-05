"""Move the CM5 5V PG pull-up beside U3 and route it locally."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "PHASE21_RESET_PG3V3_PG1V1.kicad_pcb"
OUTPUT = ROOT / "PHASE21_RESET_PG3V3_PG1V1_PGCM5.kicad_pcb"

def main():
    board = pcbnew.LoadBoard(str(INPUT))
    net = board.FindNet("/REGULATORS/PG_CM5_5V")
    assert net is not None
    r6 = board.FindFootprintByReference("R6")
    r6.SetPosition(pcbnew.VECTOR2I_MM(68, 160))
    r6.SetOrientationDegrees(180)
    for start, end in [((62.25, 164.75), (64.0, 164.75)),
                       ((64.0, 164.75), (64.0, 160.0)),
                       ((64.0, 160.0), (67.5, 160.0))]:
        track = pcbnew.PCB_TRACK(board)
        track.SetStart(pcbnew.VECTOR2I_MM(*start))
        track.SetEnd(pcbnew.VECTOR2I_MM(*end))
        track.SetWidth(pcbnew.FromMM(0.20))
        track.SetLayer(pcbnew.F_Cu)
        track.SetNet(net)
        board.Add(track)
    board.Save(str(OUTPUT))
    print(OUTPUT)

if __name__ == "__main__":
    main()
