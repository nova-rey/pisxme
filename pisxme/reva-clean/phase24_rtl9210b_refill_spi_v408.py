"""V408: native zone refill of the V407 SPI transplant."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_MERGE_SPI_V407.kicad_pcb'; out=H/'PHASE24_RTL9210B_MERGE_SPI_REFILLED_V408.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
