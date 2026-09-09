"""V845: route the monotonic upper three SPI channels on the V844 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ROTATE_FLASH_270_SUPPORT_V844.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ROTATE_FLASH_270_SPI_TOP_V845.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for name,a,z in [('SPISI',(94.05,66.8),(88,56)),('SPICLK',(94.05,67.2),(88,57.2)),('SPISO3',(94.05,68.4),(88,58.4))]: T(b,b.FindNet(name),a,z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
