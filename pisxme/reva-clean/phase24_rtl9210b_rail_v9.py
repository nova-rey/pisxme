"""Disposable RTL_5V rail completion probe from the V8 support baseline."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_ROTATED_SUPPORT_RELOCATION_V8.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_RTL5V_RAIL_V9.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)


def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def track(board, net, layer, a, z):
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(P(*a)); item.SetEnd(P(*z)); item.SetLayer(layer)
    item.SetWidth(W); item.SetNet(net); item.SetNetCode(net.GetNetCode())
    board.Add(item)


def via(board, net, q):
    item = pcbnew.PCB_VIA(board)
    item.SetPosition(P(*q)); item.SetWidth(pcbnew.FromMM(0.60))
    item.SetDrill(pcbnew.FromMM(0.30)); item.SetLayerPair(F, B)
    item.SetNet(net); item.SetNetCode(net.GetNetCode()); board.Add(item)


def main():
    board = pcbnew.LoadBoard(str(BASE)); net = board.FindNet("RTL_5V")
    # Two U1 source pads join a bottom-side trunk; C5 is launched through a
    # second ordinary via outside its pad, with no via-in-pad.
    branches = [((94.80, 66.05), (93.80, 66.05)),
                ((94.05, 72.80), (93.20, 72.80))]
    for src, edge in branches:
        track(board, net, F, src, edge); via(board, net, edge)
    track(board, net, B, (93.80, 66.05), (93.80, 74.80))
    track(board, net, B, (93.20, 72.80), (93.80, 72.80))
    track(board, net, B, (93.80, 74.80), (115.60, 74.80))
    track(board, net, B, (115.60, 74.80), (115.60, 68.50))
    via(board, net, (115.60, 68.50))
    track(board, net, F, (115.60, 68.50), (116.40, 69.00))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__":
    main()
