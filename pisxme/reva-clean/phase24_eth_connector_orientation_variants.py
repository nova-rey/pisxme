"""Create disposable Ethernet connector orientation launch variants."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb'
for rotation in (90,270):
    b=pcbnew.LoadBoard(str(BASE)); f=b.FindFootprintByReference('J2')
    f.SetOrientationDegrees(rotation)
    out=ROOT/f'PHASE24_ETH_J2_ROT{rotation}_PLACEMENT.kicad_pcb'
    b.Save(str(out)); print(out)
