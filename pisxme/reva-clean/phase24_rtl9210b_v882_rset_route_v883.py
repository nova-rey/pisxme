"""V883: route RSET to the northwest relocated R1 support."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V880_SUPPORT_NORTHWEST_V882.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V882_RSET_ROUTE_V883.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RSET')
for a,z in [((94.05,73.2),(92.5,73.2)),((92.5,73.2),(92.5,65)),((92.5,65),(88,65))]:
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
