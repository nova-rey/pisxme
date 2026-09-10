"""V53: add a bounded F.Cu POWER_GND access zone over storage acreage."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V50_U7_RXN_RIGHTDOGLEG.kicad_pcb'; OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V53_STORAGE_GND_ACCESS.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('POWER_GND'); assert n
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.F_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL); z.SetLocalClearance(pcbnew.FromMM(.25)); z.SetMinThickness(pcbnew.FromMM(.20))
c=pcbnew.SHAPE_LINE_CHAIN()
for q in [(75,105),(230,105),(230,175),(75,175)]: c.Append(P(*q))
c.SetClosed(True); poly=pcbnew.SHAPE_POLY_SET(); poly.AddOutline(c); z.SetOutline(poly); b.Add(z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
