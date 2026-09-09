"""Saved-board PERST_N audit for V1221 with a source-cohort negative control."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_PERST_EDGE_CORRIDOR_V1221.kicad_pcb'; G=[('U1','14'),('J1','50')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
    b.BuildConnectivity(); p=pads(b); return p[G[1]] in b.GetConnectivity().GetConnectedItems(p[G[0]])
b=pcbnew.LoadBoard(str(PCB)); assert ok(b)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t); src=p[G[0]].GetPosition(); victims=[x for x in t.GetTracks() if x.GetNetname()=='PERST_N' and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==pcbnew.VECTOR2I_MM(128,79)) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src)))]
assert victims
for v in victims: t.RemoveNative(v)
assert not ok(t)
print('PASS V1221 native U1.14/J1.50 PERST_N connectivity; complete source-cohort negative control PASS')
