"""V834: in-outline far-outboard control-island placement probe."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_GROUND_V772.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V772_CONTROL_ISLAND_INBOARD_V834.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
for ref,target in {'R2':(120,75),'R3':(120,80)}.items():
 f=b.FindFootprintByReference(ref); q=f.FindPadByNumber('1').GetPosition(); f.SetPosition(f.GetPosition()+pcbnew.VECTOR2I_MM(*target)-q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
