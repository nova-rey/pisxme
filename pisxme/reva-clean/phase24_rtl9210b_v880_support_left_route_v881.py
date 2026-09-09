"""V881: route relocated XTAL_IN/XTAL_OUT/RSET support around U1.52."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V879_SUPPORT_LEFT_V880.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V880_SUPPORT_LEFT_ROUTE_V881.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,*ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
tr(b,b.FindNet('XTAL_IN'),(95.2,73.95),(95.2,72.0),(88,72.0),(88,77.0),(88,80.0))
tr(b,b.FindNet('XTAL_OUT'),(95.6,73.95),(96.2,73.95),(96.2,71.5),(89.4,71.5),(89.4,77.0),(91,80.0))
tr(b,b.FindNet('RSET'),(94.05,73.2),(92.5,73.2),(92.5,81.0),(88,83.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
