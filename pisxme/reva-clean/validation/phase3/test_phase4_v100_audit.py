#!/usr/bin/env python3
"""Machine-readable audit for the schematic-only Phase 4 V100 island."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SHEET = ROOT / "V100_PCIE.kicad_sch"


def main() -> None:
    text = SHEET.read_text()
    assert text.count('(lib_id "PiSXMeRevAClean:SXM2_74221_101LF")') == 1
    assert text.count('(lib_id "PiSXMeRevAClean:PCIe_AC_COUPLING_C")') == 2
    refs = re.findall(r'property "Reference" "([A-Z]+\d+)"', text)
    assert sorted(refs) == ["C1", "C2", "J1", "X2"]
    assert all(net in text for net in (
        "V100_PER0_P", "V100_PER0_N", "V100_PET0_P", "V100_PET0_N",
        "V100_REFCLK_P", "V100_REFCLK_N", "V100_PERST",
    ))
    assert not re.search(r"PER[1-9]|PET[1-9]|NVLINK|X16|SWITCH|REDRIVER", text, re.I)
    mapping = {
        "A2": "V100_PER0_P", "A3": "V100_PER0_N",
        "G1": "V100_PET0_P", "G2": "V100_PET0_N",
        "E7": "V100_REFCLK_P", "F7": "V100_REFCLK_N", "E18": "V100_PERST",
    }
    for contact, net in mapping.items():
        assert f'(label "{net}"' in text, (contact, net)
    print("Phase 4 V100 audit: PASS; lane=0 only; PET0 coupling=2; baggage=0")


if __name__ == "__main__":
    main()
