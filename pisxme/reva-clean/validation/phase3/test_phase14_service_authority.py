from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

def main() -> None:
    fp = (ROOT / "PiSXMe_RevA_Clean.pretty/USB_C_SERVICE_10171746.kicad_mod").read_text()
    assert fp.count('(pad "') == 18
    assert 'property "Value" "Amphenol 10171746-00021LF USB-C USB2 SERVICE"' in fp
    sch = (ROOT / "SERVICE.kicad_sch").read_text()
    assert 'property "MPN" "10171746-00021LF"' in sch
    assert 'property "Value" "10171746-00021LF" (at 50 108 0)' in sch
    assert 'property "Footprint" "PiSXMeRevAClean:USB_C_SERVICE_10171746"' in sch
    assert 'property "MPN" "USB2_UFP_CONNECTOR"' not in sch
    print("Phase 14 USB-C service authority: PASS; contacts=16; shell=2; exact MPN assigned")

if __name__ == "__main__":
    main()
