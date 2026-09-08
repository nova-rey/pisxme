"""V2 disposable RTL_5V field: native-pad escapes moved clear of U1.34."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL5V_PROBE_V2.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_5V')
s(b,n,F,(95.20,66.05),(96.20,64.90));v(b,n,(96.20,64.90));s(b,n,B,(96.20,64.90),(96.20,55.00))
s(b,n,F,(101.95,66.80),(104.20,65.60));v(b,n,(104.20,65.60));s(b,n,B,(104.20,65.60),(104.20,55.00))
s(b,n,B,(96.20,55.00),(116.40,55.00));v(b,n,(116.40,55.00));s(b,n,B,(116.40,55.00),(116.40,67.80));s(b,n,F,(116.40,67.80),(116.40,69.00))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
