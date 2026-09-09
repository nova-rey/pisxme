"""V749: first single-channel route on the V748 vertical U2 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_U2_ROTATE90_VERTICAL_PROBE_V748.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_U2_ROTATE90_VERTICAL_SPISO3_V749.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def c(b,n,l,p):
 for a,z in zip(p,p[1:]): t(b,n,l,a,z)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('SPISO3')
c(b,n,F,[(99.6,66.05),(99.6,61.5)]); v(b,n,(99.6,61.5))
c(b,n,B,[(99.6,61.5),(103.5,61.5),(103.5,72.8)])
v(b,n,(103.5,72.8)); c(b,n,F,[(103.5,72.8),(105,72.8)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
