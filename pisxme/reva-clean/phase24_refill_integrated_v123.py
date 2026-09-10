"""Rebuild native net/zone state for the V123 integrated USB3 candidate."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
SOURCE = R / 'PHASE24_STORAGE_USB3_SHIFTED_ESCAPE_V123.kicad_pcb'
OUTPUT = R / 'PHASE24_STORAGE_USB3_REFILLED_V125.kicad_pcb'
b = pcbnew.LoadBoard(str(SOURCE))
if b is None: raise RuntimeError('native board load failed')
b.BuildListOfNets()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.BuildConnectivity()
b.Save(str(OUTPUT))
print(OUTPUT)
