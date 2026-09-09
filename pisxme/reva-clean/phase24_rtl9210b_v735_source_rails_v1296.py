"""V1296: extend the rotated V1295 source trio with RTL_5V."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / 'PHASE24_RTL9210B_V735_SOURCE_TRIO_V1295.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_V735_SOURCE_RAILS_V1296.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def route(board, net, layer, points):
    for a, z in zip(points, points[1:]):
        t = pcbnew.PCB_TRACK(board)
        t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
        t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode())
        board.Add(t)

def via(board, net, point):
    v = pcbnew.PCB_VIA(board)
    v.SetPosition(P(*point)); v.SetWidth(pcbnew.FromMM(.60))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(net); v.SetNetCode(net.GetNetCode())
    board.Add(v)

board = pcbnew.LoadBoard(str(BASE))
net = board.FindNet('RTL_5V')
# Pad 33 is the left edge of the rotated source row.  Exit vertically into
# the open pocket, transition once, and use a dedicated upper B.Cu corridor.
route(board, net, F, [(95.2, 66.05), (95.2, 64.0)])
via(board, net, (95.2, 64.0))
route(board, net, B, [(95.2, 64.0), (95.2, 67.0), (101.5, 67.0),
                      (101.5, 63.5), (103.5, 63.5), (103.5, 65.5),
                      (126.4, 65.5), (126.4, 52.0)])
via(board, net, (126.4, 52.0))
route(board, net, F, [(126.4, 52.0), (126.4, 51.0)])
board.BuildListOfNets()
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
