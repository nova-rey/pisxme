"""Saved-board CLKREQ_N audit for V1211."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_CLKREQ_EDGE_CORRIDOR_V1211.kicad_pcb'; G=[('U1','13'),('R3','1'),('J1','52')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity(); p=pads(b); c=b.GetConnectivity().GetConnectedItems(p[G[0]]); return all(p[x] in c for x in G[1:])
b=pcbnew.LoadBoard(str(PCB)); assert ok(b)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t); src=p[G[0]].GetPosition(); victims=[x for x in t.GetTracks() if x.GetNetname()=='CLKREQ_N' and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==pcbnew.VECTOR2I_MM(99.6,76.0)) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src)))]; assert victims
for v in victims: t.RemoveNative(v)
assert not ok(t)
print('PASS V1211 native U1.13/R3.1/J1.52 CLKREQ_N connectivity; complete source-cohort negative control PASS')
