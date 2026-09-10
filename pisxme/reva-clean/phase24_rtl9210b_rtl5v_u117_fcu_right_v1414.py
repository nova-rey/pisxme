"""V1414: U1.17 same-layer right-side RTL_5V fan-in."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_RTL5V_FCU_OUTBOARD_V1412.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RTL5V_U117_FCU_RIGHT_V1414.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_5V'); assert n
for a,z in [((101.2,73.95),(110.0,73.95)),((110.0,73.95),(110.0,67.2)),((110.0,67.2),(121.0,67.2))]:
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
