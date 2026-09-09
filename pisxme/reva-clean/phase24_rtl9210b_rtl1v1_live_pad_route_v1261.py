"""V1261: native-pad-driven RTL_1V1 support route on the V1258 lane base."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_J1_PAD_ALIGNED_LAUNCH_V1258.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_RTL1V1_LIVE_PAD_ROUTE_V1261.kicad_pcb"
F, B, W = pcbnew.F_Cu, pcbnew.B_Cu, pcbnew.FromMM(.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def mm(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def seg(board, net, layer, points):
    for a, z in zip(points, points[1:]):
        q = pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z))
        q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode())
        board.Add(q)
def via(board, net, point):
    q = pcbnew.PCB_VIA(board); q.SetPosition(P(*point)); q.SetWidth(pcbnew.FromMM(.60))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)

b = pcbnew.LoadBoard(str(BASE)); net = b.FindNet("RTL_1V1")
# Remove only the superseded RTL_1V1 copper; all lane/control copper remains.
for q in list(b.GetTracks()):
    if q.GetNetname() == "RTL_1V1": b.Remove(q)

# Actual V1258 pad coordinates, grouped into two clear source branches.
west = [(95.2, 66.05), (94.05, 68.0), (94.05, 70.0), (94.05, 71.2)]
east = [(100.8, 66.05), (101.95, 70.4), (100.8, 73.95)]
for p in west:
    seg(b, net, F, [p, (93.6, p[1]), (93.6, 60.0)])
for p in east:
    x = 103.0 if p[1] < 72 else 102.5
    seg(b, net, F, [p, (x, p[1]), (x, 60.0)])
# The upper collector stays on F.Cu only between the source branches.  It
# transitions before the lane field and uses a B.Cu y=50 trunk to the cap.
seg(b, net, F, [(93.6, 60.0), (103.0, 60.0)])
via(b, net, (103.0, 60.0)); seg(b, net, B, [(103.0, 60.0), (103.0, 50.0), (123.4, 50.0)])
via(b, net, (123.4, 50.0)); seg(b, net, F, [(123.4, 50.0), (123.4, 51.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
