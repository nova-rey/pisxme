"""V1137: rehome the QFN XTAL_OUT source escape and its 1V1 branch."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_XTAL_SOURCE_ESCAPE_REHOME_V1137.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(item, which):
    p = getattr(item, which)()
    return round(p.x / 1e6, 4), round(p.y / 1e6, 4)
def tr(board, net, layer, points):
    for a, z in zip(points, points[1:]):
        q = pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z))
        q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
def via(board, net, point):
    q = pcbnew.PCB_VIA(board); q.SetPosition(P(*point)); q.SetWidth(pcbnew.FromMM(.6))
    q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(F, B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)

b = pcbnew.LoadBoard(str(BASE))
# Remove only the old U1.55 left-hand departure and its shared branch.
onev1 = b.FindNet("RTL_1V1")
items = list(b.TracksInNet(onev1.GetNetCode()))
for item in items:
    if item.GetNetname() != "RTL_1V1": continue
    a, z = xy(item, "GetStart"), xy(item, "GetEnd")
    if (a, z) in [((94.05, 68.0), (92.8, 68.0)), ((92.8, 68.0), (92.8, 69.3)), ((92.8, 69.3), (92.8, 75.0))] or (a == (92.8, 69.3) and z == (92.8, 69.3)):
        b.Remove(item)
# Rehome Y1/C1/C2 as a coherent pocket; R1 stays in place as an independent RSET island.
for ref, pos in {"Y1": (10.7, 25.0), "C1": (13.6, 28.0), "C2": (10.6, 28.0)}.items():
    f = next(f for f in b.GetFootprints() if f.GetReference() == ref); f.SetPosition(P(*pos))
ni, no = b.FindNet("XTAL_IN"), b.FindNet("XTAL_OUT")
# U1.55 now exits right on a clean, ordinary-via return to the retained 1V1 collector.
tr(b, onev1, F, [(94.05, 68.0), (95.0, 68.0)]); via(b, onev1, (95.0, 68.0))
tr(b, onev1, B, [(95.0, 68.0), (95.0, 75.0), (102.5, 75.0)])
# Upper and lower QFN departures use distinct F.Cu source corridors.
tr(b, ni, F, [(94.05, 67.2), (93.4, 66.4), (91.5, 66.0)]); via(b, ni, (91.5, 66.0))
tr(b, ni, B, [(91.5, 66.0), (80.0, 66.0), (80.0, 80.0)]); via(b, ni, (80.0, 80.0))
tr(b, ni, F, [(80.0, 80.0), (80.0, 83.0)])
tr(b, no, F, [(94.05, 67.6), (93.4, 68.4), (91.5, 69.5)]); via(b, no, (91.5, 69.5))
tr(b, no, B, [(91.5, 69.5), (83.0, 69.5), (83.0, 83.0)]); via(b, no, (83.0, 83.0))
tr(b, no, F, [(83.0, 83.0), (83.0, 80.0), (81.4, 80.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
