#!/usr/bin/env python3
"""Path-B disposable: connect U1 RTL_5V pad 17 below the QFN on B.Cu."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_1V1_QFN_COLLECTOR_V2.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_5V_PAD17_V2.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.2)

def V(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def seg(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    board.Add(t)

def via(board, net, x, y):
    v = pcbnew.PCB_VIA(board)
    v.SetPosition(V(x, y)); v.SetWidth(pcbnew.FromMM(0.6))
    v.SetDrill(pcbnew.FromMM(0.3)); v.SetLayerPair(F, B)
    v.SetNet(net); v.SetNetCode(net.GetNetCode())
    board.Add(v)

def main():
    board = pcbnew.LoadBoard(str(BASE))
    net = board.FindNet("RTL_5V")
    seg(board, net, F, (83.2, 65.95), (83.2, 67.0))
    via(board, net, 83.2, 67.0)
    seg(board, net, B, (83.2, 67.0), (84.5, 67.0))
    seg(board, net, B, (84.5, 67.0), (84.5, 59.2))
    seg(board, net, B, (84.5, 59.2), (85.0, 59.2))
    via(board, net, 85.0, 59.2)
    board.BuildListOfNets()
    board.Save(str(OUT))
    print(OUT)

if __name__ == "__main__":
    main()
