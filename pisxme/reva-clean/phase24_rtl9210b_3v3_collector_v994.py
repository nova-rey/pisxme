"""V994: complete the C3 branch on the V993 RTL_3V3 collector."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_3V3_COLLECTOR_V993.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_3V3_COLLECTOR_V994.kicad_pcb'; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
q=pcbnew.PCB_TRACK(b); q.SetStart(P(118.6,60.8)); q.SetEnd(P(118.6,51.0)); q.SetLayer(B); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
