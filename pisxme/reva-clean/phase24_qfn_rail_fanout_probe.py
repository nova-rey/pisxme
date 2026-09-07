"""Disposable probe for missing RTL9210B QFN rail pad fanout connections."""
from pathlib import Path
import pcbnew

BASE = Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V5_NO_FIXTURE_STUBS.kicad_pcb")
OUT = Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V6_QFN_RAIL_FANOUT.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def p(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def seg(board, net, layer, a, b):
    t = pcbnew.PCB_TRACK(board); t.SetStart(p(*a)); t.SetEnd(p(*b))
    t.SetLayer(layer); t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode()); board.Add(t)
def via(board, net, at):
    v = pcbnew.PCB_VIA(board); v.SetPosition(p(*at)); v.SetWidth(pcbnew.FromMM(.60))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F, B); v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)

def main():
    b = pcbnew.LoadBoard(str(BASE))
    n1, n5 = b.FindNet("RTL_1V1"), b.FindNet("RTL_5V")
    # Short F.Cu escapes to ordinary-via perimeter points, then a B.Cu local
    # collector. These are deliberately outside pads; no via-in-pad is used.
    branches = [
        ((77.2, 58.05), (77.2, 56.5)),
        ((81.2, 58.05), (80.2, 56.5)),
        ((76.05, 60.0), (74.5, 60.0)),
        ((76.05, 62.0), (74.5, 62.0)),
        ((76.05, 63.2), (74.5, 63.2)),
        ((82.8, 65.95), (82.8, 67.5)),
    ]
    for a, z in branches: seg(b, n1, F, a, z); via(b, n1, z)
    for a, z in [((74.5, 60), (74.5, 56.5)), ((74.5, 56.5), (80.2, 56.5)),
                 ((74.5, 60), (74.5, 67.5)), ((74.5, 67.5), (82.8, 67.5))]:
        seg(b, n1, B, a, z)
    seg(b, n5, F, (83.2, 65.95), (83.6, 65.95)); seg(b, n5, F, (83.6, 65.95), (83.6, 67.0))
    via(b, n5, (83.6, 67.0)); seg(b, n5, B, (83.6, 67.0), (84.5, 67.0))
    seg(b, n5, B, (84.5, 67.0), (84.5, 59.2)); seg(b, n5, B, (84.5, 59.2), (85.0, 59.2))
    via(b, n5, (85.0, 59.2))
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
