"""Promote reviewed JMS583 local power copper onto the corrected parent."""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
base = R / os.environ.get("P24_ZONE_BASE", "PHASE24_STORAGE_AUTHORITY_CORRECTED_SUPPORT_ALIGNED.kicad_pcb")
out = R / os.environ.get("P24_ZONE_OUT", "PHASE24_STORAGE_AUTHORITY_CORRECTED_SUPPORT_ZONES.kicad_pcb")
F = pcbnew.F_Cu
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
b = pcbnew.LoadBoard(str(base))
if b is None: raise SystemExit("target board load failed")
specs = {
    "JMS_VCCO": [(129.4,113.8),(136.8,113.8),(136.8,134.4),(129.4,134.4)],
    "JMS_VDDREG_5V": [(135.9,124.6),(137.5,124.6),(137.5,132.3),(135.9,132.3)],
    "JMS_AVDDL": [(141.3,138.0),(142.4,138.0),(142.4,113.9),(136.7,113.9),(136.7,115.1),(141.3,115.1)],
}
for name, points in specs.items():
    n = b.FindNet(name)
    z = pcbnew.ZONE(b); z.SetLayer(F); z.SetNet(n); z.SetNetCode(n.GetNetCode())
    z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL); z.SetLocalClearance(pcbnew.FromMM(.20)); z.SetMinThickness(pcbnew.FromMM(.20))
    poly = pcbnew.VECTOR_VECTOR2I()
    for point in points: poly.append(P(*point))
    z.AddPolygon(poly); b.Add(z)
n = b.FindNet("JMS_VCCK")
u = b.FindFootprintByReference("U11").FindPadByNumber("2")
c = b.FindFootprintByReference("C82").FindPadByNumber("1")
t = pcbnew.PCB_TRACK(b); t.SetStart(u.GetPosition()); t.SetEnd(c.GetPosition()); t.SetLayer(F); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
# Keep the AVDDL zone as the local rail acreage, but explicitly land the
# QFN-side pad and decoupler.  Their transformed locations are not both
# inside the conservative polygon after the support components are aligned.
n = b.FindNet("JMS_AVDDL")
u = b.FindFootprintByReference("U11").FindPadByNumber("20")
c = b.FindFootprintByReference("C83").FindPadByNumber("1")
t = pcbnew.PCB_TRACK(b); t.SetStart(u.GetPosition()); t.SetEnd(c.GetPosition()); t.SetLayer(F); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(out)); print(out)
