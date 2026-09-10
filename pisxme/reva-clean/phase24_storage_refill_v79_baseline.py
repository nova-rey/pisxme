"""Re-save V79 after the same native zone refill used by route trials."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
src=R/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER.kicad_pcb'
out=R/'PHASE24_STORAGE_V79_REFILLED_BASELINE.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
