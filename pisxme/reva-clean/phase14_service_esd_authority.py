"""Replace the SERVICE ESD placeholder with the selected TI two-channel part."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from phase3_scaffold import balanced
from phase8_service import part, symbol

ROOT = Path(__file__).resolve().parent

def main() -> None:
    path = ROOT / 'SERVICE.kicad_sch'
    text = path.read_text()
    lib_start = text.index('(lib_symbols')
    lib_end = lib_start + len(balanced(text, lib_start))
    old_def_start = text.index('(symbol "PiSXMeRevAClean:USB2_ESD"', lib_start)
    old_def_end = old_def_start + len(balanced(text, old_def_start))
    text = text[:old_def_start] + symbol('USB2_ESD', ('USB2_DP', 'USB2_DM', 'SERVICE_GND')) + text[old_def_end:]
    lib_end += len(symbol('USB2_ESD', ('USB2_DP', 'USB2_DM', 'SERVICE_GND'))) - (old_def_end - old_def_start)
    inst_start = text.index('(symbol (lib_id "PiSXMeRevAClean:USB2_ESD")', lib_end)
    inst_end = inst_start + len(balanced(text, inst_start))
    replacement = part('USB2_ESD', 'U_SERVICE_ESD', 'TPD2EUSB30DRTR',
                        ('SERVICE_USB2_DP', 'SERVICE_USB2_DM', 'SERVICE_GND'),
                        0xde000000000000000000000000000000)
    text = text[:inst_start] + replacement + text[inst_end:]
    path.write_text(text)
    print('Phase 14 SERVICE ESD: TPD2EUSB30DRTR; pins=3; footprint intentionally gated')

if __name__ == '__main__':
    main()
