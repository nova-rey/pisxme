"""Native saved-board audit for the V595 local CLKREQ escape."""
from pathlib import Path
import pcbnew

PCB = Path(__file__).resolve().parent / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V595_CLKREQ_LOCAL.kicad_pcb'
GROUP = [('U1','13'), ('R3','1')]

def pads(b): return {(f.GetReference(), str(p.GetNumber())): p for f in b.GetFootprints() for p in f.Pads()}
def connected(b):
    b.BuildConnectivity(); q = pads(b); c = b.GetConnectivity().GetConnectedItems(q[GROUP[0]])
    return all(q[x] in c for x in GROUP[1:])

b = pcbnew.LoadBoard(str(PCB)); assert connected(b)
t = pcbnew.LoadBoard(str(PCB)); victims = [x for x in t.GetTracks() if x.GetNetname() == 'CLKREQ_N']
assert victims
for x in victims: t.RemoveNative(x)
assert not connected(t)
print('PASS V595 native local CLKREQ connectivity; trace-removal negative control PASS')
