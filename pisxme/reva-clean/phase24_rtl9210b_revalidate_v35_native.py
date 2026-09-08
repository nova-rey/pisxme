"""Re-save V35 after native zone refill for a current DRC receipt."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35.kicad_pcb'
out=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
