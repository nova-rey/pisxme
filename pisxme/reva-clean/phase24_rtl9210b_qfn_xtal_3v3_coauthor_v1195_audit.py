"""Saved-board audit for the V1195 paired crystal/3V3 field."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_QFN_XTAL_3V3_COAUTHOR_V1195.kicad_pcb'
GROUPS=[[('U1','52'),('U1','34'),('U1','39'),('C3','1')],[('U1','53'),('Y1','1'),('C1','1')],[('U1','54'),('Y1','2'),('C2','1')]]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,g):
 b.BuildConnectivity(); p=pads(b); c=b.GetConnectivity().GetConnectedItems(p[g[0]]); return all(p[x] in c for x in g[1:])
def source_cohort(t,src,net):
 return [x for x in t.GetTracks() if x.GetNetname()==net and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==src) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src)))]
b=pcbnew.LoadBoard(str(PCB)); assert all(connected(b,g) for g in GROUPS)
for g in GROUPS:
 t=pcbnew.LoadBoard(str(PCB)); p=pads(t); src=p[g[0]].GetPosition(); victims=source_cohort(t,src,p[g[0]].GetNetname()); assert victims
 for v in victims: t.RemoveNative(v)
 assert not connected(t,g),g
print('PASS V1195 native U1.52/3V3, XTAL_IN, and XTAL_OUT endpoint groups; three complete source-cohort negative controls PASS')
