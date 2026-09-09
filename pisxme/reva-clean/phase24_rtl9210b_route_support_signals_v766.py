"""V766: keep XTAL_OUT on F.Cu; avoid a via in the adjacent source field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_SUPPORT_PLACEMENT_V761.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_V766.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def ch(b,n,p):
 for a,z in zip(p,p[1:]): t(b,n,a,z)
b=pcbnew.LoadBoard(str(BASE))
ch(b,b.FindNet('XTAL_IN'),[(95.2,73.95),(95.2,77.5),(96.0,77.5),(96.0,77.0),(96.0,80.0)])
ch(b,b.FindNet('XTAL_OUT'),[(95.6,73.95),(95.6,75.5),(97.4,77.0),(97.4,78.4),(99.0,80.0)])
ch(b,b.FindNet('RSET'),[(94.05,73.2),(93.4,74.0),(93.4,81.8),(96.0,83.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
