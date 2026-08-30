"""Correct the two bridge-rail instances to the selected regulator MPN."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent
PATH = ROOT / 'REGULATORS.kicad_sch'

def main() -> None:
    text = PATH.read_text()
    text = text.replace('TUSB9261_3V3', 'TPSM63606RDLR_3V3')
    text = text.replace('TUSB9261_1V1', 'TPSM63606RDLR_1V1')
    text = text.replace('property "Value" "TUSB9261IPVP"', 'property "Value" "TPSM63606RDLR"')
    text = text.replace('property "MPN" "TUSB9261IPVP"', 'property "MPN" "TPSM63606RDLR"')
    text = text.replace('PiSXMeRevAClean:TUSB9261IPVP_HTQFP64', 'PiSXMeRevAClean:TPSM63606RDLR_RDL0020')
    PATH.write_text(text)
    print('Phase 14 regulator correction: U4/U5 are TPSM63606RDLR rail modules')

if __name__ == '__main__': main()
