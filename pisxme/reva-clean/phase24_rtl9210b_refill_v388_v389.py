"""V389: native zone refill of the complete V388 support/lane candidate."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_LANE0_REALLOCATE_RSET_3V3_XTALOUT_V388.kicad_pcb'
out=H/'PHASE24_RTL9210B_LANE0_REALLOCATE_RSET_3V3_XTALOUT_V389.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); filler=pcbnew.ZONE_FILLER(b); filler.Fill(b.Zones()); b.Save(str(out)); print(out)
