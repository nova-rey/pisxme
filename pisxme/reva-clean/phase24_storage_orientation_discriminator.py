"""Generate native placement-only storage orientation candidates."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE.kicad_pcb"

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))

variants = {
    "U7_180_J3_90": {"U7": (96,124,180), "J3": (138,124,90)},
    "U7_0_J3_270": {"U7": (96,124,0), "J3": (145,125,270)},
    "U7_270_J3_270": {"U7": (96,124,270), "J3": (145,125,270)},
}
affected = ("CM5_USB3_", "BRIDGE_SATA_", "SATA_M2_", "BRIDGE_XI", "BRIDGE_XO", "BRIDGE_VSSOSC")

for name, moves in variants.items():
    b = pcbnew.LoadBoard(str(BASE))
    for ref, (x, y, rot) in moves.items():
        f = b.FindFootprintByReference(ref)
        if f is None: raise RuntimeError(f"missing {ref}")
        f.SetPosition(V(x, y)); f.SetOrientationDegrees(rot)
    for item in list(b.GetTracks()):
        if any(token in item.GetNetname() for token in affected):
            b.RemoveNative(item)
    out = ROOT / f"PHASE24_STORAGE_ORIENTATION_{name}.kicad_pcb"
    b.Save(str(out)); print(out)
