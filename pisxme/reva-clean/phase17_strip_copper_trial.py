"""Create a disposable footprint/zone-only board for local re-authoring."""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_BASE", ROOT / "ACREAGE_BOUNDARY_CORRECTED.kicad_pcb"))
OUT = Path(os.environ.get("PISXME_OUT", ROOT / "ACREAGE_BOUNDARY_NO_COPPER.kicad_pcb"))

board = pcbnew.LoadBoard(str(BASE))
for item in list(board.GetTracks()):
    board.Remove(item)
board.Save(str(OUT))
print(f"saved {OUT}; removed all track/via items")
