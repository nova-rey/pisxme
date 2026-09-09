"""V983: orientation-0 QFN escape with ordered via ladder and remote U2."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ORIENTATION0_SOURCE_ESCAPE_V981.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ORIENTATION0_ORDERED_SPI_V983.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); u2=b.FindFootprintByReference('U2'); u2.SetPosition(u2.GetPosition()+pcbnew.VECTOR2I_MM(15,15))
vals={'SPICS':((101.95,70.8),(105,68.0),(110,95.0),(120,95.0)), 'SPISO':((101.95,71.2),(105,69.2),(111,93.8),(120,93.8)), 'SPISO3':((101.95,71.6),(105,70.4),(112,87.8),(120,87.8)), 'SPICLK':((101.95,72.8),(105,71.6),(113,89.0),(120,89.0)), 'SPISI':((101.95,73.2),(105,72.8),(114,90.2),(120,90.2))}
for name,(src,v1,bend,end) in vals.items():
 n=b.FindNet(name); tr(b,n,[src,(104,src[1]),v1],F); via(b,n,v1); tr(b,n,[v1,(bend[0],v1[1]),bend],B); via(b,n,bend); tr(b,n,[bend,end],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
