"""V1488: coauthor the QFN north GND pocket around the RTL_1V1 shelf."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_GND_NORTH_POCKET_V1488.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE))
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('GND'); assert n
# This short RTL_1V1 shelf is regenerated later; remove only its old F.Cu
# horizontal/vertical geometry to expose the verified ordinary-via pocket.
for q in list(b.GetTracks()):
 if q.GetNetname()=='RTL_1V1':
  a=(q.GetStart()[0]/1e6,q.GetStart()[1]/1e6); z=(q.GetEnd()[0]/1e6,q.GetEnd()[1]/1e6)
  if (a,z) in [((95.2,66.05),(95.2,65.0)),((95.2,65.0),(97.8,65.0))]: b.Remove(q)
def tr(a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
tr((97.2,66.05),(97.2,64.8))
v=pcbnew.PCB_VIA(b); v.SetPosition(V(97.2,64.8)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.In1_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetIsRuleArea(False); z.SetMinThickness(pcbnew.FromMM(.20)); z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL); z.SetZoneName('RTL9210B_GND_RETURN_FIELD')
poly=pcbnew.VECTOR_VECTOR2I()
for xy in ((96.8,64.4),(116.0,64.4),(116.0,78.4),(96.8,78.4)): poly.append(V(*xy))
z.AddPolygon(poly); b.Add(z); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
