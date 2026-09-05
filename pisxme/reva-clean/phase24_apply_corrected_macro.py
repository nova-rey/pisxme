"""Materialize the corrected, collision-screened Phase 24 macro basis.

This creates a disposable routing base from the live integrated candidate. It
moves complete Ethernet and storage neighborhoods and removes only copper
whose endpoints are invalidated by those moves; it does not create copper or
invent connectivity.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb"
OUT = ROOT / "PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb"

MOVES = {
    # Ethernet: clear the west power-entry bodies while retaining the CM5IO
    # source/ESD/connector functional neighborhood.
    "J2": (15, 145, 180), "U6": (20, 104, -90), "U9": (26, 104, -90),
    # Storage: move bridge, connector, AC coupling, clock, and local support
    # as one coherent island; C17 is included because it was previously left
    # behind and collided with the moved bridge.
    "U7": (105, 124, 180), "J3": (145, 125, 90), "C16": (95, 112, 0),
    "C17": (101, 112, 0), "C19": (107, 112, 0),
    "C30": (113, 116, 180), "C31": (113, 132, 180),
    "C32": (119, 116, 180), "C33": (119, 132, 180),
    "Y1": (95, 140, 0), "R23": (89, 140, 0),
    "C42": (89, 136, 0), "C43": (89, 144, 0),
}

affected = (
    "CM5_GBE_", "ETH_", "GBE_", "CM5_USB3_", "BRIDGE_USB3_",
    "BRIDGE_SATA_", "SATA_M2_", "BRIDGE_XI", "BRIDGE_XO",
    "BRIDGE_3V3", "/REGULATORS/BRIDGE_1V1",
    "BRIDGE_VSSOSC", "/STORAGE/", "/CLOCK/",
)

board = pcbnew.LoadBoard(str(BASE))
for ref, (x, y, rotation) in MOVES.items():
    fp = board.FindFootprintByReference(ref)
    if fp is None:
        raise RuntimeError(f"missing required moved footprint {ref}")
    fp.SetPosition(pcbnew.VECTOR2I_MM(x, y))
    fp.SetOrientationDegrees(rotation)

removed = 0
for item in list(board.GetTracks()):
    if any(token in item.GetNetname() for token in affected):
        board.Remove(item)
        removed += 1

board.Save(str(OUT))
print(f"{OUT} removed_affected_track_items={removed}")
