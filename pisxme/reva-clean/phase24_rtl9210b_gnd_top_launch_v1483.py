"""V1483: upper-right In1-field launch, outside the exposed pad."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_GND_TOP_LAUNCH_V1483.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE))
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('GND'); assert n
def tr(a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
tr((100.4,67.6),(100.9,67.6),pcbnew.F_Cu); tr((100.9,67.6),(101.2,68.2),pcbnew.F_Cu)
v=pcbnew.PCB_VIA(b); v.SetPosition(V(101.2,68.2)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.In1_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetIsRuleArea(False); z.SetMinThickness(pcbnew.FromMM(.20)); z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL); z.SetZoneName('RTL9210B_GND_RETURN_FIELD')
poly=pcbnew.VECTOR_VECTOR2I()
for xy in ((100.7,68.0),(116.0,68.0),(116.0,78.4),(100.7,78.4)): poly.append(V(*xy))
z.AddPolygon(poly); b.Add(z); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
