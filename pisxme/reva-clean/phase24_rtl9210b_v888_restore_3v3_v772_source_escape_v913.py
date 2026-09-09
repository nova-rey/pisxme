"""V913: restore 3V3 and transplant the native V772 crystal source escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V885_SUPPORT_GND_RETURN_V888.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V888_RESTORE_3V3_V772_SOURCE_ESCAPE_V913.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3');tr(b,n,[(94.8,73.95),(94.8,76.0),(93.0,76.0)]);via(b,n,93.0,76.0)
tr(b,b.FindNet('XTAL_IN'),[(95.2,73.95),(95.2,77.5),(96.0,77.5),(96.0,80.0),(86.0,80.0),(86.0,58.0),(88.0,59.0),(88.0,62.0)])
tr(b,b.FindNet('XTAL_OUT'),[(95.6,73.95),(95.6,75.5),(97.4,75.5),(97.4,77.0),(97.4,78.4),(84.0,78.4),(84.0,54.0),(90.2,54.0),(90.2,59.0),(89.4,59.0),(91.0,62.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
