"""Saved native connectivity audit and negative control for V186."""
from pathlib import Path
import tempfile
import pcbnew

HERE = Path(__file__).resolve().parent
PCB = HERE / "PHASE24_RTL9210B_RTL3V3_U134_PAD20_V186.kicad_pcb"
EXPECTED = {("U1", "20"), ("U1", "34"), ("C3", "1")}


def pads(board, ref, number):
    board.BuildConnectivity()
    pad = board.FindFootprintByReference(ref).FindPadByNumber(number)
    return {(x.GetParentFootprint().GetReference(), x.GetNumber())
            for x in board.GetConnectivity().GetConnectedItems(pad)
            if type(x).__name__ == "PAD"}


def main():
    board = pcbnew.LoadBoard(str(PCB))
    assert EXPECTED <= pads(board, "U1", "20"), pads(board, "U1", "20")
    bad = pcbnew.LoadBoard(str(PCB))
    victim = next(x for x in bad.GetTracks()
                  if type(x).__name__ == "PCB_TRACK" and x.GetNetname() == "RTL_3V3"
                  and abs(float(x.GetStart().x - x.GetEnd().x)) < 100000)
    bad.RemoveNative(victim)
    with tempfile.NamedTemporaryFile(suffix=".kicad_pcb") as handle:
        bad.Save(handle.name)
        broken = pcbnew.LoadBoard(handle.name)
        assert not EXPECTED <= pads(broken, "U1", "20")
    print("V186 native U1.20/U1.34/C3.1 connectivity PASS; trace-removal negative control PASS")


if __name__ == "__main__": main()
