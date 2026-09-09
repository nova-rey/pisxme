"""V1139: regenerate the complete QFN crystal/rail source field together."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_QFN_FIELD_REGENERATE_V1139.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return p.x / 1e6, p.y / 1e6
def tr(board, code, layer, points):
    for a, z in zip(points, points[1:]):
        q = pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
        q.SetWidth(W); q.SetNetCode(code); board.Add(q)
def via(board, code, x, y):
    q = pcbnew.PCB_VIA(board); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNetCode(code); board.Add(q)

b = pcbnew.LoadBoard(str(BASE))
names = ("RTL_3V3", "RTL_1V1", "RSET", "GND", "XTAL_IN", "XTAL_OUT")
codes = {name: b.FindNet(name).GetNetCode() for name in names}
# Clear only tracks/vias wholly inside the QFN source-field window.
for item in list(b.GetTracks()):
    if item.GetNetCode() not in codes.values(): continue
    if hasattr(item, "GetX"):
        x, y = item.GetX()/1e6, item.GetY()/1e6
        local = 90 <= x <= 96 and 64 <= y <= 76
    else:
        a, z = xy(item.GetStart()), xy(item.GetEnd())
        local = all(90 <= x <= 96 and 64 <= y <= 76 for x,y in (a,z))
    if local: b.Remove(item)

v3, v1, rs, gn, ni, no = (codes[n] for n in names)
# Independent source departures and ordinary through-via transitions.
tr(b, v3, F, [(94.05,66.8),(93.4,66.8),(93.4,65.0)]); via(b,v3,93.4,65.0)
tr(b, v3, B, [(93.4,65.0),(100.5,65.0),(100.5,64.0)])
tr(b, v1, F, [(94.05,68.0),(95.0,68.0)]); via(b,v1,95.0,68.0)
tr(b, v1, B, [(95.0,68.0),(95.0,75.0),(102.5,75.0)])
tr(b, rs, F, [(94.8,66.05),(94.0,64.8),(88.0,64.8),(88.0,65.0)])
tr(b, ni, F, [(94.05,67.2),(93.5,67.2),(93.0,66.6),(91.5,66.0)]); via(b,ni,91.5,66.0)
tr(b, ni, B, [(91.5,66.0),(85.5,66.0),(85.5,62.0)]); via(b,ni,85.5,62.0)
tr(b, ni, F, [(85.5,62.0),(88.0,62.0),(88.0,59.0)])
tr(b, no, F, [(94.05,67.6),(93.5,67.6),(93.0,68.4),(91.5,69.5)]); via(b,no,91.5,69.5)
tr(b, no, B, [(91.5,69.5),(85.5,69.5),(85.5,77.0),(85.5,59.5)]); via(b,no,85.5,59.5)
tr(b, no, F, [(85.5,59.5),(89.4,59.5),(89.4,59.0)])
tr(b, no, F, [(89.4,59.0),(89.4,60.0),(91.0,62.0)])
tr(b, gn, F, [(97.2,66.05),(98.0,70.0)]); tr(b, gn, F, [(94.05,72.4),(98.0,70.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
