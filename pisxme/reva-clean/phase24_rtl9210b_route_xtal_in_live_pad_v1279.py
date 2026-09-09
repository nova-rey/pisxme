"""V1279: route RTL9210B XTAL_IN from the live U1.53 pad to Y1.1."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_RSET_LIVE_PAD_V1278.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb"
F = pcbnew.F_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def track(board, net, points):
    for a, z in zip(points, points[1:]):
        q = pcbnew.PCB_TRACK(board)
        q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F)
        q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode())
        board.Add(q)

b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("XTAL_IN")

# Remove only the stale donor geometry for this net.  All new segments start
# and terminate on the native U1.53/Y1.1 pads below.
for q in list(b.GetTracks()):
    if q.GetNetname() == "XTAL_IN":
        b.RemoveNative(q)

track(b, n, [
    (94.05, 67.20),
    (93.40, 67.20),
    (92.80, 66.80),
    (91.00, 66.80),
    (91.00, 57.00),
    (78.00, 57.00),
    (78.00, 59.00),
])

b.BuildListOfNets()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
