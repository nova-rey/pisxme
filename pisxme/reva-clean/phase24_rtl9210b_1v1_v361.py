"""V361: refill native In2 RTL_1V1 zone from V360."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_RTL1V1_COALLOCATE_V360.kicad_pcb'; out=H/'PHASE24_RTL9210B_RTL1V1_COALLOCATE_V361.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
