"""Disposable RTL_3V3 local rail probe from the V8 support baseline."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_ROTATED_SUPPORT_RELOCATION_V8.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_RTL3V3_LOCAL_RAIL_V12.kicad_pcb"
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
    board = pcbnew.LoadBoard(str(BASE)); net = board.FindNet("RTL_3V3")
    # Exit the left/bottom U1 supply pads to a B.Cu trunk below the support
    # field, then launch C3 through an ordinary via. No via-in-pad is used.
    branches = [((94.05, 67.60), (93.40, 66.20)),
                ((94.05, 73.20), (93.40, 74.20)),
                ((96.40, 73.95), (96.40, 74.80)),
                ((101.95, 73.20), (102.80, 73.20))]
    for src, edge in branches:
        t(board, net, F, src, edge); v(board, net, edge)
    t(board, net, B, (93.40, 66.20), (93.40, 65.20))
    t(board, net, B, (93.40, 74.20), (93.40, 65.20))
    t(board, net, B, (96.40, 74.80), (96.40, 65.20))
    t(board, net, B, (102.80, 73.20), (102.80, 65.20))
    t(board, net, B, (93.40, 65.20), (109.60, 65.20))
    t(board, net, B, (109.60, 65.20), (109.60, 68.50))
    v(board, net, (109.60, 68.50)); t(board, net, F, (109.60, 68.50), (110.40, 69.00))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
