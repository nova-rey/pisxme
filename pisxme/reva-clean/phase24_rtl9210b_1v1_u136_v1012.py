"""V1012: connect the west U1.36 transition into the filled In2 pocket."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_1V1_U136_V1011.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_1V1_U136_V1012.kicad_pcb'; L=pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1')
q=pcbnew.PCB_TRACK(b); q.SetStart(P(91.8,67.2)); q.SetEnd(P(93.0,67.2)); q.SetLayer(L); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
