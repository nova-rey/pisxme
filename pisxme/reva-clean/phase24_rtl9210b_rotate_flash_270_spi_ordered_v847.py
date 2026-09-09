"""V847: ordered 270-degree SPI fanout with controls moved clear."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ROTATE_FLASH_270_SUPPORT_V844.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ROTATE_FLASH_270_SPI_ORDERED_V847.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for ref,target in {'R2':(120,75),'R3':(120,80)}.items():
 f=b.FindFootprintByReference(ref); q=f.FindPadByNumber('1').GetPosition(); f.SetPosition(f.GetPosition()+P(*target)-q)
for name,pts in {
 'SPISI':[(94.05,66.8),(92.5,66.8),(92.5,56),(88,56)],
 'SPICLK':[(94.05,67.2),(91.3,67.2),(91.3,57.2),(88,57.2)],
 'SPISO3':[(94.05,68.4),(90.1,68.4),(90.1,58.4),(88,58.4)],
}.items(): T(b,b.FindNet(name),pts)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
