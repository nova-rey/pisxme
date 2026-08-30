#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]

def main():
    calculations = subprocess.run([
        'python3', str(ROOT / 'validation/phase3/phase14_power_calculations.py')
    ], capture_output=True, text=True, check=False)
    assert calculations.returncode == 0, calculations.stdout + calculations.stderr
    power = (ROOT / 'POWER_INPUT.kicad_sch').read_text()
    regs = (ROOT / 'REGULATORS.kicad_sch').read_text()
    assert power.count('property "MPN" "LM74700QDBVRQ1"') == 2
    assert power.count('property "MPN" "0039300020"') == 2
    assert regs.count('property "MPN" "TPSM63606RDLR"') == 3
    assert regs.count('property "MPN" "C3225X7R1C226M250AC"') >= 16
    assert regs.count('property "MPN" "C3216X7R1H106K160AC"') >= 6
    assert 'property "Value" "10uF 50V"' in regs
    assert regs.count('property "Reference" "C19"') == 1
    assert 'property "Reference" "R21"' in regs and 'property "Value" "2k"' in regs
    assert regs.count('property "Reference" "C') >= 29
    assert 'property "MPN" "TUSB9261IPVP"' not in regs
    # Exact package authority must be represented, not only an MPN string.
    assert power.count('(pin "6"') >= 2 and power.count('(pin "5"') >= 2
    assert regs.count('(pin "20"') >= 3
    for pin_name in ('VIN1', 'VIN2', 'CBOOT', 'RBOOT', 'VLDOIN', 'VOUT1',
                     'VOUT2', 'FB', 'RT', 'PG', 'EN/SYNC', 'PGND'):
        assert pin_name in regs
    assert 'CSD19536KCS' in power
    assert '178.6165.0001' in power
    assert power.count('property "MPN" "SMBJ18A"') == 2
    assert 'TVS_SMBJ18A_DO214AA' in power
    for net in ('12V_IN_A', '12V_IN_B', '12V_PROTECTED', 'POWER_PG_FAULT'):
        assert net in power
    for net in ('CM5_5V', 'BRIDGE_3V3', 'BRIDGE_1V1'):
        assert net in regs
    with tempfile.TemporaryDirectory(prefix='phase5-netlist-', dir=ROOT) as tmp:
        out = Path(tmp) / 'power.xml'
        result = subprocess.run([
            'xvfb-run', '-a', 'kicad-cli', 'sch', 'export', 'netlist',
            '--format', 'kicadxml', '--output', out.name,
            str(ROOT / 'PiSXMe_RevA_Clean.kicad_sch')],
            cwd=tmp, capture_output=True, text=True, check=False)
        assert result.returncode == 0, result.stderr
        nets = {}
        for net in ET.parse(out).getroot().find('nets'):
            nets[net.attrib['name']] = {
                (node.attrib.get('ref'), node.attrib.get('pin'))
                for node in net.findall('node')
            }
        assert {('J5', '1'), ('F1', '1')} <= nets['/POWER_INPUT/12V_IN_A']
        assert {('J6', '1'), ('F2', '1')} <= nets['/POWER_INPUT/12V_IN_B']
        assert {('Q1', '1'), ('U1', '6')} <= nets['/POWER_INPUT/FUSED_12V_A']
        assert {('Q2', '1'), ('U2', '6')} <= nets['/POWER_INPUT/FUSED_12V_B']
        # J1.A3 is the PCIe lane-negative signal.  The abstract connector's
        # power authority is J1.PWR; the materializer expands that one
        # logical pin onto the documented Rev-A empirical power rows.
        protected = next(nodes for nodes in nets.values() if ('J1', 'PWR') in nodes)
        assert {('J1', 'PWR'), ('Q1', '2'), ('Q2', '2')} <= protected
        shared_ground = nets['POWER_GND']
        assert {('J1', 'GND'), ('U1', '2'), ('U2', '2'),
                ('J5', '2'), ('J6', '2')} <= shared_ground
        assert {('U3', '10'), ('R3', '2'), ('R4', '1')} <= nets['/REGULATORS/FB_CM5_5V']
        assert {('U4', '10'), ('R11', '2'), ('R12', '1')} <= nets['/REGULATORS/FB_BRIDGE_3V3']
        assert {('U5', '10'), ('R19', '2'), ('R20', '1')} <= nets['/REGULATORS/FB_BRIDGE_1V1']
        assert {('U3', '13'), ('R6', '2')} <= nets['/REGULATORS/PG_CM5_5V']
        assert {('U4', '13'), ('R14', '2')} <= nets['/REGULATORS/PG_BRIDGE_3V3']
        assert {('U5', '13'), ('R22', '2')} <= nets['/REGULATORS/PG_BRIDGE_1V1']
        assert {('C3', '1'), ('U1', '1')} <= nets['/POWER_INPUT/VCAP_A']
        assert {('C4', '1'), ('U2', '1')} <= nets['/POWER_INPUT/VCAP_B']
        assert {('C5', '1'), ('C6', '1'), ('C14', '1'), ('C15', '1')} <= next(
            nodes for name, nodes in nets.items() if '12V_PROTECTED' in name)
        assert not any('12V' in name and 'M2' in name for name in nets)
    print('Phase 5 power audit: schematic connectivity and design-envelope calculations PASS; residual physical risk recorded')

if __name__ == '__main__':
    main()
