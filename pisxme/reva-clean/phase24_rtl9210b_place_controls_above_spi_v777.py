"""V777: move PEDET/CLKREQ_N pull components above the SPI channels."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_GROUND_V772.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CONTROL_ABOVE_SPI_PLACEMENT_V777.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); targets={'C3':(91.0,78.0),'C4':(99.0,76.0),'C5':(104.0,65.0),'R2':(108.0,60.0),'R3':(108.0,63.0)}
for ref,target in targets.items():
 f=b.FindFootprintByReference(ref); q=f.FindPadByNumber('1').GetPosition(); f.SetPosition(f.GetPosition()+pcbnew.VECTOR2I(P(*target).x-q.x,P(*target).y-q.y))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
