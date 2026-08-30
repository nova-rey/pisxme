from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

def main() -> None:
    sch = (ROOT / 'ETHERNET.kicad_sch').read_text()
    definition = sch[sch.index('(symbol "PiSXMeRevAClean:TPD4E004DRYR"'):]
    definition = definition[:definition.index('(embedded_fonts no)')]
    assert len(re.findall(r'\(pin passive line', definition)) == 6
    instance = sch[sch.index('(property "MPN" "TPD4E004DRYR"'):]
    instance = instance[:instance.index('(instances')]
    assert instance.count('(pin "') == 6
    assert 'ETH_POWER' in sch and 'ETH_GND' in sch
    assert sch.count('property "MPN" "TPD4E004DRYR"') == 2
    assert (ROOT / 'PiSXMe_RevA_Clean.pretty/TPD4E004DRYR_WSON6.kicad_mod').read_text().count('(pad "') == 6
    print('Phase 14 Ethernet ESD authority: PASS; TI DRY=6 pins; four I/O plus VCC/GND')

if __name__ == '__main__':
    main()
