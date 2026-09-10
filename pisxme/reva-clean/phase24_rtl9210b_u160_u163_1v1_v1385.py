"""V1385: coupled U1.60/U1.63 RTL_1V1 lower shelves on V1384."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_U125_1V1_FANOUT_V1384.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_U160_U163_1V1_V1385.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def tr(board, net, layer, points):
    for a, z in zip(points, points[1:]):
        t = pcbnew.PCB_TRACK(board)
        t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
        t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode())
        board.Add(t)
def via(board, net, point):
    v = pcbnew.PCB_VIA(board)
    v.SetPosition(P(*point)); v.SetWidth(pcbnew.FromMM(0.60))
    v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(F, B)
    v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)

board = pcbnew.LoadBoard(str(BASE))
net = board.FindNet("RTL_1V1")
assert net
# Separate departures leave the QFN field on F.Cu, then share the existing
# lower 1V1 trunk on B.Cu. No signal is placed on a plane layer.
tr(board, net, F, [(94.05, 70.0), (91.2, 70.0)])
via(board, net, (91.2, 70.0))
tr(board, net, B, [(91.2, 70.0), (91.2, 76.5), (102.0, 76.5), (102.0, 64.8)])
tr(board, net, F, [(94.05, 71.2), (90.6, 71.2)])
via(board, net, (90.6, 71.2))
tr(board, net, B, [(90.6, 71.2), (90.6, 78.0), (102.0, 78.0)])
board.BuildListOfNets()
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
