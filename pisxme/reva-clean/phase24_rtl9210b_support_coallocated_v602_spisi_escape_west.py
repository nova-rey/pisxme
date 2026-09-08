"""V602: move the SPISI transition west of the RTL_3V3 field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V595_CLKREQ_LOCAL.kicad_pcb';out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V602_SPISI_ESCAPE_WEST.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('SPISI');s(b,n,F,(102.05,58.8),(99.5,58.8));v(b,n,(99.5,58.8));s(b,n,B,(99.5,58.8),(96.1,58.8));s(b,n,B,(96.1,58.8),(96.1,68.5));v(b,n,(96.1,68.5));s(b,n,F,(96.1,68.5),(96.1,70.0));b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
