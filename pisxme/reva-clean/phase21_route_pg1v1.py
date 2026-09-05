"""Move the bridge 1V1 PG pull-up beside U5 and route it locally."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "PHASE21_RESET_PG3V3.kicad_pcb"
OUTPUT = ROOT / "PHASE21_RESET_PG3V3_PG1V1.kicad_pcb"

def main():
    board = pcbnew.LoadBoard(str(INPUT))
    net = board.FindNet("/REGULATORS/PG_BRIDGE_1V1")
    assert net is not None
    r22 = board.FindFootprintByReference("R22")
    r22.SetPosition(pcbnew.VECTOR2I_MM(240, 115))
    r22.SetOrientationDegrees(0)
    for start, end in [((237.25, 104.75), (238.5, 104.75)),
                       ((238.5, 104.75), (238.5, 113.0)),
                       ((238.5, 113.0), (241.5, 113.0)),
                       ((241.5, 113.0), (241.5, 115.0)),
                       ((241.5, 115.0), (240.5, 115.0))]:
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
