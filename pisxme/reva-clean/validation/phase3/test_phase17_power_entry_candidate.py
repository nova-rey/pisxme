"""Focused Phase 17 regression for the reopened coherent F1 power block."""
from pathlib import Path
import re
import sys
import pcbnew

ROOT = Path(__file__).resolve().parents[2]
BOARD = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "ACREAGE_PHASE17_F1RIGHT40_ETH3.kicad_pcb"
REPORT = Path(sys.argv[2]) if len(sys.argv) > 2 else BOARD.with_name(BOARD.stem + "-drc.rpt")
b = pcbnew.LoadBoard(str(BOARD))
f1 = b.FindFootprintByReference("F1")
assert f1 is not None
assert (round(pcbnew.ToMM(f1.GetPosition().x), 3), round(pcbnew.ToMM(f1.GetPosition().y), 3)) == (240.0, 40.0)
for ref, expected in (("F1", {"/POWER_INPUT/12V_IN_A", "/POWER_INPUT/FUSED_12V_A"}),
                      ("Q1", {"/POWER_INPUT/FUSED_12V_A", "12V_PROTECTED"})):
    fp = b.FindFootprintByReference(ref)
    assert fp is not None and expected <= {p.GetNetname() for p in fp.Pads()}
report = REPORT.read_text(encoding="utf-8")
blocks = re.findall(r"\[(?:shorting_items|tracks_crossing|hole_clearance)\].*?(?=\n\[|\Z)", report, flags=re.S)
power_blocks = [x for x in blocks if "/POWER_INPUT/" in x or "F1" in x or "Q1" in x]
assert not power_blocks, "power-entry DRC defects:\n" + "\n".join(power_blocks)
for item in b.GetTracks():
    if item.GetNetname() in {"/POWER_INPUT/12V_IN_A", "/POWER_INPUT/FUSED_12V_A"}:
        assert item.GetLayer() not in (pcbnew.In1_Cu, pcbnew.In4_Cu)
print(f"Phase 17 power-entry candidate: PASS; board={BOARD.name}; report={REPORT.name}")
