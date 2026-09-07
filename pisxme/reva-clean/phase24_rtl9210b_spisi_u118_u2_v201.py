"""V201: disposable SPISI U1.18-to-U2.5 right-side upper escape."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SPICLK_CRYSTAL_EAST_V200.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPISI_U118_U2_V201.kicad_pcb"
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
    net = board.FindNet("SPISI")
    tr(board, net, F, (101.2, 58.05), (101.2, 57.2))
    tr(board, net, F, (101.2, 57.2), (102.6, 57.2))
    tr(board, net, F, (102.6, 57.2), (102.6, 46.5))
    via(board, net, (102.6, 46.5))
    tr(board, net, B, (102.6, 46.5), (86.6, 46.5))
    via(board, net, (86.6, 46.5))
    tr(board, net, F, (86.6, 46.5), (86.6, 72.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
