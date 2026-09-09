"""V843: co-move RTL9210B crystal/RSET support away from rotated U2."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ROTATE_FLASH_90_V842.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ROTATE_FLASH_SUPPORT_V843.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
for ref,delta in {'Y1':(-10,-5),'C1':(-10,-5),'C2':(-10,-5),'R1':(-10,-5)}.items():
 f=b.FindFootprintByReference(ref); f.SetPosition(f.GetPosition()+pcbnew.VECTOR2I_MM(*delta))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
