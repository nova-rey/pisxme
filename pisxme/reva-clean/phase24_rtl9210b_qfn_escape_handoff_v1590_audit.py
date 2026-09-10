"""Native endpoint and trace-removal audit for the V1590 QFN escape fixture."""
from pathlib import Path
import tempfile
import pcbnew

H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb'
NETS=('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
def key(x): return (x.GetParentFootprint().GetReference(),x.GetNumber())
def reach(b,name):
 b.BuildConnectivity(); u=next(p for p in b.FindFootprintByReference('U1').Pads() if p.GetNetname()==name)
 return {key(x) for x in b.GetConnectivity().GetConnectedItems(u) if type(x).__name__ in ('PAD','PCB_PAD')}
def assert_link(b,name): assert ('JH1',next(p.GetNumber() for p in b.FindFootprintByReference('JH1').Pads() if p.GetNetname()==name)) in reach(b,name)
b=pcbnew.LoadBoard(str(PCB))
for n in NETS: assert_link(b,n)
for n in NETS:
 bad=pcbnew.LoadBoard(str(PCB)); victim=next(q for q in bad.GetTracks() if q.GetNetname()==n); bad.RemoveNative(victim)
 with tempfile.NamedTemporaryFile(suffix='.kicad_pcb') as f:
  bad.Save(f.name); broken=pcbnew.LoadBoard(f.name)
  try: assert_link(broken,n)
  except AssertionError: continue
  raise AssertionError('negative control unexpectedly passed: '+n)
print('V1590 native six-net QFN escape connectivity PASS; six trace-removal negative controls PASS')
