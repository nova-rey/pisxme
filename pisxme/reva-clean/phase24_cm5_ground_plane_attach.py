"""Disposable CM5-ground plane attachment from the accepted collector basis."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb"
OUT = R / "PHASE24_CM5_GROUND_PLANE_ATTACH.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("/CORE_CM5/POWER_GND")
if n is None:
    raise RuntimeError("missing CM5 ground net")
V = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))

# The lower collector is already connected to the right collector through the
# accepted same-row bridges.  This ordinary through-via is outside all pads.
v = pcbnew.PCB_VIA(b)
v.SetNet(n)
v.SetPosition(V(71.50, 113.10))
v.SetWidth(pcbnew.FromMM(0.50))
v.SetDrill(pcbnew.FromMM(0.30))
b.Add(v)

# Keep CM5 ground a distinct net.  The zone is deliberately on In1, a copper
# reference layer, and is limited to the CM5 connector neighborhood.
z = pcbnew.ZONE(b)
z.SetLayer(pcbnew.In1_Cu)
z.SetNet(n)
z.SetNetCode(n.GetNetCode())
z.SetIsRuleArea(False)
z.SetMinThickness(pcbnew.FromMM(0.20))
z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL)
z.SetZoneName("REV_A_CM5_POWER_GND_ISLAND")
poly = pcbnew.VECTOR_VECTOR2I()
for xy in ((29.0, 96.0), (73.0, 96.0), (73.0, 120.0), (29.0, 120.0)):
    poly.append(V(*xy))
z.AddPolygon(poly)
b.Add(z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
