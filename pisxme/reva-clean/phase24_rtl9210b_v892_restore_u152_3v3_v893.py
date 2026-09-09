"""V893: restore U1.52 RTL_3V3 around the completed crystal support."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V888_CRYSTAL_SCRUBBED_ROUTE_V892.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V892_RESTORE_U152_3V3_V893.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
pts=[(94.8,73.95),(94.8,75.0),(98.0,75.0),(98.0,82.0),(107.3,82.0),(107.3,77.6)]
for a,z in zip(pts,pts[1:]):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
