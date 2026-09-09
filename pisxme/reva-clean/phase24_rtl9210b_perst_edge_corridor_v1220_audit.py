"""Saved-board PERST_N audit for V1220; edges come only from native connectivity."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_PERST_EDGE_CORRIDOR_V1220.kicad_pcb'
G=[('U1','14'),('J1','50')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
    b.BuildConnectivity(); p=pads(b); c=b.GetConnectivity().GetConnectedItems(p[G[0]])
    return p[G[1]] in c
b=pcbnew.LoadBoard(str(PCB)); assert ok(b)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t); src=p[G[0]].GetPosition()
victims=[x for x in t.GetTracks() if x.GetNetname()=='PERST_N' and
         ((type(x).__name__=='PCB_VIA' and x.GetPosition()==pcbnew.VECTOR2I_MM(104.5,79.0)) or
          (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src)))]
assert victims, 'source cohort missing'
for v in victims: t.RemoveNative(v)
assert not ok(t), 'negative control did not break PERST_N'
print('PASS V1220 native U1.14/J1.50 PERST_N connectivity; complete source-cohort negative control PASS')
