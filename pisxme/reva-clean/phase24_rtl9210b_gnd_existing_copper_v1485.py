"""V1485: stitch the existing QFN GND copper into the In1 return field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_GND_EXISTING_COPPER_V1485.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE))
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('GND'); assert n
# Existing GND track at x=97.2 runs to the QFN exposed-pad top boundary.
v=pcbnew.PCB_VIA(b); v.SetPosition(V(97.2,67.2)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.In1_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetIsRuleArea(False); z.SetMinThickness(pcbnew.FromMM(.20)); z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL); z.SetZoneName('RTL9210B_GND_RETURN_FIELD')
poly=pcbnew.VECTOR_VECTOR2I()
for xy in ((96.8,66.8),(116.0,66.8),(116.0,78.4),(96.8,78.4)): poly.append(V(*xy))
z.AddPolygon(poly); b.Add(z); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
