"""V997: route U1 RTL_3V3 fanout around the inherited GND return."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_3V3_COLLECTOR_V994.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_3V3_GND_AWARE_V997.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
for pts,v in [([(94.8,66.05),(92.5,65.5)],(92.5,65.5)), ([(94.05,68.4),(92.5,68.4)],(92.5,68.4)), ([(94.8,73.95),(92.5,74.8)],(92.5,74.8))]: tr(b,n,pts,F); via(b,n,v)
# Go west of the diagonal GND return, above its upper endpoint, then return
# to the existing collector transition at (100.4,60.8).
tr(b,n,[(92.5,65.5),(87.0,65.5),(87.0,59.5),(100.4,59.5),(100.4,60.8)],B)
tr(b,n,[(92.5,65.5),(92.5,68.4)],B); tr(b,n,[(92.5,68.4),(92.5,74.8)],B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
