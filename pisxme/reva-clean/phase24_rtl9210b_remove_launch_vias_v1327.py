"""V1327: remove only the two genuinely dangling RXP launch vias."""
from pathlib import Path
import runpy
import pcbnew
H=Path(__file__).resolve().parent
runpy.run_path(str(H/'phase24_rtl9210b_fix_rxp_launch_v1325.py'))
src=H/'PHASE24_RTL9210B_OUTBOARD_J1_COAUTHORED_V1325.kicad_pcb'
out=H/'PHASE24_RTL9210B_OUTBOARD_J1_COAUTHORED_V1327.kicad_pcb'
b=pcbnew.LoadBoard(str(src))
for item in list(b.GetTracks()):
    if item.GetNetname()=='LANE0_RXP' and isinstance(item,pcbnew.PCB_VIA):
        x=item.GetPosition().x/1e6; y=item.GetPosition().y/1e6
        if any(abs(x-a)<.01 and abs(y-c)<.01 for a,c in [(150.0,68.0),(154.25,60.0)]): b.RemoveNative(item)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
