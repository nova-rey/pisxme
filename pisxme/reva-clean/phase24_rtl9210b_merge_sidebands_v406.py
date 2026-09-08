"""V406: import the native V311 sideband routes onto the V404 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_XTALIN_ENDPOINT_V404.kicad_pcb'; srcp=H/'PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb'; out=H/'PHASE24_RTL9210B_MERGE_SIDEBANDS_V406.kicad_pcb'
b=pcbnew.LoadBoard(str(base)); s=pcbnew.LoadBoard(str(srcp)); wanted={'PEDET','CLKREQ_N','PERST_N','REFCLK_P','REFCLK_N'}
for x in s.GetTracks():
    if x.GetNetname() in wanted: b.Add(x.Duplicate())
b.BuildListOfNets(); b.Save(str(out)); print(out)
