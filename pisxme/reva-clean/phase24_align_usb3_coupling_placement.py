"""Align the two USB3 TX coupling capacitors to the validated local corridor."""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
base = R / os.environ.get("P24_ALIGN_BASE", "PHASE24_STORAGE_AUTHORITY_CORRECTED_SUPPORT.kicad_pcb")
out = R / os.environ.get("P24_ALIGN_OUT", "PHASE24_STORAGE_AUTHORITY_CORRECTED_SUPPORT_ALIGNED.kicad_pcb")
b = pcbnew.LoadBoard(str(base))
if b is None:
    raise SystemExit("target board load failed")
for ref, x, y in (("C86", 147.0, 145.0), ("C87", 147.0, 149.0)):
    f = b.FindFootprintByReference(ref)
    if f is None:
        raise SystemExit(f"missing {ref}")
    f.SetPosition(pcbnew.VECTOR2I_MM(x, y))
b.Save(str(out))
print(out)
