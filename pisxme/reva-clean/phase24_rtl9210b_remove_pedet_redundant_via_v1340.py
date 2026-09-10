"""V1340: remove redundant PEDET via from the continuous B.Cu run."""
from pathlib import Path
import runpy
import pcbnew
H=Path(__file__).resolve().parent
runpy.run_path(str(H/'phase24_rtl9210b_pedet_bcu_then_fcu_v1339.py'))
src=H/'PHASE24_RTL9210B_PEDET_BCU_THEN_FCU_V1339.kicad_pcb'
out=H/'PHASE24_RTL9210B_PEDET_BCU_THEN_FCU_V1340.kicad_pcb'
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
    if x.GetNetname()=='PEDET' and isinstance(x,pcbnew.PCB_VIA):
        if abs(x.GetPosition().x/1e6-125)<.01 and abs(x.GetPosition().y/1e6-80)<.01: b.RemoveNative(x)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
