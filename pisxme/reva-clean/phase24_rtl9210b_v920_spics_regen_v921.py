"""V921: regenerate SPICS around the accepted U1.25 1V1 escape."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V914_RTL1V1_NORTH_SPI_SCRUB_V920.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V920_SPICS_REGEN_V921.kicad_pcb'
F=pcbnew.F_Cu;B=pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('SPICS')
tr(b,n,[(98.8,66.05),(98.8,66.8),(97.2,66.8),(97.2,60.5)],F);via(b,n,97.2,60.5)
tr(b,n,[(97.2,60.5),(97.2,80.0),(103.5,80.0)],B);via(b,n,103.5,80.0);tr(b,n,[(103.5,80.0),(105.0,80.0)],F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
