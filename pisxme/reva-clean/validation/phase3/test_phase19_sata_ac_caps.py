#!/usr/bin/env python3
"""Regression guard for the TUSB9261 per-conductor SATA AC network."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    text = (ROOT / 'STORAGE.kicad_sch').read_text()
    assert text.count('(symbol (lib_id "PiSXMeRevAClean:SATA_AC_CAP")') == 4
    assert text.count('property "Footprint" "PiSXMeRevAClean:C_0402_1005Metric"') == 4
    assert text.count('property "MPN" "GRM155R71C104KA88D"') == 4
    for bridge, socket in (
        ('BRIDGE_SATA_TX_P', 'SATA_M2_TX_P'),
        ('BRIDGE_SATA_TX_N', 'SATA_M2_TX_N'),
        ('BRIDGE_SATA_RX_P', 'SATA_M2_RX_P'),
        ('BRIDGE_SATA_RX_N', 'SATA_M2_RX_N'),
    ):
        assert f'label "{bridge}"' in text
        assert f'label "{socket}"' in text
    assert text.count('(symbol (lib_id "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000")') == 1
    assert text.count('property "Reference" "C30"') == 1
    assert text.count('property "Reference" "C31"') == 1
    assert text.count('property "Reference" "C32"') == 1
    assert text.count('property "Reference" "C33"') == 1
    print('Phase 19 SATA AC coupling audit: PASS; four distinct-net 0402 capacitors')


if __name__ == '__main__':
    main()
