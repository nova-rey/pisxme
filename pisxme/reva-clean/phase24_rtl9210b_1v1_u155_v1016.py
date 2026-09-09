"""V1016: add U1.55 RTL_1V1 lower source departure."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_1V1_U150_V1015.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_1V1_U155_V1016.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1')
q=pcbnew.PCB_TRACK(b); q.SetStart(P(96.0,73.95)); q.SetEnd(P(96.0,75.5)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
q=pcbnew.PCB_VIA(b); q.SetPosition(P(96.0,75.5)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
