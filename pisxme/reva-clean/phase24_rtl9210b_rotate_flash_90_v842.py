"""V842: rotate the SPI flash endpoint and place its pin-order field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_PROBE_V712.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ROTATE_FLASH_90_V842.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
f=b.FindFootprintByReference('U2'); f.SetOrientationDegrees(90)
q=f.FindPadByNumber('5').GetPosition(); f.SetPosition(f.GetPosition()+pcbnew.VECTOR2I_MM(88,56)-q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
