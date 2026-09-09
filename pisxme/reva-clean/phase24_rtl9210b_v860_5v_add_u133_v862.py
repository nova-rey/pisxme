"""V862: join U1.33 into V860 at the actual In2 junction."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V857_5V_RAIL_PROBE_V860.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V860_5V_ADD_U133_V862.kicad_pcb'
F,L=pcbnew.F_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_5V')
tr(b,n,F,(95.2,66.05),(95.2,64.5)); via(b,n,95.2,64.5)
tr(b,n,L,(95.2,64.5),(105.5,66.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
