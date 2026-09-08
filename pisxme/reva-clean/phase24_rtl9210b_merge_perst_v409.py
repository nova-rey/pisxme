"""V409: import only the native V311 PERST_N route onto V404."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_XTALIN_ENDPOINT_V404.kicad_pcb'; srcp=H/'PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb'; out=H/'PHASE24_RTL9210B_MERGE_PERST_V409.kicad_pcb'
b=pcbnew.LoadBoard(str(base)); s=pcbnew.LoadBoard(str(srcp))
for x in s.GetTracks():
    if x.GetNetname()=='PERST_N': b.Add(x.Duplicate())
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
