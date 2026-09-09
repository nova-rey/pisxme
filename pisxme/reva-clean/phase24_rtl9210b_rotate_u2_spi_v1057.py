"""V1057: stagger source transitions before parallel SPI B.Cu lanes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ROTATE_U2_HORIZONTAL_V1055.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ROTATE_U2_SPI_V1057.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for name,sy,sx,ly,ex in [('SPICS',70.8,105.0,69.8,111.4),('SPISO',71.2,106.0,72.2,112.6),('SPISO3',71.6,107.0,70.6,118.6),('SPICLK',72.8,108.0,73.8,117.4),('SPISI',73.2,109.0,75.0,116.2)]:
 n=b.FindNet(name)
 add(b,n,[(104.0,sy),(sx,sy),(sx,ly)],F); via(b,n,(sx,ly)); add(b,n,[(sx,ly),(ex,ly)],B); via(b,n,(ex,ly)); add(b,n,[(ex,ly),(ex,76.4)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
