"""Regenerate the four-net RTL9210B QFN source field as one topology."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_ROTATED_SUPPORT_RELOCATION_V8.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_FOUR_NET_QFN_FIELD_V14.kicad_pcb"
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
    for name in ("SPISI", "SPICLK", "SPISO3"):
        remove_net(board, name)

    # Source-field channels are ordered in the same order as the U2 target
    # row; each exits to a distinct ordinary through-via before descending.
    routes = {
        "SPISI": ((94.05, 66.80), (93.60, 65.80), (86.60, 65.80)),
        "SPICLK": ((94.05, 67.20), (93.20, 64.80), (87.80, 64.80)),
        "SPISO3": ((94.05, 68.40), (92.40, 62.80), (89.00, 62.80)),
    }
    for name, (src, transition, target_x) in routes.items():
        net = board.FindNet(name)
        t(board, net, F, src, transition); v(board, net, transition)
        t(board, net, B, transition, (target_x[0], transition[1]))
        t(board, net, B, (target_x[0], transition[1]), (target_x[0], 78.00))
        v(board, net, (target_x[0], 78.00))
        t(board, net, F, (target_x[0], 78.00), (target_x[0], 80.00))

    pwr = board.FindNet("RTL_3V3")
    branches = [((94.05, 67.60), (92.80, 63.80)),
                ((94.05, 73.20), (93.20, 74.20)),
                ((96.40, 73.95), (96.40, 74.80)),
                ((101.95, 73.20), (102.80, 73.20))]
    for src, edge in branches:
        t(board, pwr, F, src, edge); v(board, pwr, edge)
    t(board, pwr, B, (92.80, 63.80), (92.80, 61.50))
    t(board, pwr, B, (93.20, 74.20), (93.20, 61.50))
    t(board, pwr, B, (96.40, 74.80), (96.40, 61.50))
    t(board, pwr, B, (102.80, 73.20), (102.80, 61.50))
    t(board, pwr, B, (92.80, 61.50), (109.60, 61.50))
    t(board, pwr, B, (109.60, 61.50), (109.60, 68.50))
    v(board, pwr, (109.60, 68.50))
    t(board, pwr, F, (109.60, 68.50), (110.40, 69.00))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
