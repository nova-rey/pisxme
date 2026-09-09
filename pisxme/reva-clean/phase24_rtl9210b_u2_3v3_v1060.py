"""V1060: co-author only the rotated U2.3/U2.8 same-net join."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ROTATE_U2_SPI_V1058.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U2_3V3_V1060.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
# Stay clear of the U2.4 GND return and leave the outer C3 join for a later
# corridor allocation; this primitive proves the two U2 supply pads cohere.
add(b,n,[(113.8,76.4),(113.8,74.8)],F); via(b,n,(113.8,74.8))
add(b,n,[(119.8,76.4),(119.8,78.0)],F); via(b,n,(119.8,78.0))
add(b,n,[(113.8,74.8),(119.8,78.0)],B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
