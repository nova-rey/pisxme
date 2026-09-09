"""Saved-board V1242 native connectivity audit with negative controls."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RAILS_AROUND_REFCLK_V1242.kicad_pcb'
def pads(b):
    return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def conn(b,a,z):
    b.BuildConnectivity(); p=pads(b); return p[z] in b.GetConnectivity().GetConnectedItems(p[a])
G=[(('U1','61'),('J1','55')),(('U1','62'),('J1','53')),(('U1','13'),('J1','52')),(('U1','14'),('J1','50')),(('U1','16'),('C4','1')),(('U1','55'),('C4','1')),(('U1','60'),('C4','1')),(('U1','63'),('C4','1')),(('U1','52'),('C3','1')),(('U1','39'),('C3','1')),(('U1','45'),('U1','69'))]
b=pcbnew.LoadBoard(str(PCB)); assert all(conn(b,a,z) for a,z in G)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t)
for net,xy,padno in [('CLKREQ_N',(97.8,76.0),'13'),('REFCLK_P',(91.5,78.5),'61'),('REFCLK_N',(92.5,79.2),'62'),('RTL_1V1',(91.8,69.0),'55'),('RTL_3V3',(91.8,66.2),'52')]:
    src=p[('U1',padno)].GetPosition(); vs=[x for x in t.GetTracks() if x.GetNetname()==net and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==pcbnew.VECTOR2I_MM(*xy)) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src)))]
    assert vs, net+' source cohort missing'
    for v in vs: t.RemoveNative(v)
assert all(not conn(t,a,z) for a,z in [G[0],G[1],G[5],G[2]])
print('PASS V1242 native rail/REFCLK assertions; four complete source-cohort negative controls PASS')
