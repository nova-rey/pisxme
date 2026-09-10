"""V1506: hop RSET around the one remaining RTL_1V1 B.Cu barrier."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_GND_FIELD_REPLACE_V1502.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RSET_WEST_V1506.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('RSET'); assert n
def tr(a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(*xy)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr((94.8,66.05),(94.8,64.4),pcbnew.F_Cu); via((94.8,64.4)); tr((94.8,64.4),(88.8,64.4),pcbnew.B_Cu); via((88.8,64.4)); tr((88.8,64.4),(87.2,64.4),pcbnew.F_Cu); via((87.2,64.4)); tr((87.2,64.4),(88.0,65.0),pcbnew.F_Cu)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
