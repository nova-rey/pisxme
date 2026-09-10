"""V1408: upper B.Cu join from U2 RTL_3V3 support to the rail."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U160_1V1_TOP_SHELF_V1392.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U2_3V3_UPPER_JOIN_V1408.kicad_pcb'
B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(B); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3'); assert n
tr(b,n,[(116.0,77.2),(116.0,62.8),(108.0,62.8)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
