"""V187: disposable RTL_5V U1.33-to-C5.1 rail handoff on V186."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_RTL3V3_U134_PAD20_V186.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_RTL5V_U133_C5_V187.kicad_pcb"
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
    net = board.FindNet("RTL_5V")
    tr(board, net, F, (95.2, 58.05), (95.2, 55.5))
    via(board, net, (95.2, 55.5))
    tr(board, net, B, (95.2, 55.5), (116.4, 55.5))
    via(board, net, (116.4, 55.5))
    tr(board, net, F, (116.4, 55.5), (116.4, 61.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
