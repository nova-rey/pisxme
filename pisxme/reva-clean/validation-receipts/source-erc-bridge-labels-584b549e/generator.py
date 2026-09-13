"""Promote two proven STORAGE bridge USB fanout labels to global scope.

The labels are on existing BRIDGE_USB_DP/DM wires and the same names already
exist as global contract labels in this child sheet. Exact coordinates and
UUIDs are guarded so this cannot become a broad label rewrite. Symbols, wires,
pins, coordinates, net names, and PCB files remain untouched.
"""
from pathlib import Path

SCHEMATIC = Path(__file__).resolve().parent / "STORAGE.kicad_sch"
TARGETS = (
    ("BRIDGE_USB_DP", "152.935", "f1000000-0000-0000-0000-000000000183"),
    ("BRIDGE_USB_DM", "151.665", "f1000000-0000-0000-0000-000000000184"),
)
text = SCHEMATIC.read_text(encoding="utf-8")
for name, y, uuid in TARGETS:
    local = f'(label "{name}" (at 120 {y} 0) (effects (font (size 0.8 0.8)) (justify left)) (uuid {uuid}))'
    global_ = f'(global_label "{name}" (shape bidirectional) (at 120 {y} 0) (effects (font (size 0.8 0.8)) (justify left)) (uuid {uuid}))'
    if text.count(global_) == 1:
        continue
    if text.count(local) != 1:
        raise SystemExit(f"{name}: expected one exact local label")
    text = text.replace(local, global_)
SCHEMATIC.write_text(text, encoding="utf-8")
print("promoted two STORAGE bridge USB labels to global scope")
