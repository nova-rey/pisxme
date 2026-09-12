"""Promote the proven ordinary STORAGE M2_GND alias normalization.

Only label records are changed; symbol pin names and PCB data are untouched.
The exact count guard prevents partial or accidental broad replacement.
"""
from pathlib import Path

path = Path(__file__).resolve().parent / "STORAGE.kicad_sch"
text = path.read_text()
needle = '(label "M2_GND"'
count = text.count(needle)
if count != 11:
    raise SystemExit(f"expected exactly 11 ordinary M2_GND labels, found {count}")
text = text.replace(needle, '(label "POWER_GND"')
path.write_text(text)
print(f"promoted {count} ordinary M2_GND labels to POWER_GND")
