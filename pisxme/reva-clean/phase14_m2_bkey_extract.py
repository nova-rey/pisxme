"""Derive the JAE SM3 B-key pattern from the dimensioned M.2 reference."""
from pathlib import Path
import re
import uuid

ROOT = Path(__file__).resolve().parent
DONOR = ROOT / "authority-inventory/cm5io-rev2/CM5IO.pretty/M.2 M Key socket.kicad_mod"
OUT = ROOT / "PiSXMe_RevA_Clean.pretty/JAE_SM3ZS067U410ABR1000_BKEY.kicad_mod"

def block(text: str, start: int) -> tuple[str, int]:
    depth = 0; quoted = False; escaped = False
    for i in range(start, len(text)):
        c = text[i]
        if quoted and escaped: escaped = False
        elif quoted and c == "\\": escaped = True
        elif c == '"': quoted = not quoted
        elif not quoted:
            if c == "(": depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0: return text[start:i + 1], i + 1
    raise ValueError("unbalanced footprint")

def main() -> None:
    source = DONOR.read_text()
    spans = []
    for m in re.finditer(r'\(pad "(\d+)" smd rect', source):
        value, end = block(source, m.start()); spans.append((int(m.group(1)), value))
    pads = dict(spans)
    assert set(pads) == set(range(1, 59)) | set(range(67, 76))
    moved = {}
    for number in range(12, 20):
        new = re.sub(r'\(pad "\d+"', f'(pad "{number + 47}"', pads[number], count=1)
        new = re.sub(r'\(uuid "[^"]+"\)', f'(uuid "{uuid.UUID(int=0x14000000000000000000000000000000 + number)}")', new, count=1)
        moved[number + 47] = new
        source = source.replace(pads[number], "", 1)
    insertion = source.index(pads[67])
    source = source[:insertion] + "\n".join(moved.values()) + "\n" + source[insertion:]
    source = source.replace('(footprint "M.2 M Key socket"', '(footprint "JAE_SM3ZS067U410ABR1000_BKEY"', 1)
    source = source.replace('(property "Value" "M.2 M Key socket"', '(property "Value" "JAE SM3ZS067U410ABR1000 B-key SATA socket"', 1)
    source = source.replace('(property "Footprint" "M.2 M Key socket"', '(property "Footprint" "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000_BKEY"', 1)
    source = source.replace('(layer "F.Cu")', '(layer "F.Cu")\n\t(property "Description" "Derived from JAE SM3ZS067U410 drawing; B-key void 12-19 per SATA-IO TP053")', 1)
    model = source.find('\n\t(model ')
    if model >= 0:
        source = source[:model] + '\n'
    OUT.write_text(source)
    storage = ROOT / "STORAGE.kicad_sch"
    storage.write_text(storage.read_text().replace('property "Footprint" "PiSXMeRevAClean:SM3ZS067U410ABR1000"', 'property "Footprint" "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000_BKEY"'))
    print("Phase 14 M.2 B-key extraction: 67 contacts; void=12-19")

if __name__ == "__main__": main()
