"""V876: diagonal-left U1.34 departure clear of RTL_5V transition."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V870_3V3_U139_V871.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V871_3V3_U134_V876.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
for a,z in [((94.8,66.05),(94.3,65.5)),((94.3,65.5),(94.3,63.5)),((94.3,63.5),(93,63.5)),((93,63.5),(93,68.4)),((93,68.4),(94.05,68.4))]:
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
