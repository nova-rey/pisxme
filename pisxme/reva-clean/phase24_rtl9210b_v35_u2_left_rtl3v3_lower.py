"""Complete the lower RTL_3V3 endpoints on the V35/U2-left basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;base=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_RTL3V3_UPPER_V2.kicad_pcb';out=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_RTL3V3_LOWER.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def p(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(p(*a));q.SetEnd(p(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('RTL_3V3')
# U1.39 -> relocated U2.8 via an isolated middle corridor.
s(b,n,F,(94.05,68.4),(92.8,67.7));s(b,n,F,(92.8,67.7),(92.8,66.5));v(b,n,(92.8,66.5));s(b,n,B,(92.8,66.5),(80.2,66.5));v(b,n,(80.2,66.5));s(b,n,F,(80.2,66.5),(80.2,80.0))
# U1.52 -> relocated U2.3 via the lower-left corridor.
s(b,n,F,(94.8,73.95),(94.8,75.0));v(b,n,(94.8,75.0));s(b,n,B,(94.8,75.0),(74.2,75.0));v(b,n,(74.2,75.0));s(b,n,F,(74.2,75.0),(74.2,80.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
