"""V617: add SPICLK through a separate upper-source/lower-endpoint channel."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V615_SPI_BOTTOM_CLEAR2.kicad_pcb';out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V617_SPICLK_CHANNEL.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('SPICLK')
s(b,n,F,(102.05,59.2),(101.6,59.2));s(b,n,F,(101.6,59.2),(101.6,58.4));s(b,n,F,(101.6,58.4),(98.5,58.4));v(b,n,(98.5,58.4));s(b,n,B,(98.5,58.4),(93.5,58.4));s(b,n,B,(93.5,58.4),(93.5,73.0));v(b,n,(93.5,73.0));s(b,n,F,(93.5,73.0),(97.3,73.0));s(b,n,F,(97.3,73.0),(97.3,70.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
