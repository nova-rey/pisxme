"""V362: restore authoritative V342 RTL_3V3 tracks onto the V361 1V1 region."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; dst=H/'PHASE24_RTL9210B_RTL1V1_COALLOCATE_V361.kicad_pcb'; src=H/'PHASE24_RTL9210B_RTL3V3_ROUTE_V342.kicad_pcb'; out=H/'PHASE24_RTL9210B_3V3_ON_1V1_V362.kicad_pcb'
b=pcbnew.LoadBoard(str(dst)); s=pcbnew.LoadBoard(str(src))
for x in s.GetTracks():
 if x.GetNetname()=='RTL_3V3': b.Add(x.Duplicate())
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
