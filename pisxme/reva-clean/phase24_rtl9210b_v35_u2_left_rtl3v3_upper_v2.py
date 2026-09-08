"""V2 upper RTL_3V3 fanout; avoid R3.1 and the RTL_5V via field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;base=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_CRYSTAL_COAUTHOR.kicad_pcb';out=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_RTL3V3_UPPER_V2.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def p(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(p(*a));q.SetEnd(p(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('RTL_3V3')
s(b,n,F,(94.8,66.05),(93.0,64.0));s(b,n,F,(93.0,64.0),(93.0,54.0));v(b,n,(93.0,54.0))
s(b,n,F,(90.2,56.0),(90.2,54.0));s(b,n,F,(90.2,54.0),(93.0,54.0))
s(b,n,F,(93.2,56.0),(93.2,54.0));s(b,n,F,(93.2,54.0),(93.0,54.0))
s(b,n,B,(93.0,54.0),(110.0,54.0));v(b,n,(110.0,54.0));s(b,n,F,(110.0,54.0),(110.0,60.8));v(b,n,(110.0,60.8))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
