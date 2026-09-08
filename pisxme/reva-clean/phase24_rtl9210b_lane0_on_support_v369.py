"""V369: transplant current-orientation RTL9210B lane-0 primitive onto V368."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; dst=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V368.kicad_pcb'; src=H/'PHASE24_RTL9210B_LANE0_ROUTE_V328.kicad_pcb'; out=H/'PHASE24_RTL9210B_LANE0_ON_SUPPORT_V369.kicad_pcb'
b=pcbnew.LoadBoard(str(dst)); s=pcbnew.LoadBoard(str(src))
for x in s.GetTracks():
 if x.GetNetname() in ('LANE0_TXP','LANE0_TXN','LANE0_RXP','LANE0_RXN'): b.Add(x.Duplicate())
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
