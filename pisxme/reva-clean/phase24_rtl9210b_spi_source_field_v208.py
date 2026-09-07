"""V208: complete the lower-offset XTAL_IN branch to Y1.1."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SPI_SOURCE_FIELD_V207.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPI_SOURCE_FIELD_V208.kicad_pcb"


def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


def main():
    board = pcbnew.LoadBoard(str(BASE)); net = board.FindNet("XTAL_IN")
    item = pcbnew.PCB_TRACK(board); item.SetStart(P(89.8, 61.0)); item.SetEnd(P(89.3, 60.0)); item.SetLayer(pcbnew.F_Cu); item.SetWidth(pcbnew.FromMM(0.20)); item.SetNet(net); item.SetNetCode(net.GetNetCode()); board.Add(item)
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
