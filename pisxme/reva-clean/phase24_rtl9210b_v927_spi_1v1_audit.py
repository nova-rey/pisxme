"""Native saved-board audit for V927 SPI plus RTL_1V1; edges come only from PCB geometry."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb'
EXPECTED={'SPICS':(('U1','24'),('U2','1')),'SPICLK':(('U1','19'),('U2','6')),
 'SPISO3':(('U1','22'),('U2','7')),'SPISO':(('U1','23'),('U2','2')),
 'SPISI':(('U1','18'),('U2','5')),'RTL_1V1':(('U1','25'),('C4','1'))}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
def touching_source(b,p):
 q=p.GetPosition()
 for t in b.GetTracks():
  if t.GetNetname()==p.GetNetname() and (t.GetStart()==q or t.GetEnd()==q): return t
 raise AssertionError(f'no source track for {p.GetNetname()}')
def check(path):
 b=pcbnew.LoadBoard(str(path)); ps=pads(b)
 for net, ends in EXPECTED.items():
  assert all(e in ps and ps[e].GetNetname()==net for e in ends), (net,ends)
  assert all(e in (reach(b,ps[ends[0]])|{ends[0]}) for e in ends), net
 print('V927 six-net SPI/RTL_1V1 connectivity: PASS')
 for net, ends in EXPECTED.items():
  b=pcbnew.LoadBoard(str(path)); ps=pads(b); victim=touching_source(b,ps[ends[0]])
  b.RemoveNative(victim)
  assert ends[1] not in (reach(b,ps[ends[0]])|{ends[0]}), net
 print('V927 six source-trace negative controls: PASS')
check(PCB)
