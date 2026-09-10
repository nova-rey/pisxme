"""Native saved-board audit for the V1601 staggered source breakout."""
from pathlib import Path
import tempfile
import pcbnew

H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_STAGGERED_HANDOFF_V1601.kicad_pcb'
NETS=('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
def key(x): return (x.GetParentFootprint().GetReference(),x.GetNumber())
def reach(b,name):
 b.BuildConnectivity()
 u=next(p for p in b.FindFootprintByReference('U1').Pads() if p.GetNetname()==name)
 return {key(x) for x in b.GetConnectivity().GetConnectedItems(u)
         if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB))
for name in NETS:
 hp=next(p for p in b.FindFootprintByReference('JH1').Pads() if p.GetNetname()==name)
 assert key(hp) in reach(b,name), name
for name in NETS:
 bad=pcbnew.LoadBoard(str(PCB))
 u=next(p for p in bad.FindFootprintByReference('U1').Pads() if p.GetNetname()==name)
 up=u.GetPosition()
 victims=[q for q in bad.GetTracks() if q.GetNetname()==name and (q.GetStart()==up or q.GetEnd()==up)]
 assert victims, name
 for victim in victims: bad.RemoveNative(victim)
 with tempfile.NamedTemporaryFile(suffix='.kicad_pcb') as f:
  bad.Save(f.name); broken=pcbnew.LoadBoard(f.name)
  hp=next(p for p in broken.FindFootprintByReference('JH1').Pads() if p.GetNetname()==name)
  assert key(hp) not in reach(broken,name), name
print('V1601 native six-net staggered handoff PASS; six trace-removal negative controls PASS')
