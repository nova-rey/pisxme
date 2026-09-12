"""Promote four cross-sheet USB3 fanout labels to global labels.

The labels are on the existing STORAGE USB3 fanout wires. The corresponding
same-name global labels already exist on the source-side contract, so this
identity-preserving source correction removes KiCad's local/global collision
warnings without changing any symbol, wire, pin, UUID, or net name.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCHEMATIC = ROOT / "STORAGE.kicad_sch"
TARGETS = (
    ("CM5_USB3_RX_N", "171.985", "f1000000-0000-0000-0000-000000000174"),
    ("CM5_USB3_RX_P", "173.255", "f1000000-0000-0000-0000-000000000173"),
    ("CM5_USB3_TX_N", "177.065", "f1000000-0000-0000-0000-000000000170"),
    ("CM5_USB3_TX_P", "178.335", "f1000000-0000-0000-0000-00000000016f"),
)

text = SCHEMATIC.read_text()
for name, y, uuid in TARGETS:
    local = f'(label "{name}" (at 120 {y} 0) (effects (font (size 0.8 0.8)) (justify left)) (uuid {uuid}))'
    global_ = f'(global_label "{name}" (shape bidirectional) (at 120 {y} 0) (effects (font (size 0.8 0.8)) (justify left)) (uuid {uuid}))'
    if text.count(global_) == 1:
        continue
    if text.count(local) != 1:
        raise SystemExit(f"{name}: expected one local label or promoted label")
    text = text.replace(local, global_)
SCHEMATIC.write_text(text)
print("promoted four STORAGE USB3 fanout labels to global scope")
