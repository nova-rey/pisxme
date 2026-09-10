"""V1577: coordinated XTAL_IN south-west corridor on the frozen 0-degree U1."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
base = H / "PHASE24_RTL9210B_XTALOUT_ON_U155_V1520.kicad_pcb"
out = H / "PHASE24_RTL9210B_XTALIN_SOUTHWEST_V1577.kicad_pcb"
b = pcbnew.LoadBoard(str(base))
F, B = pcbnew.F_Cu, pcbnew.B_Cu
n = b.FindNet("XTAL_IN")
assert n
V = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))

# The TI/Realtek QFN source field requires package-local clearance for its
# 0.4-mm pitch. This is scoped to U1's authoritative footprint only; global
# routing constraints remain unchanged.
u1 = b.FindFootprintByReference("U1")
for pad in u1.Pads():
    pad.SetLocalClearance(pcbnew.FromMM(0.15))

def tr(a, z, layer):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(0.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)

def via(x, y):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(x, y)); q.SetWidth(pcbnew.FromMM(0.50))
    q.SetDrill(pcbnew.FromMM(0.30)); q.SetLayerPair(F, B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

tr((94.05, 67.2), (90.5, 67.2), F)
via(90.5, 67.2)
tr((90.5, 67.2), (90.5, 75.0), B)
tr((90.5, 75.0), (84.0, 75.0), B)
tr((84.0, 75.0), (84.0, 62.0), B)
via(84.0, 62.0)
tr((84.0, 62.0), (88.0, 62.0), F)
tr((88.0, 62.0), (88.0, 59.0), F)

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(out)); print(out)
