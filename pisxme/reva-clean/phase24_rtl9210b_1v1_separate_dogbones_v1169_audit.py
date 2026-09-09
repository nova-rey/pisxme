"""Native saved-board audit for the U1.55/60/63 1V1 extension."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_1V1_SEPARATE_DOGBONES_V1169.kicad_pcb'
G=[('U1','55'),('U1','60'),('U1','63'),('C4','1')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
    b.BuildConnectivity(); p=pads(b); c=b.GetConnectivity().GetConnectedItems(p[G[0]]); return all(p[x] in c for x in G[1:])
b=pcbnew.LoadBoard(str(PCB)); assert ok(b)
for target in G[:3]:
    t=pcbnew.LoadBoard(str(PCB)); p=pads(t); v=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1' and type(x).__name__!='PCB_VIA' and (x.GetStart()==p[target].GetPosition() or x.GetEnd()==p[target].GetPosition())); t.RemoveNative(v); assert not ok(t),target
print('PASS V1169 native U1.55/U1.60/U1.63-to-C4.1 1V1 connectivity; three source-trace negative controls PASS')
