"""V1046: extend the clean orientation-0 rail transitions to C3/C4."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ORIENTATION0_QFN_RAILS_V1045.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ORIENTATION0_QFN_RAILS_V1046.kicad_pcb'; F,B,L=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n3=b.FindNet('RTL_3V3'); n1=b.FindNet('RTL_1V1')
# Separate outboard B.Cu supply corridors from the two existing QFN vias.
via(b,n3,(119.2,51.0)); add(b,n3,[(99.6,62.8),(108.0,62.8),(108.0,50.0),(119.2,50.0),(119.2,51.0)],B); add(b,n3,[(119.2,51.0),(120.4,51.0)],F)
via(b,n1,(122.2,51.0)); add(b,n1,[(102.0,64.8),(112.0,64.8),(112.0,52.0),(122.2,52.0),(122.2,51.0)],B); add(b,n1,[(122.2,51.0),(123.4,51.0)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
