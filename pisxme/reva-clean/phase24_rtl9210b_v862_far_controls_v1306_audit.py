"""V1306 native far-control endpoint and source-removal audit."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_V862_FAR_CONTROLS_V1306.kicad_pcb'
G={'PEDET':(('U1','8'),('R2','1'),('J1','69')),'CLKREQ_N':(('U1','13'),('R3','1'),('J1','52'))}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p): b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(P)); p=pads(b)
for net,e in G.items():
 assert all(x in p and p[x].GetNetname()==net for x in e); assert all(x in (reach(b,p[e[0]])|{e[0]}) for x in e); print(net,'endpoint: PASS')
 for item in [x for x in b.GetConnectivity().GetConnectedItems(p[e[0]]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net]:
  t=pcbnew.LoadBoard(str(P)); q=pads(t); v=next((x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net and ((x.GetStart()==item.GetStart() and x.GetEnd()==item.GetEnd()) or (x.GetStart()==item.GetEnd() and x.GetEnd()==item.GetStart()))),None)
  if v is None: continue
  t.RemoveNative(v); assert e[-1] not in (reach(t,q[e[0]])|{e[0]}); print(net,'negative control: PASS'); break
 else: raise AssertionError(net+' negative control failed')
