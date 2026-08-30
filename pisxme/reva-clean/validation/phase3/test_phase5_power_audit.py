#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def main():
    power = (ROOT / 'POWER_INPUT.kicad_sch').read_text()
    regs = (ROOT / 'REGULATORS.kicad_sch').read_text()
    assert power.count('property "MPN" "LM74700QDBVRQ1"') == 2
    assert regs.count('property "MPN" "TPSM63606RDLR"') == 1
    assert regs.count('property "MPN" "TUSB9261IPVP"') == 2
    for net in ('12V_IN_A', '12V_IN_B', '12V_PROTECTED', 'POWER_PG_FAULT'):
        assert net in power
    for net in ('CM5_5V', 'BRIDGE_3V3', 'BRIDGE_1V1'):
        assert net in regs
    print('Phase 5 power audit: PASS; dual inputs, protected merge, and three required rails')

if __name__ == '__main__':
    main()
