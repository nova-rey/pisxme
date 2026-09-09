"""V760: complete the five-channel SPI endpoint allocation."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_QFN_SOURCE_FANOUT_SPISO3_SPICLK_SPISI_SPISO_ENDPOINT_V759.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_QFN_SOURCE_FANOUT_FULL_SPI_V760.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('SPICS')
t(b,n,B,(97.0,60.5),(97.0,80.0)); t(b,n,B,(97.0,80.0),(103.5,80.0)); v(b,n,(103.5,80.0)); t(b,n,F,(103.5,80.0),(105.0,80.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
