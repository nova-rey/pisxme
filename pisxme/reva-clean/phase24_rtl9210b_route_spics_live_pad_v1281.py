"""V1281: route RTL9210B SPICS from U1.24 to flash U2.1."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_SPICS_LIVE_PAD_V1281.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def route(board, net, layer, points):
    for a, z in zip(points, points[1:]):
        q = pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z))
        q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
def via(board, net, point):
    q = pcbnew.PCB_VIA(board); q.SetPosition(P(*point)); q.SetWidth(pcbnew.FromMM(0.60))
    q.SetDrill(pcbnew.FromMM(0.30)); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)

b = pcbnew.LoadBoard(str(BASE)); n = b.FindNet("SPICS")
for q in list(b.GetTracks()):
    if q.GetNetname() == "SPICS": b.RemoveNative(q)
route(b, n, F, [(101.95, 70.80), (103.50, 70.80)])
via(b, n, (103.50, 70.80))
route(b, n, B, [(103.50, 70.80), (103.50, 66.50), (112.00, 66.50), (112.00, 70.80)])
via(b, n, (112.00, 70.80))
route(b, n, F, [(112.00, 70.80), (112.00, 76.40), (111.40, 76.40)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
