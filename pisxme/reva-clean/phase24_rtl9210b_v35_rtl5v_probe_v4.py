"""V4 RTL_5V probe: move U1.17 escape clear of SPISI and land at C5."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL5V_PROBE_V4.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(p(*a));q.SetEnd(p(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('RTL_5V')
s(b,n,F,(95.20,66.05),(95.20,55.00));v(b,n,(95.20,55.00))
s(b,n,F,(101.95,66.80),(103.50,65.20));s(b,n,F,(103.50,65.20),(103.50,55.00));v(b,n,(103.50,55.00))
s(b,n,B,(95.20,55.00),(116.40,55.00));s(b,n,B,(116.40,55.00),(116.40,69.00));v(b,n,(116.40,69.00));s(b,n,F,(116.40,69.00),(116.40,69.00))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
