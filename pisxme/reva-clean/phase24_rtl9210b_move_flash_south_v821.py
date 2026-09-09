"""V821: disposable test of moving the SPI flash south as a coherent endpoint."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_CONTROLS_V808.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_MOVE_FLASH_SOUTH_V821.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
u=next(f for f in b.GetFootprints() if f.GetReference()=='U2')
u.SetPosition(u.GetPosition()+pcbnew.VECTOR2I_MM(0,10))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
