"""Saved-board native RTL_5V source/endpoint audit and negative control."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_5V_SOURCE_V1071.kicad_pcb'; ENDS=[('U1','17'),('U1','33'),('C5','1')]
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def pads(b): return {key(p):p for f in b.GetFootprints() for p in f.Pads()}
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if x.GetParentFootprint()}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert all(p[e].GetNetname()=='RTL_5V' for e in ENDS); assert set(ENDS)<=reach(b,p[ENDS[0]]); print('RTL_5V source/endpoint group PASS',ENDS)
b.BuildConnectivity(); ts=[x for x in b.GetConnectivity().GetConnectedItems(p[('C5','1')]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RTL_5V']; assert ts
for c in ts:
 t=pcbnew.LoadBoard(str(PCB)); victim=None
 for x in t.GetTracks():
  if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RTL_5V' and ((x.GetStart()==c.GetStart() and x.GetEnd()==c.GetEnd()) or (x.GetStart()==c.GetEnd() and x.GetEnd()==c.GetStart())): victim=x; break
 if victim is None: continue
 t.RemoveNative(victim); q=pads(t)
 if ('U1','17') not in reach(t,q[('C5','1')]): print('RTL_5V C5-source negative control PASS'); break
else: raise AssertionError('RTL_5V source-trace removal remained connected')
