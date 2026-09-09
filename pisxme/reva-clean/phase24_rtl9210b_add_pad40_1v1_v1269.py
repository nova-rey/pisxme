"""V1269: add RTL_1V1 pad 40 with an outward diagonal QFN escape."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_PAD50_1V1_V1268.kicad_pcb';OUT=H/'PHASE24_RTL9210B_PAD40_1V1_V1269.kicad_pcb';F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
s(b,n,F,[(99.2,66.05),(99.2,64.8)]);v(b,n,(99.2,64.8));s(b,n,B,[(99.2,64.8),(87.0,64.8)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
