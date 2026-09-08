"""Native saved-board audit for the V602 SPISI sub-primitive."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V602_SPISI_ESCAPE_WEST.kicad_pcb'
GROUP=[('U1','18'),('U2','5')]
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b):
 b.BuildConnectivity();q=pads(b);c=b.GetConnectivity().GetConnectedItems(q[GROUP[0]])
 return all(q[x] in c for x in GROUP[1:])
b=pcbnew.LoadBoard(str(PCB));assert connected(b)
t=pcbnew.LoadBoard(str(PCB));victims=[x for x in t.GetTracks() if x.GetNetname()=='SPISI'];assert victims
for x in victims:t.RemoveNative(x)
assert not connected(t)
print('PASS V602 native SPISI connectivity; trace-removal negative control PASS')
