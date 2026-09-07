"""V191: alternate SPISO source/destination corridors after V190 rejection."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SPICS_U124_U2_V189.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPISO_U123_U2_V191.kicad_pcb"
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
    net = board.FindNet("SPISO")
    tr(board, net, F, (99.2, 58.05), (100.2, 57.0))
    tr(board, net, F, (100.2, 57.0), (100.2, 50.5))
    via(board, net, (100.2, 50.5))
    tr(board, net, B, (100.2, 50.5), (80.0, 50.5))
    via(board, net, (80.0, 50.5))
    tr(board, net, F, (80.0, 50.5), (80.0, 69.5))
    tr(board, net, F, (80.0, 69.5), (83.0, 72.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
