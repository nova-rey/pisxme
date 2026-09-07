"""V204: move C1 below the crystal row to clear Y1/C2/SPICLK."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SPI_SOURCE_FIELD_V202.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPI_SOURCE_FIELD_V204.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu


def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


def tr(board, net, layer, a, z):
    item = pcbnew.PCB_TRACK(board); item.SetStart(P(*a)); item.SetEnd(P(*z)); item.SetLayer(layer)
    item.SetWidth(pcbnew.FromMM(0.20)); item.SetNet(net); item.SetNetCode(net.GetNetCode()); board.Add(item)


def via(board, net, xy):
    item = pcbnew.PCB_VIA(board); item.SetPosition(P(*xy)); item.SetWidth(pcbnew.FromMM(0.60)); item.SetDrill(pcbnew.FromMM(0.30)); item.SetLayerPair(F, B); item.SetNet(net); item.SetNetCode(net.GetNetCode()); board.Add(item)


def main():
    board = pcbnew.LoadBoard(str(BASE)); board.FindFootprintByReference("C1").SetPosition(P(90.0, 63.0))
    for item in list(board.GetTracks()):
        if item.GetNetname() == "XTAL_IN": board.RemoveNative(item)
    net = board.FindNet("XTAL_IN")
    tr(board, net, F, (95.2, 65.95), (95.2, 67.2)); tr(board, net, F, (95.2, 67.2), (94.5, 67.2)); via(board, net, (94.5, 67.2))
    tr(board, net, B, (94.5, 67.2), (89.8, 61.0)); via(board, net, (89.8, 61.0)); tr(board, net, F, (89.8, 61.0), (90.6, 63.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
