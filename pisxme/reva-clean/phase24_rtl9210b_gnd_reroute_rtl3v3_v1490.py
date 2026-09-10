"""V1490: move the RTL_3V3 B.Cu shelf around the GND stitch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_GND_REROUTE_RTL3V3_V1490.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE))
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); g=b.FindNet('GND'); r=b.FindNet('RTL_3V3'); assert g and r
for q in list(b.GetTracks()):
 if q.GetNetname()=='RTL_3V3' and q.GetLayer()==pcbnew.B_Cu:
  a=(q.GetStart()[0]/1e6,q.GetStart()[1]/1e6); z=(q.GetEnd()[0]/1e6,q.GetEnd()[1]/1e6)
  if {a,z}=={(93.0,66.8),(99.6,66.8)}: b.Remove(q)
def tr(net,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)
tr(r,(93.0,66.8),(93.0,65.8),pcbnew.B_Cu); tr(r,(93.0,65.8),(99.6,65.8),pcbnew.B_Cu); tr(r,(99.6,65.8),(99.6,66.05),pcbnew.B_Cu)
v=pcbnew.PCB_VIA(b); v.SetPosition(V(97.2,67.2)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(g); v.SetNetCode(g.GetNetCode()); b.Add(v)
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.In1_Cu); z.SetNet(g); z.SetNetCode(g.GetNetCode()); z.SetIsRuleArea(False); z.SetMinThickness(pcbnew.FromMM(.20)); z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL); z.SetZoneName('RTL9210B_GND_RETURN_FIELD')
poly=pcbnew.VECTOR_VECTOR2I()
for xy in ((96.8,66.8),(116.0,66.8),(116.0,78.4),(96.8,78.4)): poly.append(V(*xy))
z.AddPolygon(poly); b.Add(z); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
