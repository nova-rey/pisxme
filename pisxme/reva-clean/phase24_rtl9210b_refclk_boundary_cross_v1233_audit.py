"""Saved-board V1233 REFCLK endpoint and pair source-cohort audit."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_REFCLK_BOUNDARY_CROSS_V1233.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,a,z):
    b.BuildConnectivity(); p=pads(b); return p[z] in b.GetConnectivity().GetConnectedItems(p[a])
G=[(('U1','61'),('J1','55')),(('U1','62'),('J1','53'))]
b=pcbnew.LoadBoard(str(PCB)); assert all(connected(b,a,z) for a,z in G)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t)
for net,xy,padno in [('REFCLK_P',(93.2,78.5),'61'),('REFCLK_N',(91.6,79.2),'62')]:
    src=p[('U1',padno)].GetPosition(); vs=[x for x in t.GetTracks() if x.GetNetname()==net and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==pcbnew.VECTOR2I_MM(*xy)) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src)))]
    assert vs
    for v in vs: t.RemoveNative(v)
assert not connected(t,*G[0]) and not connected(t,*G[1])
print('PASS V1233 native REFCLK_P/N endpoint connectivity; complete source-cohort negative controls PASS')
