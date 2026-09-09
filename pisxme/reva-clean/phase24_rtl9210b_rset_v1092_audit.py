"""Saved-board native RSET audit and negative control."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_RSET_V1092.kicad_pcb'; ENDS=[('U1','51'),('R1','1')]
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def pads(b): return {key(p):p for f in b.GetFootprints() for p in f.Pads()}
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if x.GetParentFootprint()}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert all(p[e].GetNetname()=='RSET' for e in ENDS); assert set(ENDS)<=reach(b,p[ENDS[0]]); print('RSET endpoint group PASS',ENDS)
b.BuildConnectivity(); ts=[x for x in b.GetConnectivity().GetConnectedItems(p[('U1','51')]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RSET']; assert ts
for c in ts:
 t=pcbnew.LoadBoard(str(PCB)); victim=None
 for x in t.GetTracks():
  if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RSET' and ((x.GetStart()==c.GetStart() and x.GetEnd()==c.GetEnd()) or (x.GetStart()==c.GetEnd() and x.GetEnd()==c.GetStart())): victim=x; break
 if victim is None: continue
 t.RemoveNative(victim); q=pads(t)
 if ('R1','1') not in reach(t,q[('U1','51')]): print('RSET source-trace negative control PASS'); break
else: raise AssertionError('RSET source-trace removal remained connected')
