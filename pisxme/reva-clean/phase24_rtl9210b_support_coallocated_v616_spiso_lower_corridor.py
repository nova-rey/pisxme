"""V616: add SPISO through a lower B.Cu corridor around retained SPI endpoints."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V615_SPI_BOTTOM_CLEAR2.kicad_pcb';out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V616_SPISO_LOWER_CORRIDOR.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('SPISO');s(b,n,F,(102.05,60.8),(98.5,60.8));v(b,n,(98.5,60.8));s(b,n,B,(98.5,60.8),(94.0,60.8));s(b,n,B,(94.0,60.8),(94.0,74.0));s(b,n,B,(94.0,74.0),(90.5,74.0));v(b,n,(90.5,74.0));s(b,n,F,(90.5,74.0),(92.5,74.0));s(b,n,F,(92.5,74.0),(92.5,70.0));b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
