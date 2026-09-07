"""V185: disposable RTL_3V3 U1.34-to-C3.1 rail handoff on V184."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V184.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_RTL3V3_U134_C3_V185.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)


def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


def tr(board, net, layer, a, z):
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(P(*a)); item.SetEnd(P(*z)); item.SetLayer(layer)
    item.SetWidth(W); item.SetNet(net); item.SetNetCode(net.GetNetCode())
    board.Add(item)


def via(board, net, xy):
    item = pcbnew.PCB_VIA(board); item.SetPosition(P(*xy))
    item.SetWidth(pcbnew.FromMM(0.60)); item.SetDrill(pcbnew.FromMM(0.30))
    item.SetLayerPair(F, B); item.SetNet(net); item.SetNetCode(net.GetNetCode())
    board.Add(item)


def main():
    board = pcbnew.LoadBoard(str(BASE))
    net = board.FindNet("RTL_3V3")
    # Pad-aware escape above the rotated QFN, then a B.Cu rail to C3.1.
    tr(board, net, F, (94.8, 58.05), (93.8, 56.5))
    via(board, net, (93.8, 56.5))
    tr(board, net, B, (93.8, 56.5), (110.4, 56.5))
    via(board, net, (110.4, 56.5))
    tr(board, net, F, (110.4, 56.5), (110.4, 61.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
