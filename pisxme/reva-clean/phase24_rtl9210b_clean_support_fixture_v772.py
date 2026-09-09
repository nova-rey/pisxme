"""V772: keep the fixture banner inside the board outline."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_GROUND_V771.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_GROUND_V772.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
for d in b.GetDrawings():
 if type(d).__name__ == 'PCB_TEXT' and 'NON-PRODUCTION' in d.GetText(): d.SetPosition(pcbnew.VECTOR2I_MM(110.0,42.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
