"""V1267: add RTL_1V1 pad 55 to the V1266 live source-field basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_COUPLED_RXN_1V1_SOURCEFIELD_V1266.kicad_pcb';OUT=H/'PHASE24_RTL9210B_PAD55_1V1_V1267.kicad_pcb';F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
s(b,n,F,[(94.05,68.0),(93.4,68.0),(92.6,67.5),(87.5,67.5)]);v(b,n,(87.5,67.5));s(b,n,B,[(87.5,67.5),(87.0,67.5),(87.0,71.2)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
