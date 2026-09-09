"""V1072: attach U1.50 RTL_1V1 to the established west source field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_5V_SOURCE_V1071.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U150_1V1_V1072.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1')
pts=[(95.2,66.05),(95.2,64.8),(97.8,64.8),(97.8,63.6)]
for a,z in zip(pts,pts[1:]):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
