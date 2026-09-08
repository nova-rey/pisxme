"""V373: lane-0 transplant against direct XTAL_OUT handoff."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; dst=H/'PHASE24_RTL9210B_SUPPORT_XTALOUT_DIRECT_V372.kicad_pcb'; src=H/'PHASE24_RTL9210B_LANE0_ROUTE_V328.kicad_pcb'; out=H/'PHASE24_RTL9210B_LANE0_ON_XTALOUT_V373.kicad_pcb'
b=pcbnew.LoadBoard(str(dst)); s=pcbnew.LoadBoard(str(src))
for x in s.GetTracks():
 if x.GetNetname() in ('LANE0_TXP','LANE0_TXN','LANE0_RXP','LANE0_RXN'): b.Add(x.Duplicate())
b.BuildListOfNets(); b.Save(str(out)); print(out)
