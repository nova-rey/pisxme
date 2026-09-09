"""Re-run V772 support authority on the V857 saved board."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_V772_PERST_STRAIGHT_RIGHT_V857.kicad_pcb'
TARGET={'XTAL_IN':(('U1','53'),('Y1','1'),('C1','1')),
 'XTAL_OUT':(('U1','54'),('Y1','2'),('C2','1')),
 'RSET':(('U1','51'),('R1','1')),
 'GND':(('C1','2'),('C2','2'),('R1','2'))}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
def negative(net,src,dst,p):
 b=pcbnew.LoadBoard(str(PCB)); pp=pads(b); b.BuildConnectivity(); items=[x for x in b.GetConnectivity().GetConnectedItems(pp[src]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net]; assert items
 for item in items:
  t=pcbnew.LoadBoard(str(PCB)); victim=next((x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net and ((x.GetStart()==item.GetStart() and x.GetEnd()==item.GetEnd()) or (x.GetStart()==item.GetEnd() and x.GetEnd()==item.GetStart()))),None)
  if victim is None: continue
  t.RemoveNative(victim); q=pads(t)
  if dst not in (reach(t,q[src])|{src}): print(net,'negative control: PASS'); return
 raise AssertionError(net+' negative control failed')
b=pcbnew.LoadBoard(str(PCB)); p=pads(b)
for net,ends in TARGET.items():
 for e in ends: assert e in p and p[e].GetNetname()==net,(net,e)
 assert all(e in (reach(b,p[ends[0]])|{ends[0]}) for e in ends); print(net,'endpoint: PASS')
for net in ('XTAL_IN','XTAL_OUT','RSET'):
 negative(net,TARGET[net][0],TARGET[net][1],p)
print('GND negative control: intentionally omitted; plane-backed')
print('V857 support audit: PASS')
