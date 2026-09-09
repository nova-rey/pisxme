"""V751: add SPICS and SPISO to the clean V750 two-channel basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_U2_ROTATE90_VERTICAL_SPISO3_SPICLK_V750.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_U2_ROTATE90_VERTICAL_FOUR_CHANNELS_V751.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def c(b,n,l,p):
 for a,z in zip(p,p[1:]): t(b,n,l,a,z)
b=pcbnew.LoadBoard(str(BASE))
# SPICS: drop below all endpoint shelves before approaching its U2.1 pad.
n=b.FindNet('SPICS'); c(b,n,F,[(98.8,66.05),(98.8,62.5)]); v(b,n,(98.8,62.5)); c(b,n,B,[(98.8,62.5),(98.8,84.0),(103.0,84.0),(103.0,80.0)]); v(b,n,(103.0,80.0)); c(b,n,F,[(103.0,80.0),(105.0,80.0)])
# SPISO: source transition stays left of the existing B.Cu channels; return
# below them and use a short F.Cu dogbone to U2.2.
n=b.FindNet('SPISO'); c(b,n,F,[(99.2,66.05),(99.2,59.5)]); v(b,n,(99.2,59.5)); c(b,n,B,[(99.2,59.5),(99.2,82.0),(104.0,82.0),(104.0,78.8)]); v(b,n,(104.0,78.8)); c(b,n,F,[(104.0,78.8),(105.0,78.8)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
