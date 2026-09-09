"""V750: co-author SPISO3 and SPICLK on the V748 vertical endpoint field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_U2_ROTATE90_VERTICAL_SPISO3_V749.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_U2_ROTATE90_VERTICAL_SPISO3_SPICLK_V750.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def c(b,n,l,p):
 for a,z in zip(p,p[1:]): t(b,n,l,a,z)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('SPICLK')
c(b,n,F,[(100.8,66.05),(100.8,60.0)]); v(b,n,(100.8,60.0))
c(b,n,B,[(100.8,60.0),(104.5,60.0),(104.5,74.0)])
v(b,n,(104.5,74.0)); c(b,n,F,[(104.5,74.0),(105.0,74.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
