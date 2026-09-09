"""V1058: reallocate SPI source dogbones around the two V1057 crossings."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ROTATE_U2_HORIZONTAL_V1055.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ROTATE_U2_SPI_V1058.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
# Source endpoint -> dogbone -> source via; all B.Cu lanes remain parallel.
paths=[('SPICS',[(104,70.8),(104.5,70.8),(104.5,69.8),(105,69.8)],(105,69.8),111.4),
       ('SPISO',[(104,71.2),(105.5,71.2),(105.5,70.4),(106,70.4)],(106,70.4),112.6),
       ('SPISO3',[(104,71.6),(106.5,71.6),(106.5,71.0),(107,71.0)],(107,71.0),118.6),
       ('SPICLK',[(104,72.8),(104.5,72.8),(104.5,72.0),(108,72.0)],(108,72.0),117.4),
       ('SPISI',[(104,73.2),(104.5,73.2),(104.5,75.2),(109,75.2)],(109,75.2),116.2)]
for name,src,sv,ex in paths:
 n=b.FindNet(name); add(b,n,src,F); via(b,n,sv)
 add(b,n,[sv,(ex,sv[1])],B); via(b,n,(ex,sv[1])); add(b,n,[(ex,sv[1]),(ex,76.4)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
