"""V774: clear C3/RSET and R2/R3 from V760 signal corridors."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_GROUND_V772.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V760_RAIL_CONTROL_PLACEMENT_V774.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); targets={'C3':(91.0,78.0),'C4':(99.0,76.0),'C5':(104.0,65.0),'R2':(107.0,67.0),'R3':(107.0,70.0)}
for ref,target in targets.items():
 f=b.FindFootprintByReference(ref); q=f.FindPadByNumber('1').GetPosition(); f.SetPosition(f.GetPosition()+pcbnew.VECTOR2I(P(*target).x-q.x,P(*target).y-q.y))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
for ref in targets:
 q=b.FindFootprintByReference(ref).FindPadByNumber('1').GetPosition(); print(ref,round(pcbnew.ToMM(q.x),3),round(pcbnew.ToMM(q.y),3))
