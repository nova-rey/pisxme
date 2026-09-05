"""Co-locate the two LM74700 VCAP capacitors and route their controls."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "PHASE21_RESET_PG3V3_PG1V1_PGCM5.kicad_pcb"
OUTPUT = ROOT / "PHASE21_CONTROLS_VCAP.kicad_pcb"

def add_track(board, net, start, end):
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(pcbnew.VECTOR2I_MM(*start)); track.SetEnd(pcbnew.VECTOR2I_MM(*end))
    track.SetWidth(pcbnew.FromMM(0.20)); track.SetLayer(pcbnew.F_Cu); track.SetNet(net)
    board.Add(track)

def main():
    board = pcbnew.LoadBoard(str(INPUT))
    for ref, pos in (("C3", (15, 70)), ("C4", (15, 90))):
        fp = board.FindFootprintByReference(ref)
        fp.SetPosition(pcbnew.VECTOR2I_MM(*pos)); fp.SetOrientationDegrees(0)
    add_track(board, board.FindNet("/POWER_INPUT/VCAP_A"), (18.55, 73.55), (14.2, 70.0))
    add_track(board, board.FindNet("/POWER_INPUT/VCAP_B"), (18.55, 93.55), (14.2, 90.0))
    board.Save(str(OUTPUT)); print(OUTPUT)

if __name__ == "__main__": main()
