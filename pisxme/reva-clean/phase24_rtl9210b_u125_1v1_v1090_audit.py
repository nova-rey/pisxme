"""Saved-board native RTL_1V1 audit for V1090."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_U125_1V1_V1090.kicad_pcb'; ENDS=[('U1','16'),('U1','25'),('U1','36'),('U1','40'),('U1','50'),('U1','55'),('U1','60'),('U1','63'),('C4','1')]
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def pads(b): return {key(p):p for f in b.GetFootprints() for p in f.Pads()}
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if x.GetParentFootprint()}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert all(p[e].GetNetname()=='RTL_1V1' for e in ENDS); assert set(ENDS)<=reach(b,p[ENDS[0]]); print('RTL_1V1 complete endpoint group PASS',ENDS)
b.BuildConnectivity(); ts=[x for x in b.GetConnectivity().GetConnectedItems(p[('U1','25')]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RTL_1V1']; assert ts
for c in ts:
 t=pcbnew.LoadBoard(str(PCB)); victim=None
 for x in t.GetTracks():
  if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RTL_1V1' and ((x.GetStart()==c.GetStart() and x.GetEnd()==c.GetEnd()) or (x.GetStart()==c.GetEnd() and x.GetEnd()==c.GetStart())): victim=x; break
 if victim is None: continue
 t.RemoveNative(victim); q=pads(t)
 if ('C4','1') not in reach(t,q[('U1','25')]): print('RTL_1V1 U1.25 source-trace negative control PASS'); break
else: raise AssertionError('RTL_1V1 U1.25 source-trace removal remained connected')
