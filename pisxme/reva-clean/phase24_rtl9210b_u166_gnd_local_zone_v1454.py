"""V1454: disposable local F.Cu GND island for U1.66/pad69."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U166_GND_LOCAL_ZONE_V1454.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND'); assert n
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.F_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL); z.SetMinThickness(pcbnew.FromMM(.20)); z.SetZoneName('RTL9210B_LOCAL_QFN_GND')
z.SetAssignedPriority(1)
p=pcbnew.VECTOR_VECTOR2I()
for xy in ((93.2,69.2),(98.7,69.2),(98.7,73.8),(93.2,73.8)): p.append(P(*xy))
z.AddPolygon(p); b.Add(z); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
