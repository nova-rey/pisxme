"""V1138: offset XTAL_OUT return corridor after coordinated U1.55 rehome."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_XTALOUT_OFFSET_RETURN_V1138.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(item, which):
    p = getattr(item, which)()
    return round(p.x / 1e6, 4), round(p.y / 1e6, 4)
def tr(board, net, layer, points):
    for a, z in zip(points, points[1:]):
        q = pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
        q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
def via(board, net, point):
    q = pcbnew.PCB_VIA(board); q.SetPosition(P(*point)); q.SetWidth(pcbnew.FromMM(.6))
    q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(F, B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)

b = pcbnew.LoadBoard(str(BASE))
onev1, ni, no = b.FindNet("RTL_1V1"), b.FindNet("XTAL_IN"), b.FindNet("XTAL_OUT")
# Retain the known-clean V1119 XTAL_IN departure and move its return to y=75.
tr(b, ni, F, [(94.05,67.2),(93.5,67.2),(93.0,67.5),(91.5,68.6)]); via(b, ni, (91.5,68.6))
tr(b, ni, B, [(91.5,68.6),(91.5,75.0),(85.5,75.0),(85.5,62.0)]); via(b, ni, (85.5,62.0))
tr(b, ni, F, [(85.5,62.0),(88.0,62.0),(88.0,59.0)])
# XTAL_OUT clears the source field, then uses an independent y=77 return lane.
tr(b, no, F, [(94.05,67.6),(93.5,67.6),(93.0,68.4),(91.5,69.5)]); via(b, no, (91.5,69.5))
tr(b, no, B, [(91.5,69.5),(91.5,77.0),(85.5,77.0),(85.5,59.5)]); via(b, no, (85.5,59.5))
tr(b, no, F, [(85.5,59.5),(89.4,59.5),(89.4,59.0)])
tr(b, no, F, [(89.4,59.0),(89.4,60.0),(91.0,62.0)])

# U1.55 gets a separate right-side ordinary-via transition to the retained 1V1 collector.
tr(b, onev1, F, [(94.05,68.0),(95.0,68.0)]); via(b, onev1, (95.0,68.0))
tr(b, onev1, B, [(95.0,68.0),(95.0,75.0),(102.5,75.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
