"""Disposable protected-12V plane test on the validated J1 field bus."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_J1_PROTECTED_BUS_V2.kicad_pcb"
OUT = ROOT / "PHASE24_J1_PROTECTED_PLANE.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("12V_PROTECTED")
if n is None:
    raise RuntimeError("missing 12V_PROTECTED")


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


z = pcbnew.ZONE(b)
z.SetLayer(pcbnew.In3_Cu)
z.SetNet(n)
z.SetNetCode(n.GetNetCode())
z.SetIsRuleArea(False)
z.SetMinThickness(pcbnew.FromMM(0.25))
z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL)
z.SetZoneName("REV_A_PROTECTED_12V_DISTRIBUTION")
poly = pcbnew.VECTOR_VECTOR2I()
for xy in ((1, 1), (299, 1), (299, 179), (1, 179)):
    poly.append(p(*xy))
z.AddPolygon(poly)
b.Add(z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
