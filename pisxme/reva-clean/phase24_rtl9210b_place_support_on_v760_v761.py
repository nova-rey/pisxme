"""V761: place the crystal/RSET support pocket on the V760 SPI basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_QFN_SOURCE_FANOUT_FULL_SPI_V760.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V760_SUPPORT_PLACEMENT_V761.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
targets={'Y1':(96.0,77.0),'C1':(96.0,80.0),'C2':(99.0,80.0),'R1':(96.0,83.0)}
for ref,target in targets.items():
 f=b.FindFootprintByReference(ref); pad=f.FindPadByNumber('1'); q=pad.GetPosition()
 f.SetPosition(f.GetPosition()+pcbnew.VECTOR2I(P(*target).x-q.x,P(*target).y-q.y))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
for ref in targets:
 f=b.FindFootprintByReference(ref); p=f.FindPadByNumber('1'); q=p.GetPosition(); print(ref,round(pcbnew.ToMM(q.x),3),round(pcbnew.ToMM(q.y),3))
