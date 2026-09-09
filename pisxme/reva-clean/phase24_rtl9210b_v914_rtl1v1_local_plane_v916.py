"""V916: tighter 1V1 escapes and north In2.PWR trunk."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V888_V772_SPLIT_NO_DUPLICATE_V914.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V914_RTL1V1_LOCAL_PLANE_V916.kicad_pcb'
F=pcbnew.F_Cu;L=pcbnew.In2_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
tr(b,n,[(94.05,67.2),(92.2,67.2)],F);via(b,n,92.2,67.2)
tr(b,n,[(94.05,68.8),(92.2,68.8)],F);via(b,n,92.2,68.8)
tr(b,n,[(123.4,51.0),(123.4,48.0)],F);via(b,n,123.4,48.0)
tr(b,n,[(92.2,67.2),(90.0,67.2),(90.0,58.0),(114.0,58.0),(114.0,48.0),(123.4,48.0)],L)
tr(b,n,[(92.2,68.8),(90.0,68.8),(90.0,67.2)],L)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
