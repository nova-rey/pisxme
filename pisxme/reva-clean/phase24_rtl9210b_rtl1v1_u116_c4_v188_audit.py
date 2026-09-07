"""Saved native connectivity audit and negative control for V188."""
from pathlib import Path
import tempfile
import pcbnew

HERE = Path(__file__).resolve().parent
PCB = HERE / "PHASE24_RTL9210B_RTL1V1_U116_C4_V188.kicad_pcb"
EXPECTED = {("U1", "16"), ("C4", "1")}


def pads(board, ref, number):
    board.BuildConnectivity()
    pad = board.FindFootprintByReference(ref).FindPadByNumber(number)
    return {(x.GetParentFootprint().GetReference(), x.GetNumber())
            for x in board.GetConnectivity().GetConnectedItems(pad)
            if type(x).__name__ == "PAD"}


def main():
    board = pcbnew.LoadBoard(str(PCB))
    assert EXPECTED <= pads(board, "U1", "16"), pads(board, "U1", "16")
    bad = pcbnew.LoadBoard(str(PCB))
    victim = next(x for x in bad.GetTracks()
                  if type(x).__name__ == "PCB_TRACK" and x.GetNetname() == "RTL_1V1")
    bad.RemoveNative(victim)
    with tempfile.NamedTemporaryFile(suffix=".kicad_pcb") as handle:
        bad.Save(handle.name)
        broken = pcbnew.LoadBoard(handle.name)
        assert not EXPECTED <= pads(broken, "U1", "16")
    print("V188 native U1.16/C4.1 connectivity PASS; trace-removal negative control PASS")


if __name__ == "__main__": main()
