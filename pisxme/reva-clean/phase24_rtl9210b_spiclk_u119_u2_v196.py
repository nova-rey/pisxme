"""V196: keep V193 XTAL_IN and dogleg SPICLK around its transition via."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SPISO_U123_U2_V193.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPICLK_U119_U2_V196.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu


def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


def tr(board, net, layer, a, z):
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(P(*a)); item.SetEnd(P(*z)); item.SetLayer(layer)
    item.SetWidth(pcbnew.FromMM(0.20)); item.SetNet(net)
    item.SetNetCode(net.GetNetCode()); board.Add(item)


def via(board, net, xy):
    item = pcbnew.PCB_VIA(board); item.SetPosition(P(*xy))
    item.SetWidth(pcbnew.FromMM(0.60)); item.SetDrill(pcbnew.FromMM(0.30))
    item.SetLayerPair(F, B); item.SetNet(net); item.SetNetCode(net.GetNetCode())
    board.Add(item)


def main():
    board = pcbnew.LoadBoard(str(BASE))
    net = board.FindNet("SPICLK")
    tr(board, net, F, (100.8, 58.05), (100.8, 57.2))
    tr(board, net, F, (100.8, 57.2), (101.4, 57.2))
    tr(board, net, F, (101.4, 57.2), (101.4, 50.0))
    via(board, net, (101.4, 50.0))
    tr(board, net, B, (101.4, 50.0), (87.8, 50.0))
    via(board, net, (87.8, 50.0))
    tr(board, net, F, (87.8, 50.0), (87.8, 58.5))
    tr(board, net, F, (87.8, 58.5), (90.6, 59.5))
    tr(board, net, F, (90.6, 59.5), (90.6, 64.0))
    tr(board, net, F, (90.6, 64.0), (87.8, 65.0))
    tr(board, net, F, (87.8, 65.0), (87.8, 72.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
