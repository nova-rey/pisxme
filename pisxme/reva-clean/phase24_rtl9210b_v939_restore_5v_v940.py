"""V940: restore RTL_5V source/capacitor power path around the accepted V939 field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_V938_RESTORE_U155_V939.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V939_RESTORE_5V_V940.kicad_pcb';F=pcbnew.F_Cu;L=pcbnew.In2_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_5V')
tr(b,n,[(101.95,66.8),(102.3,66.8),(102.3,65.8),(105.5,65.8)],F);via(b,n,(105.5,65.8));tr(b,n,[(95.2,66.05),(95.2,64.5),(96.5,64.5)],F);via(b,n,(96.5,64.5));tr(b,n,[(96.5,64.5),(105.5,65.8),(126.4,50.0)],L);via(b,n,(126.4,50.0));tr(b,n,[(126.4,50.0),(126.4,51.0)],F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
