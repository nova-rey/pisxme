"""Native RTL_5V V137 audit and trace-removal negative control."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
PCB = ROOT / "PHASE24_RTL9210B_RTL5V_BELOW_C5_V137.kicad_pcb"
EXPECTED = {("C5", "1"), ("U1", "17"), ("U1", "33")}

def connected(board):
    board.BuildConnectivity()
    pad = board.FindFootprintByReference("C5").FindPadByNumber("1")
    return {(item.GetParentFootprint().GetReference(), item.GetNumber())
            for item in board.GetConnectivity().GetConnectedItems(pad)
            if type(item).__name__ == "PAD"}

def main():
    board = pcbnew.LoadBoard(str(PCB))
    if EXPECTED - connected(board):
        raise AssertionError(f"RTL_5V missing {sorted(EXPECTED - connected(board))}")
    negative = pcbnew.LoadBoard(str(PCB))
    removed = 0
    for item in list(negative.GetTracks()):
        if item.GetNetname() == "RTL_5V":
            negative.RemoveNative(item)
            removed += 1
    if not removed:
        raise AssertionError("negative control found no RTL_5V route")
    if not EXPECTED - connected(negative):
        raise AssertionError("negative control unexpectedly passed")
    print("PASS V137 native RTL_5V audit and negative control")

if __name__ == "__main__":
    main()
