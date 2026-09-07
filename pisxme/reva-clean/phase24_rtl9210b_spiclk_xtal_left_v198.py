"""V198: left-side XTAL_IN transition with straight SPICLK landing."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SPISO_U123_U2_V193.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPICLK_XTAL_LEFT_V198.kicad_pcb"
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


def remove_net(board, name):
    for item in list(board.GetTracks()):
        if item.GetNetname() == name: board.RemoveNative(item)


def main():
    board = pcbnew.LoadBoard(str(BASE))
    spiclk = board.FindNet("SPICLK")
    xtal = board.FindNet("XTAL_IN")
    remove_net(board, "SPICLK")
    remove_net(board, "XTAL_IN")

    tr(board, spiclk, F, (100.8, 58.05), (100.8, 57.2))
    tr(board, spiclk, F, (100.8, 57.2), (101.4, 57.2))
    tr(board, spiclk, F, (101.4, 57.2), (101.4, 50.0))
    via(board, spiclk, (101.4, 50.0))
    tr(board, spiclk, B, (101.4, 50.0), (87.8, 50.0))
    via(board, spiclk, (87.8, 50.0))
    tr(board, spiclk, F, (87.8, 50.0), (87.8, 72.0))

    tr(board, xtal, F, (95.2, 65.95), (95.2, 67.2))
    tr(board, xtal, F, (95.2, 67.2), (94.5, 67.2))
    via(board, xtal, (94.5, 67.2))
    tr(board, xtal, B, (94.5, 67.2), (86.8, 61.0))
    via(board, xtal, (86.8, 61.0))
    tr(board, xtal, F, (86.8, 61.0), (87.3, 60.0))
    tr(board, xtal, F, (87.3, 60.0), (86.1, 60.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
