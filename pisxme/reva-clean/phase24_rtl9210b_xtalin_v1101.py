"""V1101: farther-out XTAL_IN via below the 3V3 edge field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RSET_V1092.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALIN_V1101.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('XTAL_IN')
add(b,n,[(94.05,67.2),(93.2,67.2),(93.0,67.5),(91.5,68.6)],F); via(b,n,(91.5,68.6))
add(b,n,[(91.5,68.6),(91.5,75.0),(85.5,75.0),(85.5,62.0)],B); via(b,n,(85.5,62.0)); add(b,n,[(85.5,62.0),(88.0,62.0)],F); add(b,n,[(88.0,59.0),(88.0,62.0)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
