"""V1419: direct F.Cu U1.66-to-exposed-pad GND connection."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_RTL5V_U117_FCU_RIGHT_V1415.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_QFN_GND_DIRECT_V1419.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND'); assert n
for pts in [[(97.2,66.05),(97.2,67.6)],[(94.05,72.4),(96.0,72.4),(96.0,70.0),(98.0,70.0)]]:
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
