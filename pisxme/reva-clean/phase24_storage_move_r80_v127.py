"""V127: move storage-local R80 clear of the proven USB3 corridor."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
SOURCE = R / 'PHASE24_STORAGE_USB3_REFILLED_V125.kicad_pcb'
OUTPUT = R / 'PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb'
b = pcbnew.LoadBoard(str(SOURCE))
r80 = b.FindFootprintByReference('R80')
if r80 is None: raise RuntimeError('missing storage support R80')
r80.SetPosition(pcbnew.VECTOR2I_MM(166.0, 130.0))
b.BuildListOfNets()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.BuildConnectivity()
b.Save(str(OUTPUT)); print(OUTPUT)
