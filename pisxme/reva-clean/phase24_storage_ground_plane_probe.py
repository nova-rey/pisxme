"""Disposable F.Cu storage ground-access zone probe; no source nets change."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb')); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
n=b.FindNet('POWER_GND'); z=pcbnew.ZONE(b); z.SetLayer(pcbnew.F_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL); z.SetLocalClearance(pcbnew.FromMM(.25)); z.SetMinThickness(pcbnew.FromMM(.20))
poly=pcbnew.SHAPE_POLY_SET(); c=pcbnew.SHAPE_LINE_CHAIN()
for q in [(85,105),(190,105),(190,155),(85,155)]: c.Append(P(*q))
c.SetClosed(True); poly.AddOutline(c); z.SetOutline(poly); b.Add(z); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones())
out=R/'PHASE24_STORAGE_J8_V5_GROUND_ZONE_V1.kicad_pcb'; b.Save(str(out)); print(out)
