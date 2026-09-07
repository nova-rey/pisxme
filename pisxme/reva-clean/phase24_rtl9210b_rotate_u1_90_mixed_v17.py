"""Mixed-layer four-net handoff for the 90-degree U1 placement."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_ROTATE_U1_90_V15.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_ROTATE_U1_90_MIXED_V17.kicad_pcb"
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


def main():
    board = pcbnew.LoadBoard(str(BASE))
    # SPISO3 takes the independent F.Cu channel; this avoids the reversed
    # source/target ordering imposed on the two B.Cu channels.
    net = board.FindNet("SPISO3")
    t(board, net, F, (99.60, 66.05), (99.60, 61.60))
    t(board, net, F, (99.60, 61.60), (89.00, 61.60))
    t(board, net, F, (89.00, 61.60), (89.00, 80.00))

    for name, src, transition, target in [
        ("SPICLK", (100.80, 66.05), (100.80, 64.00), (87.80, 64.00)),
        ("SPISI", (101.20, 66.05), (101.20, 64.80), (86.60, 64.80)),
    ]:
        net = board.FindNet(name); t(board, net, F, src, transition)
        v(board, net, transition); t(board, net, B, transition, target)
        t(board, net, B, target, (target[0], 78.00)); v(board, net, (target[0], 78.00))
        t(board, net, F, (target[0], 78.00), (target[0], 80.00))

    # RTL_3V3 leaves its top-row source pad through a separate transition and
    # stays above the SPI channels before launching C3.
    net = board.FindNet("RTL_3V3")
    t(board, net, F, (100.40, 66.05), (100.40, 60.80)); v(board, net, (100.40, 60.80))
    t(board, net, B, (100.40, 60.80), (110.00, 60.80))
    t(board, net, B, (110.00, 60.80), (110.00, 68.50)); v(board, net, (110.00, 68.50))
    t(board, net, F, (110.00, 68.50), (110.40, 69.00))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
