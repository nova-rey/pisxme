"""V661 disposable: combine retained V35 crystal/1V1/3V3 with proven 5V."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_RTL3V3_UPPER_V2.kicad_pcb'; out=H/'PHASE24_RTL9210B_V35_U2_LEFT_RAILS_5V_PLUS_3V3_PROBE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('RTL_5V')
s(b,n,F,(95.2,66.05),(95.2,55.0));v(b,n,(95.2,55.0));s(b,n,F,(101.95,66.8),(103.5,65.2));s(b,n,F,(103.5,65.2),(103.5,55.0));v(b,n,(103.5,55.0));s(b,n,B,(95.2,55.0),(116.4,55.0));s(b,n,B,(116.4,55.0),(116.4,69.0));v(b,n,(116.4,69.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
