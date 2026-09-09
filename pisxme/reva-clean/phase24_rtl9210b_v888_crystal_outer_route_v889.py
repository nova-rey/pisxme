"""V889: direct outer F.Cu escapes for relocated crystal support."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V885_SUPPORT_GND_RETURN_V888.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V888_CRYSTAL_OUTER_ROUTE_V889.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
tr(b,b.FindNet('XTAL_IN'),[(95.2,73.95),(95.2,76.0),(86.0,76.0),(86.0,58.0),(88.0,59.0),(88.0,62.0)])
tr(b,b.FindNet('XTAL_OUT'),[(95.6,73.95),(96.5,77.0),(84.0,77.0),(84.0,56.0),(89.4,59.0),(91.0,62.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
