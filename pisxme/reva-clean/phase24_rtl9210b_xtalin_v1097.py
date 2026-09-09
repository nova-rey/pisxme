"""V1097: tight outboard XTAL_IN transition clear of U1.52/3V3."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RSET_V1092.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALIN_V1097.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('XTAL_IN')
add(b,n,[(94.05,67.2),(92.5,67.8)],F); via(b,n,(92.5,67.8))
add(b,n,[(92.5,67.8),(92.5,75.0),(86.0,75.0),(86.0,62.0)],B); via(b,n,(86.0,62.0)); add(b,n,[(86.0,62.0),(88.0,62.0)],F); add(b,n,[(88.0,59.0),(88.0,62.0)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
