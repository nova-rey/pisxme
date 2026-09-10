"""V1353: PERST_N lower shelf between CLKREQ_N and PEDET_N."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / 'PHASE24_RTL9210B_CLKREQ_OVERPASS_V1347.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_PERST_LOWER_SHELF_V1353.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def track(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    board.Add(t)

def via(board, net, xy):
    v = pcbnew.PCB_VIA(board)
    v.SetPosition(P(*xy)); v.SetWidth(pcbnew.FromMM(0.60))
    v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(F, B)
    v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)

board = pcbnew.LoadBoard(str(BASE))
net = board.FindNet('PERST_N')
assert net is not None

# U1.14 -> lower B.Cu shelf -> F.Cu connector launch.
track(board, net, F, (100.0, 73.95), (100.0, 78.0))
track(board, net, F, (100.0, 78.0), (102.0, 78.0))
via(board, net, (102.0, 78.0))
track(board, net, B, (102.0, 78.0), (124.0, 78.0))
via(board, net, (124.0, 78.0))
track(board, net, F, (124.0, 78.0), (124.0, 70.275))
track(board, net, F, (124.0, 70.275), (136.0, 70.275))

board.BuildListOfNets()
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
