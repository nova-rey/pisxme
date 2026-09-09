"""V1056: regenerate five SPI channels to the rotated U2 row."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ROTATE_U2_HORIZONTAL_V1055.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ROTATE_U2_SPI_V1056.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
# Source endpoint, source transition, B.Cu lane, endpoint transition, U2 pad.
for name,sy,sx,ex in [('SPICS',70.8,110.0,111.4),('SPISO',71.2,109.0,112.6),('SPISO3',71.6,106.0,118.6),('SPICLK',72.8,107.0,117.4),('SPISI',73.2,108.0,116.2)]:
 n=b.FindNet(name); add(b,n,[(104.0,sy),(sx,sy)],F); via(b,n,(sx,sy)); add(b,n,[(sx,sy),(ex,sy)],B); via(b,n,(ex,sy)); add(b,n,[(ex,sy),(ex,76.4)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
