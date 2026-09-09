"""Native connectivity audit and negative controls for V772 support nets."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_GROUND_V772.kicad_pcb'
TARGET={
 'XTAL_IN':(('U1','53'),('Y1','1'),('C1','1')),
 'XTAL_OUT':(('U1','54'),('Y1','2'),('C2','1')),
 'RSET':(('U1','51'),('R1','1')),
 'GND':(('C1','2'),('C2','2'),('R1','2')),
}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def conn(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
def check(b):
 p=pads(b)
 for net,ends in TARGET.items():
  for e in ends: assert e in p and str(p[e].GetNetname())==net,(net,e)
  reached=conn(b,p[ends[0]])|{ends[0]}
  assert all(x in reached for x in ends),(net,'disconnected')
  print(net,': PASS',ends)
def negative(net):
 b=pcbnew.LoadBoard(str(PCB)); p=pads(b); b.BuildConnectivity(); src=TARGET[net][0]; dst=TARGET[net][1]
 items=[x for x in b.GetConnectivity().GetConnectedItems(p[src]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net]
 assert items,net+' no source track'
 for item in items:
  t=pcbnew.LoadBoard(str(PCB)); victim=next((x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net and x.GetStart()==item.GetStart() and x.GetEnd()==item.GetEnd()),None)
  if victim is None: continue
  t.RemoveNative(victim); q=pads(t); reached=conn(t,q[src])|{src}
  if dst not in reached: print(net,': PASS negative control'); return
 raise AssertionError(net+' removal did not disconnect')
b=pcbnew.LoadBoard(str(PCB)); check(b)
for n in ('XTAL_IN','XTAL_OUT','RSET'):
    negative(n)
print('GND: negative control intentionally omitted; connectivity is plane-backed')
print('V772 support native connectivity and negative controls: PASS')
