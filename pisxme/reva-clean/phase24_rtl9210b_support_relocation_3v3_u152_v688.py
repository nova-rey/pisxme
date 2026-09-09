"""V688: close the U1.52 RTL_3V3 left-edge branch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_U139_JOG_V687.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_U152_V688.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
for a,z in [((94.05,66.8),(92.0,66.8)),((92.0,66.8),(92.0,55.0)),((92.0,55.0),(103.0,55.0))]:
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
