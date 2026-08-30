"""Promote the selected Amphenol USB-C service connector into the clean tree."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
DONOR = ROOT.parent / "footprints/PiSXMe.pretty/USB_C_SERVICE_10171746.kicad_mod"
OUT = ROOT / "PiSXMe_RevA_Clean.pretty/USB_C_SERVICE_10171746.kicad_mod"
ESD_OUT = ROOT / "PiSXMe_RevA_Clean.pretty/Texas_DRT_3.kicad_mod"

ESD_FOOTPRINT = '''(footprint "Texas_DRT_3" (version 20211014) (generator pcbnew)
  (layer "F.Cu")
  (descr "Texas Instruments DRT-3 1x0.8mm, 0.7mm pitch; TI TPD2EUSB30 datasheet; KiCad maintained footprint")
  (tags "DRT-3 1x0.8mm Pitch 0.7mm")
  (property "Reference" "REF**" (at 0 -1.5 0) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
  (property "Value" "Texas_DRT_3" (at 0 1.5 0) (layer "F.Fab") (hide yes) (effects (font (size 0.8 0.8) (thickness 0.12))))
  (attr smd)
  (fp_line (start 0.65 -0.55) (end 0.45 -0.55) (stroke (width 0.12) (type default)) (layer "F.SilkS"))
  (fp_line (start 0.65 0) (end 0.65 -0.55) (stroke (width 0.12) (type default)) (layer "F.SilkS"))
  (fp_line (start -0.65 0) (end -0.65 -0.55) (stroke (width 0.12) (type default)) (layer "F.SilkS"))
  (fp_line (start -0.65 -0.55) (end -0.45 -0.55) (stroke (width 0.12) (type default)) (layer "F.SilkS"))
  (fp_rect (start -0.8 -0.7) (end 0.8 0.7) (stroke (width 0.05) (type default)) (fill none) (layer "F.CrtYd"))
  (pad "1" smd rect (at -0.35 0.425) (size 0.3 0.3) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "2" smd rect (at 0.35 0.425) (size 0.3 0.3) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "3" smd rect (at 0 -0.425) (size 0.3 0.3) (layers "F.Cu" "F.Paste" "F.Mask"))
)\n'''

def main() -> None:
    footprint = DONOR.read_text()
    footprint = footprint.replace('(footprint "USB_C_SERVICE_10171746"',
                                  '(footprint "USB_C_SERVICE_10171746"', 1)
    OUT.write_text(footprint)
    ESD_OUT.write_text(ESD_FOOTPRINT)
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
    lines = []
    for line in text.splitlines(keepends=True):
        if 'property "MPN" "TPD2EUSB30DRTR"' in line:
            line = re.sub(r'property "Footprint" "[^"]*"',
                          'property "Footprint" "PiSXMeRevAClean:Texas_DRT_3"', line)
        if 'property "MPN" "5.1k Rd"' in line:
            line = re.sub(r'property "Footprint" "[^"]*"',
                          'property "Footprint" "PiSXMeRevAClean:R_0402_1005Metric"', line)
        lines.append(line)
    text = ''.join(lines)
    path.write_text(text)
    print("Phase 14 USB-C authority: Amphenol 10171746-00021LF; pads=18; footprint assigned")

if __name__ == "__main__":
    main()
