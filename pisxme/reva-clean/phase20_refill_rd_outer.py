from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
b=pcbnew.LoadBoard(str(ROOT/'PHASE20_SERVICE_RD_OUTER.kicad_pcb'))
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
out=ROOT/'PHASE20_SERVICE_RD_OUTER_REFILLED.kicad_pcb'; b.Save(str(out)); print(out)
