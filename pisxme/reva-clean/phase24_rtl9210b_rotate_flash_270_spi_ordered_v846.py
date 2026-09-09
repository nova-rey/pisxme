"""V846: ordered orthogonal fanout for the monotonic 270-degree field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ROTATE_FLASH_270_SUPPORT_V844.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ROTATE_FLASH_270_SPI_ORDERED_V846.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for name,pts in {
 'SPISI':[(94.05,66.8),(92,66.8),(92,56),(88,56)],
 'SPICLK':[(94.05,67.2),(91,67.2),(91,57.2),(88,57.2)],
 'SPISO3':[(94.05,68.4),(90,68.4),(90,58.4),(88,58.4)],
}.items(): T(b,b.FindNet(name),pts)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
