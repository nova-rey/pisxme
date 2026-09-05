"""Move the bridge 3V3 PG pull-up beside U4 and route it locally."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "PHASE21_RESET_TIE.kicad_pcb"
OUTPUT = ROOT / "PHASE21_RESET_PG3V3.kicad_pcb"

def main():
    board = pcbnew.LoadBoard(str(INPUT))
    net = board.FindNet("/REGULATORS/PG_BRIDGE_3V3")
    assert net is not None
    r14 = board.FindFootprintByReference("R14")
    r14.SetPosition(pcbnew.VECTOR2I_MM(220, 115))
    r14.SetOrientationDegrees(0)
    track = pcbnew.PCB_TRACK(board)
    for start, end in [((227.25, 104.75), (229.0, 104.75)),
                       ((229.0, 104.75), (229.0, 115.0)),
                       ((229.0, 115.0), (220.5, 115.0))]:
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
