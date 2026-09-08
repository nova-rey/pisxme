"""V603: add an independent SPISO3 source/flash escape to V602."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V602_SPISI_ESCAPE_WEST.kicad_pcb';out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V603_SPISO3_ESCAPE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('SPISO3');s(b,n,F,(102.05,60.4),(99.5,60.4));v(b,n,(99.5,60.4));s(b,n,B,(99.5,60.4),(98.5,60.4));s(b,n,B,(98.5,60.4),(98.5,68.5));v(b,n,(98.5,68.5));s(b,n,F,(98.5,68.5),(98.5,70.0));b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
