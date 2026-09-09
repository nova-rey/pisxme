"""Saved-board V1240 REFCLK native connectivity audit with negative controls."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_REFCLK_SOURCE_FIELD_CLEAR_V1240.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,a,z):
    b.BuildConnectivity(); p=pads(b); return p[z] in b.GetConnectivity().GetConnectedItems(p[a])
G=[(('U1','61'),('J1','55')),(('U1','62'),('J1','53'))]
b=pcbnew.LoadBoard(str(PCB)); assert all(connected(b,a,z) for a,z in G)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t)
for net,xy,padno in [('REFCLK_P',(91.5,78.5),'61'),('REFCLK_N',(92.5,79.2),'62')]:
    src=p[('U1',padno)].GetPosition(); vs=[x for x in t.GetTracks() if x.GetNetname()==net and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==pcbnew.VECTOR2I_MM(*xy)) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src)))]
    assert vs
    for v in vs: t.RemoveNative(v)
assert not connected(t,*G[0]) and not connected(t,*G[1])
print('PASS V1240 native REFCLK_P/N endpoint connectivity; complete pair source-cohort negative controls PASS')
