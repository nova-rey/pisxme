"""V835: route the in-outline control island on separated B.Cu lanes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V772_CONTROL_ISLAND_INBOARD_V834.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V772_CONTROL_ISLAND_INBOARD_ROUTE_V835.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
n=b.FindNet('PEDET'); T(b,n,F,[(101.95,70.4),(104,70.4)]); V(b,n,(104,70.4)); T(b,n,B,[(104,70.4),(104,75),(119.2,75)]); V(b,n,(119.2,75)); T(b,n,F,[(119.2,75),(120,75)])
n=b.FindNet('CLKREQ_N'); T(b,n,F,[(101.95,68.4),(106,68.4)]); V(b,n,(106,68.4)); T(b,n,B,[(106,68.4),(106,80),(119.2,80)]); V(b,n,(119.2,80)); T(b,n,F,[(119.2,80),(120,80)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
