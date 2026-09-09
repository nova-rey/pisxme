"""V752: monotonic five-net QFN source fan-out, endpoint-free probe."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_U2_ROTATE90_VERTICAL_PROBE_V748.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_QFN_SOURCE_FANOUT_V752.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
routes={
 'SPICS':((98.8,66.05),(97.0,60.5)),
 'SPISO':((99.2,66.05),(99.0,60.5)),
 'SPISO3':((99.6,66.05),(101.0,60.5)),
 'SPICLK':((100.8,66.05),(103.0,60.5)),
 'SPISI':((101.2,66.05),(105.0,60.5)),
}
b=pcbnew.LoadBoard(str(BASE))
for name,(src,dst) in routes.items():
 n=b.FindNet(name); t(b,n,F,src,(src[0],64.5)); t(b,n,F,(src[0],64.5),dst); v(b,n,dst)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
