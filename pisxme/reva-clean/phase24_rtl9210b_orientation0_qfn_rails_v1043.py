"""V1043: orientation-0 top-edge staggered 1V1/3V3 QFN escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ORIENTATION0_SOURCE_ESCAPE_V981.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ORIENTATION0_QFN_RAILS_V1043.kicad_pcb'; F,B,L=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n3=b.FindNet('RTL_3V3'); n1=b.FindNet('RTL_1V1')
for q in list(b.GetTracks()):
 if q.GetNetCode() in {n3.GetNetCode(),n1.GetNetCode()}: b.RemoveNative(q)
# Top-edge pads are staggered before their ordinary transitions; all copper
# leaves the package outward and no transition is placed in the pad row.
add(b,n1,[(100.8,66.05),(100.8,64.8),(102.0,64.8)],F); via(b,n1,(102.0,64.8))
add(b,n3,[(99.6,66.05),(99.6,64.2),(98.8,64.2)],F); via(b,n3,(98.8,64.2))
add(b,n1,[(99.2,66.05),(99.2,63.6),(97.8,63.6)],F); via(b,n1,(97.8,63.6))
add(b,n1,[(102.0,64.8),(98.8,64.8),(98.8,63.6),(97.8,63.6)],L)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
