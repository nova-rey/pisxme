"""Native saved-board RTL_3V3 connectivity audit and negative control."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_U2_3V3_V1063.kicad_pcb'
ENDS=[('U1','34'),('U1','39'),('U2','3'),('U2','8'),('R2','2'),('R3','2'),('C3','1')]
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def pads(b): return {key(p):p for f in b.GetFootprints() for p in f.Pads()}
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}|{key(p)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert all(p[e].GetNetname()=='RTL_3V3' for e in ENDS); assert set(ENDS)<=reach(b,p[ENDS[0]]); print('RTL_3V3 endpoint group PASS',ENDS)
b.BuildConnectivity(); tracks=[x for x in b.GetConnectivity().GetConnectedItems(p[('U1','34')]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RTL_3V3']; assert tracks
for c in tracks:
 t=pcbnew.LoadBoard(str(PCB)); victim=None
 for x in t.GetTracks():
  if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RTL_3V3' and ((x.GetStart()==c.GetStart() and x.GetEnd()==c.GetEnd()) or (x.GetStart()==c.GetEnd() and x.GetEnd()==c.GetStart())): victim=x; break
 if victim is None: continue
 t.RemoveNative(victim); q=pads(t)
 if ('C3','1') not in reach(t,q[('U1','34')]): print('RTL_3V3 source-trace negative control PASS'); break
else: raise AssertionError('source-trace removal remained connected')
