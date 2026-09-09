"""V1280: route RTL9210B XTAL_OUT from the live U1.54 pad to Y1.2."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_XTAL_OUT_LIVE_PAD_V1280.kicad_pcb"
F = pcbnew.F_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def route(board, net, points, layer=F):
    for a, z in zip(points, points[1:]):
        q = pcbnew.PCB_TRACK(board)
        q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
        q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode())
        board.Add(q)

def via(board, net, point):
    q = pcbnew.PCB_VIA(board)
    q.SetPosition(P(*point)); q.SetWidth(pcbnew.FromMM(0.60))
    q.SetDrill(pcbnew.FromMM(0.30)); q.SetNet(net); q.SetNetCode(net.GetNetCode())
    board.Add(q)

b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("XTAL_OUT")
for q in list(b.GetTracks()):
    if q.GetNetname() == "XTAL_OUT":
        b.RemoveNative(q)

route(b, n, [
    (94.05, 67.60),
    (93.00, 67.60),
    (92.90, 67.60),
])
via(b, n, (92.90, 67.60))
route(b, n, [
    (92.90, 67.60),
    (92.90, 69.50),
    (86.00, 69.50),
    (86.00, 55.00),
    (79.40, 55.00),
], pcbnew.B_Cu)
via(b, n, (79.40, 55.00))
route(b, n, [
    (79.40, 55.00),
    (79.40, 59.00),
])

b.BuildListOfNets()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
