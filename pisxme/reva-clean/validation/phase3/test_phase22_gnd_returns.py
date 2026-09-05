"""Phase 22 checks for plane roles, ground pours, and return-via inventory."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PCB = ROOT / 'PHASE21_CONTROLS_REGULATOR_CONTROLS_GATES.kicad_pcb'
DRC = ROOT / 'PHASE21_CONTROLS_REGULATOR_CONTROLS_GATES-drc.rpt'

def main():
    text, report = PCB.read_text(), DRC.read_text()
    assert '(zone\n\t\t(net "POWER_GND")\n\t\t(layer "In1.Cu")' in text
    assert '(zone\n\t\t(net "POWER_GND")\n\t\t(layer "In4.Cu")' in text
    segments = re.findall(r'\(segment\s.*?\(layer "([^"]+)"\)', text, re.S)
    assert not ({'In1.Cu', 'In4.Cu'} & set(segments))
    gnd_vias = len(re.findall(r'\(via\s(?:(?!\n\t\t\(via).)*?\(net "POWER_GND"\)', text, re.S))
    assert gnd_vias >= 12, gnd_vias
    assert '[shorting_items]' not in report and '[tracks_crossing]' not in report
    print(f'Phase 22 GND/returns/zones: PASS ({gnd_vias} dedicated POWER_GND vias)')

if __name__ == '__main__': main()
