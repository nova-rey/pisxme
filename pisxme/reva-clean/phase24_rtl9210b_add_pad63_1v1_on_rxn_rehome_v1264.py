"""V1264: add one RTL_1V1 QFN pad-63 escape after the V1263 RXN rehome."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_RXN_SOURCE_REHOME_FOR_SUPPORT_V1263.kicad_pcb';OUT=H/'PHASE24_RTL9210B_PAD63_1V1_ON_RXN_REHOME_V1264.kicad_pcb';F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
s(b,n,F,[(94.05,71.2),(93.4,71.2),(92.8,71.2)]);v(b,n,(92.8,71.2))
s(b,n,B,[(92.8,71.2),(90.0,71.2),(90.0,60.0),(103.0,60.0),(103.0,50.0),(123.4,50.0)])
v(b,n,(103.0,60.0));v(b,n,(123.4,50.0));s(b,n,F,[(123.4,50.0),(123.4,51.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
