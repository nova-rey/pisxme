"""Save the CM5IO-authoritative USON-10 footprint into the clean library."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
oracle=pcbnew.LoadBoard(str(ROOT/'authority-inventory/cm5io-rev2/CM5IO.kicad_pcb'))
source=oracle.FindFootprintByReference('U1')
assert source is not None
source.SetReference('U')
io=pcbnew.PCB_IO_KICAD_SEXPR()
result=io.FootprintSave(str(ROOT/'PiSXMe_RevA_Clean.pretty'),source)
print('saved official USON-10 footprint:', result)
