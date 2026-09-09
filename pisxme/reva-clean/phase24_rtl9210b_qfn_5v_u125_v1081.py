"""V1081: co-authored RTL_5V relocation and U1.25 RTL_1V1 escape."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U116_1V1_V1075.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_QFN_5V_U125_V1081.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n5=b.FindNet('RTL_5V'); n1=b.FindNet('RTL_1V1')
# Remove only prior generated 5V copper from the V1068 field.
for x in list(b.GetTracks()):
 if x.GetNetname()=='RTL_5V': b.RemoveNative(x)
# New 5V outer corridor, preserving both QFN endpoints and C5 source.
add(b,n5,[(101.95,67.2),(106.0,67.2)],F); via(b,n5,(106.0,67.2))
add(b,n5,[(106.0,67.2),(106.0,74.5)],B); via(b,n5,(106.0,74.5))
add(b,n5,[(106.0,74.5),(101.2,73.95)],F)
add(b,n5,[(106.0,67.2),(106.0,82.0),(126.4,82.0),(126.4,51.0)],B); via(b,n5,(126.4,51.0))
# U1.25 leaves the right QFN edge above SPICS, then returns on B.Cu.
add(b,n1,[(101.95,70.4),(104.2,70.2)],F); via(b,n1,(104.2,70.2))
add(b,n1,[(104.2,70.2),(104.2,64.8),(102.0,64.8)],B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
