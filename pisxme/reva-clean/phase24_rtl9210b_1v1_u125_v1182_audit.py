"""Native saved-board audit for the four accepted 1V1 QFN endpoints."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_1V1_U125_UPPER_EAST_WIDE_V1182.kicad_pcb'
G=[('U1','55'),('U1','60'),('U1','63'),('U1','25'),('C4','1')]
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity();p=pads(b);c=b.GetConnectivity().GetConnectedItems(p[G[0]]);return all(p[x] in c for x in G[1:])
b=pcbnew.LoadBoard(str(PCB));assert ok(b)
for target in G[:4]:
 t=pcbnew.LoadBoard(str(PCB));p=pads(t);src=p[target].GetPosition()
 if target==('U1','25'):
  # VECTOR2I is intentionally kept as a list: pcbnew.VECTOR2I is not
  # hashable in the KiCad Python bindings.  Equality still compares the
  # native coordinates exactly, which is the required physical-contact test.
  pts=[src,pcbnew.VECTOR2I_MM(103.0,70.4),pcbnew.VECTOR2I_MM(104.0,68.5),pcbnew.VECTOR2I_MM(109.5,68.5)]
  victims=[x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1' and ((type(x).__name__=='PCB_VIA' and x.GetPosition() in pts) or (type(x).__name__!='PCB_VIA' and (x.GetStart() in pts or x.GetEnd() in pts)))]
 else:
  victims=[next(x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1' and type(x).__name__!='PCB_VIA' and (x.GetStart()==src or x.GetEnd()==src))]
 for v in victims:t.RemoveNative(v)
 assert not ok(t),target
print('PASS V1182 native U1.55/U1.60/U1.63/U1.25-to-C4.1 1V1 connectivity; four source-trace negative controls PASS')
