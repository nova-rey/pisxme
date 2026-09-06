"""Negative control for the assertion-only native SATA connectivity audit."""
from pathlib import Path
import pcbnew
BASE=Path(__file__).resolve().parent/'PHASE24_STORAGE_NATIVE_ORACLE_TRANSPLANT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); b.BuildConnectivity(); c=b.GetConnectivity()
def tok(p): return f'{p.GetParentFootprint().GetReference()}.{p.GetNumber()}'
pads={tok(p):p for f in b.GetFootprints() for p in f.Pads()}
# Remove one necessary donor track from the TX_P socket path.
removed=False
for t in list(b.GetTracks()):
    if t.GetNetname()=='/STORAGE/SATA_M2_TX_P' and not isinstance(t,pcbnew.PCB_VIA):
        b.Remove(t); removed=True; break
if not removed: raise AssertionError('negative control could not remove a SATA track')
b.BuildConnectivity(); c=b.GetConnectivity()
ends=('C30.1','J3.1')
reached={tok(x) for x in c.GetConnectedItems(pads[ends[0]]) if type(x).__name__=='PAD'}|{ends[0]}
if set(ends)<=reached: raise AssertionError('negative control unexpectedly remained connected')
print('SATA negative control: PASS (removed trace caused native disconnect)')
