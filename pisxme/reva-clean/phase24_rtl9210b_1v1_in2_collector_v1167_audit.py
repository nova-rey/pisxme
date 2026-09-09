"""Saved-board native audit for the V1167 1V1 power primitive."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_1V1_IN2_COLLECTOR_V1167.kicad_pcb'
G=[('U1','55'),('C4','1')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
    b.BuildConnectivity(); p=pads(b); return p[G[1]] in b.GetConnectivity().GetConnectedItems(p[G[0]])
b=pcbnew.LoadBoard(str(PCB)); assert ok(b)
t=pcbnew.LoadBoard(str(PCB)); pp=pads(t); v=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1' and type(x).__name__!='PCB_VIA' and (x.GetStart()==pp[G[0]].GetPosition() or x.GetEnd()==pp[G[0]].GetPosition())); t.RemoveNative(v); assert not ok(t)
print('PASS V1167 native U1.55-to-C4.1 1V1 connectivity; source-trace negative control PASS')
