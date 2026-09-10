"""V1482: center the ordinary GND via in the narrow launch pocket."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_GND_IN1_RETURN_V1482.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE))
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('GND'); assert n
v=pcbnew.PCB_VIA(b); v.SetPosition(V(101.3,69.2)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
t=pcbnew.PCB_TRACK(b); t.SetStart(V(100.4,69.2)); t.SetEnd(V(101.3,69.2)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.In1_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetIsRuleArea(False); z.SetMinThickness(pcbnew.FromMM(.20)); z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL); z.SetZoneName('RTL9210B_GND_RETURN_FIELD')
poly=pcbnew.VECTOR_VECTOR2I()
for xy in ((100.7,68.8),(116.0,68.8),(116.0,78.4),(100.7,78.4)): poly.append(V(*xy))
z.AddPolygon(poly); b.Add(z); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
