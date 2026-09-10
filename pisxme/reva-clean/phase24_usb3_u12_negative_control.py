"""Negative control: remove one saved USB3 segment and require audit failure."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
source = R / 'PHASE24_STORAGE_USB3_SHIFTED_ESCAPE_V121.kicad_pcb'
output = R / 'PHASE24_USB3_U12_NEGATIVE_CONTROL.kicad_pcb'
b = pcbnew.LoadBoard(str(source))
removed = False
for item in list(b.GetTracks()):
    if item.GetNetname().rsplit('/', 1)[-1] == 'CM5_USB3_RX_N' and not isinstance(item, pcbnew.PCB_VIA):
        b.RemoveNative(item)
        removed = True
        break
if not removed:
    raise RuntimeError('did not find a saved RX_N segment to remove')
b.Save(str(output))
print(output)
