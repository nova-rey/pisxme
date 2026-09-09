"""Record the superseded Y1 clock-island net decision without editing source."""
from pathlib import Path

P = Path(__file__).resolve().parent / "STORAGE.kicad_sch"
s = P.read_text()
if '(label "BRIDGE_XI"' not in s or '(label "BRIDGE_XO"' not in s:
    raise SystemExit("legacy Y1 clock aliases not present")
print("Y1 remains superseded; live JMS583 clock authority is U11/XIN-XOUT to Y10")
