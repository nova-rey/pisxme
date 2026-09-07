"""V189: disposable SPICS U1.24-to-U2.1 outer-corridor route."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_RTL1V1_U116_C4_V188.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPICS_U124_U2_V189.kicad_pcb"
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
    net = board.FindNet("SPICS")
    tr(board, net, F, (98.8, 58.05), (98.8, 52.5))
    via(board, net, (98.8, 52.5))
    tr(board, net, B, (98.8, 52.5), (81.8, 52.5))
    via(board, net, (81.8, 52.5))
    tr(board, net, F, (81.8, 52.5), (81.8, 72.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
