"""Generate the schematic-only Phase 5 power-stage contract islands."""
from pathlib import Path
from phase3_scaffold import balanced, make_uuid

ROOT = Path(__file__).resolve().parent

def sym(name, pins):
    rows = []
    for i, pin in enumerate(pins):
        y = (i - (len(pins)-1)/2) * 3
        rows.append('(pin passive line (at 20 %g 180) (length 5) (name "%s" (effects (font (size 1 1)))) (number "%d" (effects (font (size 1 1)))))' % (y, pin, i+1))
    return '(symbol "PiSXMeRevAClean:%s" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes) (property "Reference" "U" (at 0 -10 0) (effects (font (size 1 1)))) (property "Value" "%s" (at 0 10 0) (effects (font (size 1 1)))) (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes))) (symbol "%s_1_1" (rectangle (start -15 -8) (end 15 8) (stroke (width 0.254) (type default)) (fill (type background))) %s) (embedded_fonts no))' % (name, name, name, '\n'.join(rows))

def part(lib, ref, mpn, nets, uid):
    labels = []
    pins = []
    for i, net in enumerate(nets):
        y = (i - (len(nets)-1)/2) * 3
        labels.append('(label "%s" (at 70 %g 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid %s))' % (net, 95+y, make_uuid(uid+100+i)))
        pins.append('(pin "%d" (uuid %s))' % (i+1, make_uuid(uid+i)))
    return '\n'.join(labels) + '\n(symbol (lib_id "PiSXMeRevAClean:%s") (at 50 95 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid %s) (property "Reference" "%s" (at 50 84 0) (effects (font (size 1.1 1.1)))) (property "Value" "%s" (at 50 106 0) (effects (font (size 1.1 1.1)))) (property "MPN" "%s" (at 50 95 0) (effects (font (size 1 1)) (hide yes))) %s (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000" (reference "%s") (unit 1)))) )' % (lib, make_uuid(uid), ref, mpn, mpn, '\n'.join(pins), ref)

def edit(filename, defs, parts):
    path = ROOT / filename
    text = path.read_text()
    if 'property "MPN"' in text:
        return
    start = text.index('(lib_symbols')
    end = start + len(balanced(text, start)) - 1
    text = text[:end].rstrip() + '\n' + '\n'.join(sym(*d) for d in defs) + text[end:]
    text = text.replace('  (sheet_instances ', '\n'.join(part(*p) for p in parts) + '\n  (sheet_instances ', 1)
    path.write_text(text)

def main():
    edit('POWER_INPUT.kicad_sch', (('LM74700Q1', ('IN', 'PROTECTED', 'GND', 'PG')), ('LM74700Q2', ('IN', 'PROTECTED', 'GND', 'PG'))), (('LM74700Q1', 'U_PROTECT_A', 'LM74700QDBVRQ1', ('12V_IN_A', '12V_PROTECTED', 'POWER_GND', 'POWER_PG_FAULT'), 0xd3000000000000000000000000000000), ('LM74700Q2', 'U_PROTECT_B', 'LM74700QDBVRQ1', ('12V_IN_B', '12V_PROTECTED', 'POWER_GND', 'POWER_PG_FAULT'), 0xd4000000000000000000000000000000)))
    edit('REGULATORS.kicad_sch', (('TPSM63606RDLR_5V', ('IN', 'OUT', 'GND', 'PG')), ('TUSB9261_3V3', ('IN', 'OUT', 'GND', 'EN')), ('TUSB9261_1V1', ('IN', 'OUT', 'GND', 'EN'))), (('TPSM63606RDLR_5V', 'U_CM5_5V', 'TPSM63606RDLR', ('12V_PROTECTED', 'CM5_5V', 'POWER_GND', 'POWER_PG_FAULT'), 0xd5000000000000000000000000000000), ('TUSB9261_3V3', 'U_BRIDGE_3V3', 'TUSB9261IPVP', ('12V_PROTECTED', 'BRIDGE_3V3', 'POWER_GND', 'BRIDGE_ENABLE'), 0xd6000000000000000000000000000000), ('TUSB9261_1V1', 'U_BRIDGE_1V1', 'TUSB9261IPVP', ('12V_PROTECTED', 'BRIDGE_1V1', 'POWER_GND', 'BRIDGE_ENABLE'), 0xd7000000000000000000000000000000)))
    print('Phase 5 power islands generated')

if __name__ == '__main__':
    main()
