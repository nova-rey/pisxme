"""Focused Phase 21 regression for the coordinated low-speed candidate."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PCB = ROOT / 'PHASE21_CONTROLS_REGULATOR_CONTROLS_GATES.kicad_pcb'
DRC = ROOT / 'PHASE21_CONTROLS_REGULATOR_CONTROLS_GATES-drc.rpt'
REQUIRED = {
    '/POWER_INPUT/GATE_A': {'Q1.3', 'U1.5'}, '/POWER_INPUT/GATE_B': {'Q2.3', 'U2.5'},
    '/POWER_INPUT/VCAP_A': {'C3.1', 'U1.1'}, '/POWER_INPUT/VCAP_B': {'C4.1', 'U2.1'},
    '/REGULATORS/FB_BRIDGE_1V1': {'R19.2', 'R20.1', 'U5.10'},
    '/REGULATORS/FB_BRIDGE_3V3': {'C18.1', 'R11.2', 'R12.1', 'U4.10'},
    '/REGULATORS/RT_BRIDGE_1V1': {'R21.1', 'U5.12'}, '/REGULATORS/RT_BRIDGE_3V3': {'R13.1', 'U4.12'},
    '/REGULATORS/PG_BRIDGE_1V1': {'R22.2', 'U5.13'}, '/REGULATORS/PG_BRIDGE_3V3': {'R14.2', 'U4.13'},
    '/STORAGE/BRIDGE_RESET': {'U7.2', 'U7.4'},
}
def main():
    text, report = PCB.read_text(), DRC.read_text()
    assert PCB.exists() and DRC.exists()
    for net, pins in REQUIRED.items():
        assert net in text, net
        for pin in pins:
            ref, pad = pin.split('.')
            assert re.search(rf'\(property "Reference" "{re.escape(ref)}".*?\n\s*\(pad "{re.escape(pad)}".*?\(net "{re.escape(net)}"', text, re.S), f'{net} {pin}'
    for category in ('[shorting_items]', '[tracks_crossing]', '[track_width]', '[pth_inside_courtyard]'):
        assert category not in report, category
    segment_layers = re.findall(r'\(segment\s.*?\(layer "([^"]+)"\)', text, re.S)
    assert not ({'In1.Cu', 'In4.Cu'} & set(segment_layers))
    print('Phase 21 coordinated control candidate: PASS')
if __name__ == '__main__': main()
