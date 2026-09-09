"""V822: direct topology probe for the south-moved SPI flash endpoint."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_MOVE_FLASH_SOUTH_V821.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_MOVE_FLASH_SOUTH_SPI_V822.kicad_pcb'
W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,a,z,l=pcbnew.F_Cu):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for name,a,z in [('SPISI',(94.05,66.8),(88.1,60)),('SPICLK',(94.05,67.2),(89.3,60)),('SPISO3',(94.05,68.4),(90.5,60)),('SPISO',(94.05,68.8),(84.5,60)),('SPICS',(94.05,69.2),(83.3,60))]:
 n=b.FindNet(name); T(b,n,a,z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
