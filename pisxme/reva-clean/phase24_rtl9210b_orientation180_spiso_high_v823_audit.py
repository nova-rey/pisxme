"""Saved-board connectivity audit for the V823 SPI source pair."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_ORIENTATION180_SPISO_HIGH_V823.kicad_pcb'
PAIRS={'SPICS':(('U1','24'),('U2','1')),'SPISO':(('U1','23'),('U2','2'))}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
for net, ends in PAIRS.items():
 b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert all(e in p and p[e].GetNetname()==net for e in ends)
 assert ends[1] in (reach(b,p[ends[0]])|{ends[0]}); print(net,'endpoint: PASS',ends)
 b.BuildConnectivity(); items=[x for x in b.GetConnectivity().GetConnectedItems(p[ends[0]]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net]; assert items
 for item in items:
  t=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net and ((x.GetStart()==item.GetStart() and x.GetEnd()==item.GetEnd()) or (x.GetStart()==item.GetEnd() and x.GetEnd()==item.GetStart()))); t.RemoveNative(victim); q=pads(t)
  if ends[1] not in (reach(t,q[ends[0]])|{ends[0]}): print(net,'negative control: PASS'); break
 else: raise AssertionError(net+' removal did not disconnect')
