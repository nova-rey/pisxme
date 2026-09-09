"""V747: move SPICS to B.Cu so the SPISO3 source escape stays monotonic."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_U1_ROTATE90_PROBE_V730.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_U1_ROTATE90_SPICS_SPISO_SPISO3_V747.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def vi(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def ch(b,n,l,p):
 for a,z in zip(p,p[1:]): tr(b,n,l,a,z)
b=pcbnew.LoadBoard(str(BASE))
# SPICS: early F escape, then B.Cu corridor; endpoint return is below the
# SPISO shelf so the two endpoint launches do not intersect.
n=b.FindNet('SPICS'); ch(b,n,F,[(98.8,66.05),(98.8,62.5)]); vi(b,n,(98.8,62.5)); ch(b,n,B,[(98.8,62.5),(104,62.5),(104,82.5),(105,82.5)]); vi(b,n,(105,82.5)); ch(b,n,F,[(105,82.5),(105,80)])
# SPISO: separate early handoff and raised endpoint shelf.
n=b.FindNet('SPISO'); ch(b,n,F,[(99.2,66.05),(99.2,64.0)]); vi(b,n,(99.2,64.0)); ch(b,n,B,[(99.2,64.0),(102.5,64.0),(102.5,83.5),(106.2,83.5)]); vi(b,n,(106.2,83.5)); ch(b,n,F,[(106.2,83.5),(106.2,80)])
# SPISO3: distinct F source escape and B.Cu long channel.
n=b.FindNet('SPISO3'); ch(b,n,F,[(99.6,66.05),(99.6,61.5)]); vi(b,n,(99.6,61.5)); ch(b,n,B,[(99.6,61.5),(112.2,61.5),(112.2,82.5)]); vi(b,n,(112.2,82.5)); ch(b,n,F,[(112.2,82.5),(112.2,80)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
