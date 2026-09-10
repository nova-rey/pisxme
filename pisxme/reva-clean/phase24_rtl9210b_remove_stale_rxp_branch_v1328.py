"""V1328: remove the stale V1324 RXP vertical branch left by the handoff edit."""
from pathlib import Path
import runpy
import pcbnew
H=Path(__file__).resolve().parent
runpy.run_path(str(H/'phase24_rtl9210b_remove_launch_vias_v1327.py'))
src=H/'PHASE24_RTL9210B_OUTBOARD_J1_COAUTHORED_V1327.kicad_pcb'
out=H/'PHASE24_RTL9210B_OUTBOARD_J1_COAUTHORED_V1328.kicad_pcb'
b=pcbnew.LoadBoard(str(src))
for item in list(b.GetTracks()):
    if item.GetNetname()=='LANE0_RXP' and not isinstance(item,pcbnew.PCB_VIA):
        a=item.GetStart(); z=item.GetEnd(); vals=[a.x/1e6,a.y/1e6,z.x/1e6,z.y/1e6]
        if abs(vals[0]-150)<.01 and abs(vals[1]-82)<.01 and abs(vals[2]-150)<.01 and abs(vals[3]-68)<.01: b.RemoveNative(item)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
