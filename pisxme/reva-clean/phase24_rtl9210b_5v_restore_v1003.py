"""V1003: below-R2/R3 RTL_5V shelf and vertical C5 launch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_3V3_GND_AWARE_V999.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_5V_RESTORE_V1003.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_5V')
tr(b,n,[(101.95,66.8),(102.3,66.8),(102.3,65.8),(105.5,65.8)],F); via(b,n,(105.5,65.8))
tr(b,n,[(95.2,66.05),(95.2,64.5),(96.5,64.5)],F); via(b,n,(96.5,64.5))
tr(b,n,[(96.5,64.5),(96.5,67.5),(105.5,67.5),(121.5,67.5),(121.5,81.0),(126.4,81.0),(126.4,52.0)],B); via(b,n,(126.4,52.0)); tr(b,n,[(126.4,52.0),(126.4,51.0)],F)
tr(b,n,[(105.5,65.8),(105.5,67.5)],B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
