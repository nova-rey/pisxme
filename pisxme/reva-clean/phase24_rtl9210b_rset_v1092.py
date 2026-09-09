"""V1092: corrected RSET entry around R1's adjacent GND pad."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U125_1V1_V1090.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RSET_V1092.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RSET'); pts=[(94.8,66.05),(92.5,66.05),(92.5,64.0),(88.0,64.0),(88.0,65.0)]
for a,z in zip(pts,pts[1:]):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
