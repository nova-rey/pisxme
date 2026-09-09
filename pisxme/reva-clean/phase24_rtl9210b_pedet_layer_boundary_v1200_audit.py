"""Saved-board PEDET connectivity audit for V1200."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_PEDET_LAYER_BOUNDARY_V1200.kicad_pcb'; G=[('U1','8'),('R2','1'),('J1','69')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity(); p=pads(b); c=b.GetConnectivity().GetConnectedItems(p[G[0]]); return all(p[x] in c for x in G[1:])
b=pcbnew.LoadBoard(str(PCB)); assert ok(b)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t); src=p[G[0]].GetPosition(); victims=[x for x in t.GetTracks() if x.GetNetname()=='PEDET' and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==src) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src)))]; assert victims
for v in victims: t.RemoveNative(v)
assert not ok(t)
print('PASS V1200 native U1.8/R2.1/J1.69 PEDET connectivity; complete source-cohort negative control PASS')
