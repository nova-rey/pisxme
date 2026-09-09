"""V754: five-net source fan-out using the clean adjacent-pair dogbones."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_U2_ROTATE90_VERTICAL_PROBE_V748.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_QFN_SOURCE_FANOUT_V754.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def chain(b,n,p):
 for a,z in zip(p,p[1:]): t(b,n,a,z)
b=pcbnew.LoadBoard(str(BASE))
for name,pts,via_at in (
 ('SPICS',[(98.8,66.05),(98.8,64.5),(97.0,60.5)],(97.0,60.5)),
 ('SPISO',[(99.2,66.05),(99.2,64.5),(99.0,60.5)],(99.0,60.5)),
 ('SPISO3',[(99.6,66.05),(99.6,64.5),(101.0,60.5)],(101.0,60.5)),
 ('SPICLK',[(100.8,66.05),(100.8,64.5),(100.4,64.0),(104.0,60.0)],(104.0,60.0)),
 ('SPISI',[(101.2,66.05),(101.2,64.5),(101.6,64.0),(106.0,60.0)],(106.0,60.0)),):
 n=b.FindNet(name); chain(b,n,pts); v(b,n,via_at)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
