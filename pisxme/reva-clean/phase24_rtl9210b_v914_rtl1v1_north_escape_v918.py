"""V918: north-side U1.25 RTL_1V1 power-plane escape."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V888_V772_SPLIT_NO_DUPLICATE_V914.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V914_RTL1V1_NORTH_ESCAPE_V918.kicad_pcb'
F=pcbnew.F_Cu;L=pcbnew.In2_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
tr(b,n,[(98.4,66.05),(98.4,63.5)],F);via(b,n,98.4,63.5)
tr(b,n,[(123.4,51.0),(123.4,48.0)],F);via(b,n,123.4,48.0)
tr(b,n,[(98.4,63.5),(98.4,56.0),(114.0,56.0),(114.0,48.0),(123.4,48.0)],L)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
