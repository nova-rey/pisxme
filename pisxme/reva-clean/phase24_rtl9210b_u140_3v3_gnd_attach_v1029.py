"""V1029: restore local F.Cu GND attachments removed by V1026 broad scrub."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U140_3V3_GND_CONTACT_V1027.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U140_3V3_GND_ATTACH_V1029.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND')
for a,z in [((89.2,65.0),(89.2,67.0)),((92.2,62.0),(94.0,62.0)),((89.2,62.0),(89.2,60.0))]:
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
