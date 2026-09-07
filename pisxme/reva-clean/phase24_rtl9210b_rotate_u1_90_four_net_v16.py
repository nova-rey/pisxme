"""Four-net source-field probe using the 90-degree U1 placement."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_ROTATE_U1_90_V15.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_ROTATE_U1_90_FOUR_NET_V16.kicad_pcb"
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
    # Each top-row source pad exits straight outward to its own transition.
    routes = {
        "SPISI": ((101.20, 66.05), (101.20, 64.00), (86.60, 64.00)),
        "SPICLK": ((100.80, 66.05), (100.80, 63.20), (87.80, 63.20)),
        "SPISO3": ((99.60, 66.05), (99.60, 61.60), (89.00, 61.60)),
    }
    for name, (src, transition, target) in routes.items():
        net = board.FindNet(name); t(board, net, F, src, transition)
        v(board, net, transition); t(board, net, B, transition, target)
        t(board, net, B, target, (target[0], 78.00))
        v(board, net, (target[0], 78.00)); t(board, net, F,
                                             (target[0], 78.00), (target[0], 80.00))

    pwr = board.FindNet("RTL_3V3")
    src, transition = (100.40, 66.05), (100.40, 60.80)
    t(board, pwr, F, src, transition); v(board, pwr, transition)
    t(board, pwr, B, transition, (110.00, 60.80))
    t(board, pwr, B, (110.00, 60.80), (110.00, 68.50))
    v(board, pwr, (110.00, 68.50)); t(board, pwr, F,
                                      (110.00, 68.50), (110.40, 69.00))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
