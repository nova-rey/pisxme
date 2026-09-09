"""Correct U12's selector control to the shared STORAGE_SEL authority."""
from pathlib import Path

SCH = Path(__file__).resolve().parent / "STORAGE.kicad_sch"
old = '(label "USB_SEL" (at 120 180.875 0)'
new = '(label "STORAGE_SEL" (at 120 180.875 0)'
text = SCH.read_text()
count = text.count(old)
if count != 1:
    raise SystemExit(f"expected one U12 pin-9 selector label, found {count}")
SCH.write_text(text.replace(old, new))
print("mapped serialized U12 pin-9 label to STORAGE_SEL")
