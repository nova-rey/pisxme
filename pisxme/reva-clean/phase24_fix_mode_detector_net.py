"""Route M.2 contact 69 into the documented AUTO strap net."""
from pathlib import Path

SCH = Path(__file__).resolve().parent / "STORAGE.kicad_sch"
old = '(label "M2_PEDET" (at 240 125.63 0)'
new = '(label "AUTO_PEDET" (at 240 125.63 0)'
text = SCH.read_text()
count = text.count(old)
if count != 2:
    raise SystemExit(f"expected two serialized J3 contact-69 labels, found {count}")
SCH.write_text(text.replace(old, new))
print("mapped both serialized J3 contact-69 labels to AUTO_PEDET")
