"""V405: transplant the native V364 RTL_1V1 support network onto V404."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_XTALIN_ENDPOINT_V404.kicad_pcb'; srcp=H/'PHASE24_RTL9210B_1V1_3V3_COALLOCATE_V364.kicad_pcb'; out=H/'PHASE24_RTL9210B_MERGE_1V1_V405.kicad_pcb'
b=pcbnew.LoadBoard(str(base)); s=pcbnew.LoadBoard(str(srcp))
for x in s.GetTracks():
    if x.GetNetname()=='RTL_1V1': b.Add(x.Duplicate())
b.BuildListOfNets(); b.Save(str(out)); print(out)
