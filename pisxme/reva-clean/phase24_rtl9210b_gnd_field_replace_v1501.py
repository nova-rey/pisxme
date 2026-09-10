"""V1501: replace the blocking GND triangle with an In1 return field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_GND_REROUTE_RTL3V3_V1491.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_GND_FIELD_REPLACE_V1501.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); g=b.FindNet('GND'); assert g
# Remove only the old B.Cu GND collector edges.  F.Cu pad/field joins and
# their ordinary vias remain; the plane below becomes the return authority.
for q in list(b.GetTracks()):
 if q.GetNetname()=='GND' and q.GetLayer()==pcbnew.B_Cu: b.RemoveNative(q)
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.In1_Cu); z.SetNet(g); z.SetNetCode(g.GetNetCode()); z.SetIsRuleArea(False); z.SetMinThickness(pcbnew.FromMM(.20)); z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL); z.SetZoneName('RTL9210B_GND_RETURN_FIELD_WIDE')
poly=pcbnew.VECTOR_VECTOR2I()
for xy in ((87.5,57.5),(116.0,57.5),(116.0,78.4),(87.5,78.4)): poly.append(V(*xy))
z.AddPolygon(poly); b.Add(z); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
