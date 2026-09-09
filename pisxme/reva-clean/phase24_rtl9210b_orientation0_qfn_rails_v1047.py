"""V1047: correct C4-side 1V1 transition placement."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ORIENTATION0_QFN_RAILS_V1045.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ORIENTATION0_QFN_RAILS_V1047.kicad_pcb'; F,B,L=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n3=b.FindNet('RTL_3V3'); n1=b.FindNet('RTL_1V1')
# C3-side RTL_3V3 and C4-side RTL_1V1 use distinct ordinary transitions.
via(b,n3,(119.2,51.0)); add(b,n3,[(99.6,62.8),(108,62.8),(108,50),(119.2,50),(119.2,51)],B); add(b,n3,[(119.2,51),(120.4,51)],F)
via(b,n1,(122.8,51.0)); add(b,n1,[(102,64.8),(112,64.8),(112,52),(122.8,52),(122.8,51)],B); add(b,n1,[(122.8,51),(123.4,51)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
