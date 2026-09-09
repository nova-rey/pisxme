"""V1300 native clock/RSET endpoint and source-removal audit."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_V1279_V1195_CLOCK_RSET_TRANSPLANT_V1300.kicad_pcb'
T={'RSET':(('U1','51'),('R1','1')),'XTAL_IN':(('U1','53'),('Y1','1'),('C1','1')),'XTAL_OUT':(('U1','54'),('Y1','2'),('C2','1'))}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(pad): return (pad.GetParentFootprint().GetReference(), pad.GetNumber())
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(P)); p=pads(b)
for net,ends in T.items():
 assert all(e in p and p[e].GetNetname()==net for e in ends)
 got=reach(b,p[ends[0]]); assert all(e in got or e==ends[0] for e in ends)
 print(net,'endpoint: PASS')
 for item in [x for x in b.GetConnectivity().GetConnectedItems(p[ends[0]]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net]:
  t=pcbnew.LoadBoard(str(P)); q=pads(t); victim=next((x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net and ((x.GetStart()==item.GetStart() and x.GetEnd()==item.GetEnd()) or (x.GetStart()==item.GetEnd() and x.GetEnd()==item.GetStart()))),None)
  if victim is None: continue
  t.RemoveNative(victim); assert ends[1] not in reach(t,q[ends[0]])
  print(net,'negative control: PASS'); break
 else: raise AssertionError(net+' negative control failed')
print('V1300 saved-board clock/RSET transplant audit: PASS')
