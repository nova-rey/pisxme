"""V1302 saved-board RSET audit with trace-removal negative control."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RSET_FCU_DOGLEG_V1302.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p): b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(P)); p=pads(b); assert ('R1','1') in (reach(b,p[('U1','51')])|{('U1','51')}); print('RSET endpoint: PASS')
for item in [x for x in b.GetConnectivity().GetConnectedItems(p[('U1','51')]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RSET']:
 t=pcbnew.LoadBoard(str(P)); q=pads(t); victim=next((x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RSET' and ((x.GetStart()==item.GetStart() and x.GetEnd()==item.GetEnd()) or (x.GetStart()==item.GetEnd() and x.GetEnd()==item.GetStart()))),None)
 if victim is None: continue
 t.RemoveNative(victim); assert ('R1','1') not in (reach(t,q[('U1','51')])|{('U1','51')}); print('RSET negative control: PASS'); break
else: raise AssertionError('negative control failed')
