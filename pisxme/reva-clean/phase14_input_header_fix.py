"""Place and connect the two mandatory cold-plug input headers."""
from pathlib import Path
from phase3_scaffold import balanced, make_uuid

PATH = Path(__file__).resolve().parent / 'POWER_INPUT.kicad_sch'

def main() -> None:
    text = PATH.read_text()
    text = text.replace('(label "12V_IN_A" (at 70 93.75 0)', '(label "12V_IN_A" (at 70 41.25 0)', 1)
    text = text.replace('(label "POWER_GND" (at 70 96.25 0)', '(label "POWER_GND" (at 70 38.75 0)', 1)
    text = text.replace('(label "12V_IN_B" (at 70 93.75 0)', '(label "12V_IN_B" (at 70 81.25 0)', 1)
    text = text.replace('(label "POWER_GND" (at 70 96.25 0)', '(label "POWER_GND" (at 70 78.75 0)', 1)
    cursor = 0
    for ref, y in (('J5', 40), ('J6', 80)):
        pos = text.index(f'(property "Reference" "{ref}"', cursor)
        start = text.rfind('(symbol (lib_id', 0, pos)
        block = balanced(text, start)
        block = block.replace('(at 50 95 0)', f'(at 50 {y} 0)', 1)
        text = text[:start] + block + text[start + len(block):]
        cursor = start + len(block)
    # The header definition has pin anchors 17 mm right of the symbol origin;
    # labels terminate at x=70, so these explicit 3 mm wires reach the pin
    # connection ends and keep the connection visible to native ERC.
    wires = ''
    for i, y in enumerate((40, 80)):
        for j, yy in enumerate((y + 1.25, y - 1.25)):
            uid = 0xea000000000000000000000000000000 + i * 0x10 + j
            wires += f'(wire (pts (xy 70 {yy:g}) (xy 67 {yy:g})) (stroke (width 0) (type default)) (uuid {make_uuid(uid)}))\n'
    text = text.replace('  (sheet_instances ', wires + '  (sheet_instances ', 1)
    PATH.write_text(text)
    print('input headers placed and branch-connected: J5@40, J6@80')

if __name__ == '__main__':
    main()
