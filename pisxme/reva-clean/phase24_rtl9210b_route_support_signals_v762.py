"""V762: route XTAL_IN, XTAL_OUT, and RSET on the V761 support pocket."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_SUPPORT_PLACEMENT_V761.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_V762.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def c(b,n,p):
 for a,z in zip(p,p[1:]): t(b,n,F,a,z)
b=pcbnew.LoadBoard(str(BASE))
c(b,b.FindNet('XTAL_IN'),[(95.2,73.95),(95.2,75.2),(96.0,76.2),(96.0,77.0),(96.0,80.0)])
c(b,b.FindNet('XTAL_OUT'),[(95.6,73.95),(95.6,75.4),(97.4,77.0),(97.4,78.4),(99.0,80.0)])
c(b,b.FindNet('RSET'),[(94.05,73.2),(93.4,74.0),(93.4,81.8),(96.0,83.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
