"""Native saved-board audit for V808 control and PERST paths."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_ORIENTATION180_CONTROLS_V808.kicad_pcb'
TARGET={'PEDET':(('U1','8'),('R2','1')),'CLKREQ_N':(('U1','13'),('R3','1')),'PERST_N':(('U1','14'),('J1','50'))}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,pad):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(pad) if type(x).__name__ in ('PAD','PCB_PAD')}
def check(b):
 p=pads(b)
 for net,ends in TARGET.items():
  assert all(e in p and p[e].GetNetname()==net for e in ends),(net,ends)
  r=reach(b,p[ends[0]])|{ends[0]}; assert all(e in r for e in ends),(net,'disconnected')
  print(net,': PASS',ends)
def negative(net):
 b=pcbnew.LoadBoard(str(PCB)); p=pads(b); b.BuildConnectivity(); src,dst=TARGET[net]
 items=[x for x in b.GetConnectivity().GetConnectedItems(p[src]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net]
 assert items,net+' no track'
 for item in items:
  t=pcbnew.LoadBoard(str(PCB)); victim=next((x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net and x.GetStart()==item.GetStart() and x.GetEnd()==item.GetEnd()),None)
  if victim is None: continue
  t.RemoveNative(victim); q=pads(t); r=reach(t,q[src])|{src}
  if dst not in r: print(net,': PASS negative control'); return
 raise AssertionError(net+' removal did not disconnect')
b=pcbnew.LoadBoard(str(PCB)); check(b)
for net in TARGET: negative(net)
print('V808 native control/PERST connectivity and negative controls: PASS')
