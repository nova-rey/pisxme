"""Negative control for the V666 native QFN escape discriminator."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_QFN_39_40_CLEAN_ESCAPE_FIXTURE_V666.kicad_pcb'
out=H/'PHASE24_RTL9210B_QFN_39_40_CLEAN_ESCAPE_FIXTURE_V666_NEGATIVE.kicad_pcb'
b=pcbnew.LoadBoard(str(src))
victims=[q for q in b.GetTracks() if q.GetNetname()=='RTL_3V3']
assert victims, 'required RTL_3V3 escape trace missing'
b.RemoveNative(victims[0]); b.Save(str(out)); print(out)
