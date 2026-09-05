from pathlib import Path
import pcbnew
root=Path(__file__).resolve().parent
b=pcbnew.LoadBoard(str(root/'PHASE21_CONTROLS_FB3V3.kicad_pcb'))
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
out=root/'PHASE21_CONTROLS_FB3V3_REFILLED.kicad_pcb'; b.Save(str(out)); print(out)
