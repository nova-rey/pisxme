"""Native saved-board SPICS endpoint audit with a trace-removal control."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_ORIENTATION180_SPICS_V810.kicad_pcb'
ENDS=(('U1','24'),('U2','1'))
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert all(e in p and p[e].GetNetname()=='SPICS' for e in ENDS)
assert ENDS[1] in (reach(b,p[ENDS[0]])|{ENDS[0]}); print('SPICS endpoint: PASS',ENDS)
b.BuildConnectivity(); items=[x for x in b.GetConnectivity().GetConnectedItems(p[ENDS[0]]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='SPICS']; assert items
for item in items:
 t=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='SPICS' and ((x.GetStart()==item.GetStart() and x.GetEnd()==item.GetEnd()) or (x.GetStart()==item.GetEnd() and x.GetEnd()==item.GetStart()))); t.RemoveNative(victim); q=pads(t)
 if ENDS[1] not in (reach(t,q[ENDS[0]])|{ENDS[0]}): print('SPICS negative control: PASS'); break
else: raise AssertionError('SPICS removal did not disconnect')
