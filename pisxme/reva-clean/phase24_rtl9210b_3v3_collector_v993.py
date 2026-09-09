"""V993: opposite-side R2/R3 RTL_3V3 branch launches."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_FULL_SOURCE_FIELD_3V3_V990.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_3V3_COLLECTOR_V993.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
tr(b,n,[(100.4,60.8),(122.5,60.8)],B)
via(b,n,(118.6,51.0)); tr(b,n,[(118.6,51.0),(120.4,51.0)],F)
tr(b,n,[(122.5,60.8),(122.5,75.0)],B); via(b,n,(122.5,75.0)); tr(b,n,[(122.5,75.0),(121.2,75.0)],F)
tr(b,n,[(122.5,75.0),(122.5,80.0)],B); via(b,n,(122.5,80.0)); tr(b,n,[(122.5,80.0),(121.2,80.0)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
