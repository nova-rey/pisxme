"""Migrate the Ethernet ESD instance to TI TPD4E004's six-pin contract."""
from pathlib import Path
import re
from phase3_scaffold import balanced
from phase6_ethernet import part, symbol

ROOT = Path(__file__).resolve().parent
PATH = ROOT / "ETHERNET.kicad_sch"

def main() -> None:
    text = PATH.read_text()
    start = text.index('(symbol "PiSXMeRevAClean:TPD4E004DRYR"')
    end = start + len(balanced(text, start))
    text = text[:start] + symbol('TPD4E004DRYR', ('MDI0_P','MDI0_N','MDI1_P','MDI1_N','VCC','GND')) + text[end:]
    # Remove every prior generated ESD instance and its generated labels so
    # this migration is deterministic and safe to rerun.
    text = re.sub(r'\(label "(?:CM5_GBE_TD[0-3]_[PN]|ETH_POWER|ETH_GND)"[^\n]*\(uuid d[ab]000000-0000-0000-0000-0000000000[0-9a-f]+\)\)', '', text)
    while '(symbol (lib_id "PiSXMeRevAClean:TPD4E004DRYR")' in text:
        start = text.index('(symbol (lib_id "PiSXMeRevAClean:TPD4E004DRYR")')
        end = start + len(balanced(text, start))
        text = text[:start] + text[end:]
    replacement = part('TPD4E004DRYR', 'U6', 'TPD4E004DRYR', 50, 145,
                       ('CM5_GBE_TD0_P','CM5_GBE_TD0_N','CM5_GBE_TD1_P','CM5_GBE_TD1_N','ETH_POWER','ETH_GND'),
                       0xda000000000000000000000000000000,
                       'PiSXMeRevAClean:TPD4E004DRYR_WSON6')
    replacement += part(
        'TPD4E004DRYR', 'U9', 'TPD4E004DRYR', 50, 165,
        ('CM5_GBE_TD2_P','CM5_GBE_TD2_N','CM5_GBE_TD3_P','CM5_GBE_TD3_N','ETH_POWER','ETH_GND'),
        0xdb000000000000000000000000000000,
        'PiSXMeRevAClean:TPD4E004DRYR_WSON6')
    text = text.replace('  (sheet_instances ', replacement + '\n  (sheet_instances ', 1)
    PATH.write_text(text)
    print('Phase 14 Ethernet ESD migration: TPD4E004DRYR six-pin DRY contract')

if __name__ == '__main__':
    main()
