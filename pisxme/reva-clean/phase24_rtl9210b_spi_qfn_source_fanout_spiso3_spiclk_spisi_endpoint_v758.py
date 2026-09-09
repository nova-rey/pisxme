"""V758: add the SPISI endpoint launch to the V757 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_QFN_SOURCE_FANOUT_SPISO3_SPICLK_ENDPOINT_V757.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_QFN_SOURCE_FANOUT_SPISO3_SPICLK_SPISI_ENDPOINT_V758.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('SPISI')
t(b,n,B,(106.0,60.0),(106.5,60.0)); t(b,n,B,(106.5,60.0),(106.5,75.2)); v(b,n,(106.5,75.2)); t(b,n,F,(106.5,75.2),(105.0,75.2))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
