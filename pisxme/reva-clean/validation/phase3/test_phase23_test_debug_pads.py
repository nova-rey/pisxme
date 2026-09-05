"""Phase 23 regression for accessible, net-connected probe pads."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PCB = ROOT / 'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'
DRC = ROOT / 'PHASE23_TEST_DEBUG_PADS_V5-drc.rpt'
EXPECTED = {
    'TP1': '/POWER_INPUT/12V_IN_A', 'TP2': '/POWER_INPUT/FUSED_12V_A',
    'TP3': '12V_PROTECTED', 'TP4': '/CORE_CM5/CM5_5V',
    'TP5': '/STORAGE/BRIDGE_3V3', 'TP6': '/REGULATORS/PG_BRIDGE_3V3',
    'TP7': '/REGULATORS/PG_BRIDGE_1V1', 'TP8': '/CORE_CM5/CM5_PERST',
    'TP9': 'POWER_GND', 'TP10': '/DEBUG/UART', 'TP11': '/DEBUG/RECOVERY',
    'TP12': '/DEBUG/POWER_PG_FAULT', 'TP13': '/DEBUG/DEBUG_GND',
}
def main():
    text, report = PCB.read_text(), DRC.read_text()
    for ref, net in EXPECTED.items():
        block = re.search(rf'\(property "Reference" "{ref}".*?(?=\n\s*\(footprint |\Z)', text, re.S)
        assert block and f'(net "{net}")' in block.group(0), (ref, net)
        assert '(pad "1" thru_hole' in block.group(0)
    for category in ('[shorting_items]', '[tracks_crossing]', '[track_width]', '[hole_clearance]', '[pth_inside_courtyard]'):
        assert category not in report, category
    assert 'In1.Cu' not in ''.join(re.findall(r'\(segment\s.*?\(layer "([^"]+)"\)', text, re.S))
    assert 'In4.Cu' not in ''.join(re.findall(r'\(segment\s.*?\(layer "([^"]+)"\)', text, re.S))
    print('Phase 23 test/debug pads: PASS')
if __name__ == '__main__': main()
