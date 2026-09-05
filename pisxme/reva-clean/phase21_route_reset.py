"""Route the duplicate U7 bridge-reset pads locally for Phase 21."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "PHASE20_SERVICE_RD_OUTER_REFILLED.kicad_pcb"
OUTPUT = ROOT / "PHASE21_RESET_TIE.kicad_pcb"

def main():
    board = pcbnew.LoadBoard(str(INPUT))
    net = board.FindNet("/STORAGE/BRIDGE_RESET")
    assert net is not None
    for start, end in [((124.5, 144.0), (123.5, 144.0)),
                       ((123.5, 144.0), (123.5, 143.0)),
                       ((123.5, 143.0), (124.5, 143.0))]:
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
