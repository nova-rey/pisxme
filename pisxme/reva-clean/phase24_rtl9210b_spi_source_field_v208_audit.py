"""Saved native connectivity audit and negative controls for V208."""
from pathlib import Path
import tempfile
import pcbnew

HERE = Path(__file__).resolve().parent
PCB = HERE / "PHASE24_RTL9210B_SPI_SOURCE_FIELD_V208.kicad_pcb"
EXPECT = {"RTL_3V3": (("U1", "20"), {("U1", "20"), ("U1", "34"), ("C3", "1")}), "SPICLK": (("U1", "19"), {("U1", "19"), ("U2", "6")}), "SPISI": (("U1", "18"), {("U1", "18"), ("U2", "5")}), "XTAL_IN": (("U1", "53"), {("U1", "53"), ("Y1", "1"), ("C1", "1")})}


def pads(board, ref, number):
    board.BuildConnectivity(); pad = board.FindFootprintByReference(ref).FindPadByNumber(number)
    return {(x.GetParentFootprint().GetReference(), x.GetNumber()) for x in board.GetConnectivity().GetConnectedItems(pad) if type(x).__name__ == "PAD"}


def main():
    board = pcbnew.LoadBoard(str(PCB))
    for name, ((ref, number), expected) in EXPECT.items(): assert expected <= pads(board, ref, number), name
    for name, ((ref, number), expected) in EXPECT.items():
        bad = pcbnew.LoadBoard(str(PCB))
        # XTAL_IN is intentionally branched to Y1.1 and C1.1; remove the
        # complete disposable net copper so the negative control cannot pass
        # merely by retaining the other branch.
        for victim in list(bad.GetTracks()):
            if victim.GetNetname() == name:
                bad.RemoveNative(victim)
        with tempfile.NamedTemporaryFile(suffix=".kicad_pcb") as handle:
            bad.Save(handle.name); broken = pcbnew.LoadBoard(handle.name); assert not expected <= pads(broken, ref, number), name
    print("V208 native rail/SPI/crystal connectivity PASS; four negative controls PASS")


if __name__ == "__main__": main()
