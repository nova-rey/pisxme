"""Saved-board control connectivity audit and negative controls for V837."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_V772_CONTROL_INBOARD_MONOTONIC_V837.kicad_pcb'
TARGET={'PEDET':(('U1','8'),('R2','1')),'CLKREQ_N':(('U1','13'),('R3','1'))}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
for net,ends in TARGET.items():
 b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert all(e in p and p[e].GetNetname()==net for e in ends)
 assert ends[1] in (reach(b,p[ends[0]])|{ends[0]}); print(net,'endpoint: PASS')
 b.BuildConnectivity(); items=[x for x in b.GetConnectivity().GetConnectedItems(p[ends[0]]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net]; assert items
 for item in items:
  t=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net and x.GetStart()==item.GetStart() and x.GetEnd()==item.GetEnd()); t.RemoveNative(victim); q=pads(t)
  if ends[1] not in (reach(t,q[ends[0]])|{ends[0]}): print(net,'negative control: PASS'); break
 else: raise AssertionError(net+' negative control failed')
