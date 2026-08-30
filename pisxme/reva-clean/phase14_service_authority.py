"""Promote the selected Amphenol USB-C service connector into the clean tree."""
from pathlib import Path
import re
import re

ROOT = Path(__file__).resolve().parent
DONOR = ROOT.parent / "footprints/PiSXMe.pretty/USB_C_SERVICE_10171746.kicad_mod"
OUT = ROOT / "PiSXMe_RevA_Clean.pretty/USB_C_SERVICE_10171746.kicad_mod"

def main() -> None:
    footprint = DONOR.read_text()
    footprint = footprint.replace('(footprint "USB_C_SERVICE_10171746"',
                                  '(footprint "USB_C_SERVICE_10171746"', 1)
    OUT.write_text(footprint)
    path = ROOT / "SERVICE.kicad_sch"
    text = path.read_text()
    text = text.replace('property "Value" "USB2_UFP_CONNECTOR"',
                        'property "Value" "10171746-00021LF"', 1)
    text = text.replace('property "Value" "USB2_UFP_CONNECTOR" (at 50 108 0)',
                        'property "Value" "10171746-00021LF" (at 50 108 0)', 1)
    text = text.replace('property "MPN" "USB2_UFP_CONNECTOR"',
                        'property "MPN" "10171746-00021LF"', 1)
    text = text.replace('property "Footprint" "" (at 50 95 0)',
                        'property "Footprint" "PiSXMeRevAClean:USB_C_SERVICE_10171746" (at 50 95 0)', 1)
    text = re.sub(r'(property "MPN" "USB2 connector-boundary ESD".*?property "Footprint" )"[^"]*"',
                  r'\1""', text, count=1)
    path.write_text(text)
    print("Phase 14 USB-C authority: Amphenol 10171746-00021LF; pads=18; footprint assigned")

if __name__ == "__main__":
    main()
