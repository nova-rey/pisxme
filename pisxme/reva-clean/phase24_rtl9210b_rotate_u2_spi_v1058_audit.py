"""Saved-board native SPI endpoint and source-track negative controls (V1058)."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_ROTATE_U2_SPI_V1058.kicad_pcb'
TARGET={'SPISI':(('U1','18'),('U2','5')),'SPICLK':(('U1','19'),('U2','6')),
        'SPISO3':(('U1','22'),('U2','7')),'SPISO':(('U1','23'),('U2','2')),
        'SPICS':(('U1','24'),('U2','1'))}
def key(x): return (x.GetParentFootprint().GetReference(),x.GetNumber())
def pads(b): return {key(p):p for f in b.GetFootprints() for p in f.Pads()}
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}|{key(p)}
def disconnects(path,net,src,dst):
 b=pcbnew.LoadBoard(str(path)); p=pads(b); b.BuildConnectivity();
 candidates=[x for x in b.GetConnectivity().GetConnectedItems(p[src]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net]
 assert candidates, f'{net}: no source track'
 for c in candidates:
  t=pcbnew.LoadBoard(str(path)); victim=None
  for x in t.GetTracks():
   if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net and ((x.GetStart()==c.GetStart() and x.GetEnd()==c.GetEnd()) or (x.GetStart()==c.GetEnd() and x.GetEnd()==c.GetStart())):
    victim=x; break
  if victim is None: continue
  t.RemoveNative(victim); q=pads(t)
  if dst not in reach(t,q[src]): return
 raise AssertionError(f'{net}: tested source-trace removal did not disconnect')
b=pcbnew.LoadBoard(str(PCB)); p=pads(b)
for net,(src,dst) in TARGET.items():
 assert p[src].GetNetname()==net and p[dst].GetNetname()==net
 assert dst in reach(b,p[src]); disconnects(PCB,net,src,dst); print(net,'PASS endpoint + negative control')
print('V1058 rotated-U2 SPI native connectivity and negative controls: PASS')
