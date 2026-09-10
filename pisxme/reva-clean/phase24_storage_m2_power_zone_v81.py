"""Disposable storage-rail plane trial on the V79 authoritative-net parent."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER.kicad_pcb"
OUT = R / "PHASE24_STORAGE_M2_POWER_ZONE_V81.kicad_pcb"
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))

b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("STORAGE_3V3")
assert n
z = pcbnew.ZONE(b)
z.SetLayer(pcbnew.F_Cu)
z.SetNet(n)
z.SetNetCode(n.GetNetCode())
z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL)
z.SetLocalClearance(pcbnew.FromMM(0.20))
z.SetMinThickness(pcbnew.FromMM(0.20))
poly = pcbnew.VECTOR_VECTOR2I()
for xy in ((120,128),(190,128),(190,150),(235,150),(235,175),(205,175),(205,145),(120,145)):
    poly.append(P(*xy))
z.AddPolygon(poly)
b.Add(z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
