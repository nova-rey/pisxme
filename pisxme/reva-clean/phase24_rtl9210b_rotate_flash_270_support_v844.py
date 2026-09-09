"""V844: test the opposite rotated-flash pin-order orientation."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_PROBE_V712.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ROTATE_FLASH_270_SUPPORT_V844.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); f=b.FindFootprintByReference('U2'); f.SetOrientationDegrees(270)
q=f.FindPadByNumber('5').GetPosition(); f.SetPosition(f.GetPosition()+pcbnew.VECTOR2I_MM(88,56)-q)
for ref,delta in {'Y1':(-10,-5),'C1':(-10,-5),'C2':(-10,-5),'R1':(-10,-5)}.items():
 x=b.FindFootprintByReference(ref); x.SetPosition(x.GetPosition()+pcbnew.VECTOR2I_MM(*delta))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
