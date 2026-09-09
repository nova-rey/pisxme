"""Saved-board V1232 audit for REFCLK plus co-authored control endpoints."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_REFCLK_CONTROL_COAUTHOR_V1232.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,a,z):
    b.BuildConnectivity(); p=pads(b); return p[z] in b.GetConnectivity().GetConnectedItems(p[a])
G=[(('U1','13'),('J1','52')),(('U1','14'),('J1','50')),(('U1','61'),('J1','55')),(('U1','62'),('J1','53'))]
b=pcbnew.LoadBoard(str(PCB)); assert all(connected(b,a,z) for a,z in G)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t)
for net,xy,padno in [('CLKREQ_N',(98.8,76.0),'13'),('PERST_N',(100.0,83.0),'14'),('REFCLK_P',(93.2,77.8),'61'),('REFCLK_N',(92.2,78.5),'62')]:
    src=p[('U1',padno)].GetPosition(); vs=[x for x in t.GetTracks() if x.GetNetname()==net and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==pcbnew.VECTOR2I_MM(*xy)) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src)))]
    assert vs, net+' source cohort missing'
    for v in vs: t.RemoveNative(v)
assert all(not connected(t,*g) for g in G)
print('PASS V1232 native CLKREQ_N/PERST_N/REFCLK_P/REFCLK_N endpoint connectivity; four complete source-cohort negative controls PASS')
