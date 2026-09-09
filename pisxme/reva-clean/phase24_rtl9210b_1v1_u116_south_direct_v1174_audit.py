"""Native saved-board audit for the V1174 U1.16 1V1 extension."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_1V1_U116_SOUTH_DIRECT_V1174.kicad_pcb'; G=[('U1','16'),('C4','1')]
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity();p=pads(b);return p[G[1]] in b.GetConnectivity().GetConnectedItems(p[G[0]])
b=pcbnew.LoadBoard(str(PCB));assert ok(b)
t=pcbnew.LoadBoard(str(PCB));p=pads(t);src=p[G[0]].GetPosition(); junction=pcbnew.VECTOR2I_MM(98.5,76.0); victims=[x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1' and ((type(x).__name__=='PCB_VIA' and x.GetPosition()==junction) or (type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src or x.GetStart()==junction or x.GetEnd()==junction)))]; assert len(victims)>=3
for v in victims:t.RemoveNative(v)
assert not ok(t)
print('PASS V1174 native U1.16-to-C4.1 1V1 connectivity; source-trace negative control PASS')
