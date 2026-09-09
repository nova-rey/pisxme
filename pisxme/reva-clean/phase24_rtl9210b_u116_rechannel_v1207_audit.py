"""Saved-board audit for the V1207 U1.16 1V1 rechannel."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_U116_RECHANNEL_V1207.kicad_pcb'; G=[('U1','16'),('C4','1')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity(); p=pads(b); return p[G[1]] in b.GetConnectivity().GetConnectedItems(p[G[0]])
b=pcbnew.LoadBoard(str(PCB)); assert ok(b)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t); src=p[G[0]].GetPosition(); victims=[x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1' and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==pcbnew.VECTOR2I_MM(104.5,77.0)) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src or x.GetStart()==pcbnew.VECTOR2I_MM(104.5,77.0) or x.GetEnd()==pcbnew.VECTOR2I_MM(104.5,77.0))))]; assert len(victims)>=3
for v in victims: t.RemoveNative(v)
assert not ok(t)
print('PASS V1207 native U1.16-to-C4.1 1V1 connectivity; complete source-cohort negative control PASS')
