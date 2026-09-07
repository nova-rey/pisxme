"""Native connectivity audit for the V256 RTL9210B rail experiment.

Edges are derived by KiCad from the saved pads, tracks, vias, and zones.
"""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BOARD = HERE / "PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V256.kicad_pcb"


def main():
    board = pcbnew.LoadBoard(str(BOARD))
    board.BuildConnectivity()
    connectivity = board.GetConnectivity()
    u1 = board.FindFootprintByReference("U1")
    c4 = board.FindFootprintByReference("C4").FindPadByNumber("1")
    for number in ("36", "40"):
        assert c4 in connectivity.GetConnectedItems(u1.FindPadByNumber(number))
    print("V256 native U1.36/U1.40 to C4.1 connectivity PASS")


if __name__ == "__main__":
    main()
