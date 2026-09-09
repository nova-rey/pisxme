"""V1244 saved-board lane-0 audit with source-cohort negative controls."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_LANE0_FROM_V1243_V1244.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def conn(b,a,z):
 b.BuildConnectivity(); p=pads(b); return p[z] in b.GetConnectivity().GetConnectedItems(p[a])
G=[(('U1','64'),('J1','43')),(('U1','65'),('J1','41')),(('U1','67'),('J1','47')),(('U1','68'),('J1','49'))]
b=pcbnew.LoadBoard(str(PCB)); assert all(conn(b,a,z) for a,z in G)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t)
for net,xy,padno in [('LANE0_RXP',(93.6,75.5),'64'),('LANE0_RXN',(93.0,76.2),'65'),('LANE0_TXN',(95.0,75.5),'67'),('LANE0_TXP',(95.6,76.2),'68')]:
 src=p[('U1',padno)].GetPosition(); found=[x for x in t.GetTracks() if x.GetNetname()==net and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==pcbnew.VECTOR2I_MM(*xy)) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src)))]
 assert found, net+' source cohort missing'
 for x in found: t.RemoveNative(x)
assert all(not conn(t,a,z) for a,z in G)
print('PASS V1244 native lane-0 endpoint assertions; four source-cohort negative controls PASS')
