"""V1515: rehome U1.55 RTL_1V1 around the crystal source edge."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RSET_WEST_V1508.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U155_REHOME_V1515.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('RTL_1V1'); assert n; F,B=pcbnew.F_Cu,pcbnew.B_Cu
for q in list(b.GetTracks()):
 if q.GetNetname()=='RTL_1V1' and q.GetLayer()==F:
  a=(q.GetStart()[0]/1e6,q.GetStart()[1]/1e6); z=(q.GetEnd()[0]/1e6,q.GetEnd()[1]/1e6)
  if {a,z} in ({(94.05,68.0),(92.0,68.0)},{(92.0,68.0),(92.0,64.0)}): b.RemoveNative(q)
def tr(a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
tr((94.05,68.0),(93.4,68.0),F); tr((93.4,68.0),(93.4,69.2),F)
v=pcbnew.PCB_VIA(b); v.SetPosition(V(93.4,69.2)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v); tr((93.4,69.2),(92.8,69.8),B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
