"""V882: move crystal/RSET support farther northwest as one block."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V879_SUPPORT_LEFT_V880.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V880_SUPPORT_NORTHWEST_V882.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
for ref in ('Y1','C1','C2','R1'):
 f=b.FindFootprintByReference(ref);f.SetPosition(f.GetPosition()+P(0,-18))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
