"""Saved-board audit for V1226 control departures with negative controls."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_PERST_EDGE_CORRIDOR_V1226.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,a,z):
    b.BuildConnectivity(); p=pads(b); return p[z] in b.GetConnectivity().GetConnectedItems(p[a])
G=[(('U1','13'),('J1','52')), (('U1','14'),('J1','50'))]
b=pcbnew.LoadBoard(str(PCB)); assert all(connected(b,a,z) for a,z in G)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t)
for net,xy,padno in [('CLKREQ_N',(98.8,76.0),'13'),('PERST_N',(100.0,83.0),'14')]:
    src=p[('U1',padno)].GetPosition(); vs=[x for x in t.GetTracks() if x.GetNetname()==net and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==pcbnew.VECTOR2I_MM(*xy)) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src)))]
    assert vs
    for v in vs: t.RemoveNative(v)
assert not connected(t,*G[0]) and not connected(t,*G[1])
print('PASS V1226 native CLKREQ_N and PERST_N endpoint connectivity; both complete source-cohort negative controls PASS')
