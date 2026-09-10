"""V1421: RSET perimeter route from U1.51 to R1.1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_RTL5V_U117_FCU_RIGHT_V1415.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RSET_PERIMETER_V1421.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RSET'); assert n
for a,z in [((94.8,66.05),(94.8,64.5)),((94.8,64.5),(88.0,64.5)),((88.0,64.5),(88.0,65.0))]:
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
