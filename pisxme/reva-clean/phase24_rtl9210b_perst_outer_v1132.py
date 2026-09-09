"""V1132: disposable PERST_N outer return adapted to current U1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_PEDET_ROUTE_V1124.kicad_pcb';OUT=H/'PHASE24_RTL9210B_PERST_OUTER_V1132.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('PERST_N');t(b,n,F,[(100.0,73.95),(100.0,75.5)]);v(b,n,(100.0,75.5));t(b,n,B,[(100.0,75.5),(100.0,48.0),(135.0,48.0),(135.0,69.5)]);v(b,n,(135.0,69.5));t(b,n,F,[(135.0,69.5),(136.0,70.275)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
