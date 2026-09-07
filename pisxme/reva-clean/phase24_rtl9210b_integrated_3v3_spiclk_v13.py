"""Co-authored RTL_3V3 and SPICLK QFN source escape probe."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_ROTATED_SUPPORT_RELOCATION_V8.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_INTEGRATED_3V3_SPICLK_V13.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)


def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


def t(board, net, layer, a, z):
    q = pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z))
    q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode())
    board.Add(q)


def v(board, net, q):
    x = pcbnew.PCB_VIA(board); x.SetPosition(P(*q))
    x.SetWidth(pcbnew.FromMM(0.60)); x.SetDrill(pcbnew.FromMM(0.30))
    x.SetLayerPair(F, B); x.SetNet(net); x.SetNetCode(net.GetNetCode())
    board.Add(x)


def remove_net(board, name):
    for item in list(board.GetTracks()):
        if item.GetNetname() == name:
            board.RemoveNative(item)


def main():
    board = pcbnew.LoadBoard(str(BASE))
    remove_net(board, "SPICLK")
    clk = board.FindNet("SPICLK")
    # Move SPICLK into an upper B.Cu channel, opening the U1.20 escape lane.
    t(board, clk, F, (94.05, 67.20), (93.00, 67.20))
    t(board, clk, F, (93.00, 67.20), (92.80, 65.00))
    v(board, clk, (92.80, 65.00))
    t(board, clk, B, (92.80, 65.00), (87.80, 65.00))
    t(board, clk, B, (87.80, 65.00), (87.80, 78.00))
    v(board, clk, (87.80, 78.00))
    t(board, clk, F, (87.80, 78.00), (87.80, 80.00))

    pwr = board.FindNet("RTL_3V3")
    branches = [((94.05, 67.60), (93.20, 67.60)),
                ((94.05, 73.20), (93.20, 73.20)),
                ((96.40, 73.95), (96.40, 74.80)),
                ((101.95, 73.20), (102.80, 73.20))]
    for src, edge in branches:
        t(board, pwr, F, src, edge); v(board, pwr, edge)
    t(board, pwr, B, (93.20, 67.60), (93.20, 64.20))
    t(board, pwr, B, (93.20, 73.20), (93.20, 64.20))
    t(board, pwr, B, (96.40, 74.80), (96.40, 64.20))
    t(board, pwr, B, (102.80, 73.20), (102.80, 64.20))
    t(board, pwr, B, (93.20, 64.20), (109.60, 64.20))
    t(board, pwr, B, (109.60, 64.20), (109.60, 68.50))
    v(board, pwr, (109.60, 68.50))
    t(board, pwr, F, (109.60, 68.50), (110.40, 69.00))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
