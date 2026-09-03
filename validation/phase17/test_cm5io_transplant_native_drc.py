"""Reject true native DRC errors in the complete CM5IO transplant fixture."""
from pathlib import Path
import os

report = Path(os.environ.get(
    "PISXME_ETHERNET_DRC",
    "/home/nyx/PiSXMe/pisxme/reva-clean/CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE-drc.rpt",
))
text = report.read_text()
for marker in ("[shorting_items]", "[tracks_crossing]", "[hole_clearance]",
               "[via_dangling]", "[unconnected_items]", "[invalid_outline]",
               "[silk_over_copper]"):
    assert marker not in text, f"true native DRC failure remains: {marker}"
assert "** Found 0 unconnected pads **" in text
assert "** Found 0 Footprint errors **" in text
print("CM5IO transplant native DRC regression: PASS (warnings only)")
