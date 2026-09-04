"""Scoped Phase 17 Ethernet electrical regression for disposable ancestors.

This deliberately does not replace native DRC: it separates Ethernet
connectivity/layer evidence from inherited acreage scaffold findings.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
BOARD = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "ACREAGE_PHASE17_TI_U3_F1_ETH_60_165AC_CT1F.kicad_pcb"
REPORT = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "ACREAGE_PHASE17_TI_U3_F1_ETH_60_165AC_CT1F-drc.rpt"

text = BOARD.read_text(encoding="utf-8")
report = REPORT.read_text(encoding="utf-8")
required = {
    "CM5_GBE_TD0_P", "CM5_GBE_TD0_N", "CM5_GBE_TD1_P", "CM5_GBE_TD1_N",
    "CM5_GBE_TD2_P", "CM5_GBE_TD2_N", "CM5_GBE_TD3_P", "CM5_GBE_TD3_N",
    "/ETHERNET/ETH_CT1", "/ETHERNET/ETH_CT2", "/ETHERNET/ETH_CT3",
    "/ETHERNET/ETH_CT4", "ETH_CT_COMMON", "/ETHERNET/GBE_SHIELD",
    "POWER_GND",
}
missing = sorted(net for net in required if net not in text)
assert not missing, f"missing Ethernet nets: {missing}"

assert "[shorting_items]" not in report, "native DRC reports a true short"
assert "[tracks_crossing]" not in report, "native DRC reports a track crossing"

for block in re.findall(r"\[unconnected_items\].*?(?=\n\[|\Z)", report, flags=re.S):
    assert not re.search(r"ETH|GBE|CM5_GBE", block), f"Ethernet unconnected record: {block[:240]}"

for line in text.splitlines():
    if "(net \"" in line and any(net.strip("/") in line for net in required):
        assert '"In1.Cu"' not in line and '"In4.Cu"' not in line

print(f"Phase 17 scoped Ethernet electrical regression: PASS; board={BOARD.name}; report={REPORT.name}")
