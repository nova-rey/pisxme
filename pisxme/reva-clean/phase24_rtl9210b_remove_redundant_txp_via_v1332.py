"""V1332: remove the redundant TXP via at the B.Cu-only boundary."""
from pathlib import Path
import runpy
import pcbnew
H=Path(__file__).resolve().parent
runpy.run_path(str(H/'phase24_rtl9210b_txp_bcu_far_launch_v1331.py'))
src=H/'PHASE24_RTL9210B_V1058_SUPPORT_LANE_ORIGINAL_J1_V1331.kicad_pcb'
out=H/'PHASE24_RTL9210B_V1058_SUPPORT_LANE_ORIGINAL_J1_V1332.kicad_pcb'
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
    if x.GetNetname()=='LANE0_TXP' and isinstance(x,pcbnew.PCB_VIA):
        if abs(x.GetPosition().x/1e6-136.0)<.01 and abs(x.GetPosition().y/1e6-61.0)<.01: b.RemoveNative(x)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
