"""Materialize the selected Ethernet macro migration as a disposable route base."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb"
OUT = ROOT / "PHASE24_SELECTED_ETH_LOCAL_MACRO.kicad_pcb"
MOVES = {"J2": (15,145,180), "U6": (20,104,-90), "U9": (26,104,-90)}
board = pcbnew.LoadBoard(str(BASE))
for ref, (x,y,r) in MOVES.items():
    f = board.FindFootprintByReference(ref)
    if f is None: raise RuntimeError(ref)
    f.SetPosition(pcbnew.VECTOR2I_MM(x,y)); f.SetOrientationDegrees(r)
removed = 0
tokens = ("CM5_GBE_", "ETH_", "GBE_")
for item in list(board.GetTracks()):
    if any(t in item.GetNetname() for t in tokens):
        board.Remove(item); removed += 1
board.Save(str(OUT))
print(f"{OUT} removed_affected_track_items={removed}")
