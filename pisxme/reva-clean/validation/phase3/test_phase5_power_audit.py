#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def main():
    power = (ROOT / 'POWER_INPUT.kicad_sch').read_text()
    regs = (ROOT / 'REGULATORS.kicad_sch').read_text()
    assert power.count('property "MPN" "LM74700QDBVRQ1"') == 2
    assert power.count('property "MPN" "0039300020"') == 2
    assert regs.count('property "MPN" "TPSM63606RDLR"') == 3
    assert 'property "MPN" "TUSB9261IPVP"' not in regs
    # Exact package authority must be represented, not only an MPN string.
    assert power.count('(pin "6"') >= 2 and power.count('(pin "5"') >= 2
    assert regs.count('(pin "20"') >= 3
    assert 'CSD19536KCS' in power
    assert '178.6165.0001' in power
    for net in ('12V_IN_A', '12V_IN_B', '12V_PROTECTED', 'POWER_PG_FAULT'):
        assert net in power
    for net in ('CM5_5V', 'BRIDGE_3V3', 'BRIDGE_1V1'):
        assert net in regs
    print('Phase 5 power audit: identity baseline PASS; circuit-completion gate remains open')

if __name__ == '__main__':
    main()
