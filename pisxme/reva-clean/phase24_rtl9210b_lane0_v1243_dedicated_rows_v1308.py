"""V1308: co-author lane-0 with the accepted V1243 support/reference field.

This is a disposable native-board experiment.  Lane source escapes leave the
lower QFN edge on separated F.Cu corridors, transition below the support
field, and use dedicated B.Cu outer rows before independent J1 launches.
"""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_RAILS_REFCLK_FIXED_V1243.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_LANE0_DEDICATED_ROWS_V1308.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def add(b, n, layer, points):
    for a, z in zip(points, points[1:]):
        q = pcbnew.PCB_TRACK(b)
        q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
        q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

def via(b, n, xy):
    q = pcbnew.PCB_VIA(b)
    q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(0.60))
    q.SetDrill(pcbnew.FromMM(0.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode())
    b.Add(q)

b = pcbnew.LoadBoard(str(BASE))
u, j = b.FindFootprintByReference("U1"), b.FindFootprintByReference("J1")

# Source escapes are intentionally separated from the V1243 lower support
# departures.  Their lower transitions are below the local QFN field.
routes = [
    ("LANE0_RXP", "64", (89.0, 82.0), (132.0, 42.0), "43"),
    ("LANE0_RXN", "65", (90.5, 83.5), (133.0, 44.0), "41"),
    ("LANE0_TXN", "67", (92.0, 85.0), (134.0, 46.0), "47"),
    ("LANE0_TXP", "68", (93.5, 86.5), (135.0, 48.0), "49"),
]
for name, padnum, source_via, outer, jpad in routes:
    n = b.FindNet(name)
    p = u.FindPadByNumber(padnum).GetPosition()
    src = (pcbnew.ToMM(p.x), pcbnew.ToMM(p.y))
    # Use a short orthogonal F.Cu departure, then a dedicated B.Cu row.
    add(b, n, F, [src, (source_via[0], src[1]), source_via])
    via(b, n, source_via)
    add(b, n, B, [source_via, (outer[0], source_via[1]), outer])
    via(b, n, outer)
    d = j.FindPadByNumber(jpad).GetPosition()
    dst = (pcbnew.ToMM(d.x), pcbnew.ToMM(d.y))
    add(b, n, F, [outer, (outer[0], dst[1]), dst])

b.BuildListOfNets()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
