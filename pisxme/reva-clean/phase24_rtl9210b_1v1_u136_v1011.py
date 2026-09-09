"""V1011: move U1.36 RTL_1V1 transition west of the RTL_3V3 via."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_1V1_U116_V1009.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_1V1_U136_V1011.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1')
q=pcbnew.PCB_TRACK(b); q.SetStart(P(94.05,67.2)); q.SetEnd(P(91.8,67.2)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
q=pcbnew.PCB_VIA(b); q.SetPosition(P(91.8,67.2)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
