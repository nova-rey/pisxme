"""V892: perpendicular QFN dogbone trial for XTAL_OUT."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V885_SUPPORT_GND_RETURN_V888.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V888_CRYSTAL_SCRUBBED_ROUTE_V892.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for x in list(b.GetTracks()):
 pts=[x.GetStart(),x.GetEnd()]
 if x.GetNetname()=='RTL_3V3' and any(92.5<=p.x/1e6<=95.5 and 73.5<=p.y/1e6<=77 for p in pts): b.RemoveNative(x)
tr(b,b.FindNet('XTAL_IN'),[(95.2,73.95),(95.2,76.0),(86.0,76.0),(86.0,58.0),(88.0,59.0),(88.0,62.0)])
tr(b,b.FindNet('XTAL_OUT'),[(95.6,73.95),(95.6,74.6),(96.8,75.8),(96.8,77.0),(84.0,77.0),(84.0,54.0),(90.2,54.0),(90.2,59.0),(89.4,59.0),(91.0,62.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
