"""V927: add the remaining SPISI source-to-flash route to the clean SPI escape."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V924_SPISO_REGEN_V926.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb'
F=pcbnew.F_Cu;B=pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('SPISI')
tr(b,n,[(101.2,66.05),(101.2,64.5),(101.6,64.0),(106.0,60.0)],F);via(b,n,106.0,60.0)
tr(b,n,[(106.0,60.0),(106.5,60.0),(106.5,75.2)],B);via(b,n,106.5,75.2);tr(b,n,[(106.5,75.2),(105.0,75.2)],F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
