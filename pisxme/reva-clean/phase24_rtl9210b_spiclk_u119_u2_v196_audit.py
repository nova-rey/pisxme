"""Saved native connectivity audit and negative control for V196."""
from pathlib import Path
import tempfile
import pcbnew

HERE = Path(__file__).resolve().parent
PCB = HERE / "PHASE24_RTL9210B_SPICLK_U119_U2_V196.kicad_pcb"


def pads(board, ref, number):
    board.BuildConnectivity()
    pad = board.FindFootprintByReference(ref).FindPadByNumber(number)
    return {(x.GetParentFootprint().GetReference(), x.GetNumber())
            for x in board.GetConnectivity().GetConnectedItems(pad)
            if type(x).__name__ == "PAD"}


def main():
    board = pcbnew.LoadBoard(str(PCB))
    assert {("U1", "19"), ("U2", "6")} <= pads(board, "U1", "19")
    bad = pcbnew.LoadBoard(str(PCB))
    victim = next(x for x in bad.GetTracks()
                  if type(x).__name__ == "PCB_TRACK" and x.GetNetname() == "SPICLK")
    bad.RemoveNative(victim)
    with tempfile.NamedTemporaryFile(suffix=".kicad_pcb") as handle:
        bad.Save(handle.name)
        broken = pcbnew.LoadBoard(handle.name)
        assert not {("U1", "19"), ("U2", "6")} <= pads(broken, "U1", "19")
    print("V196 native U1.19/U2.6 SPICLK connectivity PASS; trace-removal negative control PASS")


if __name__ == "__main__": main()
