"""Promote the two clean-sheet LM74700 contracts to the exact DBV pin map."""
from pathlib import Path
import re
from phase3_scaffold import balanced, make_uuid

ROOT = Path(__file__).resolve().parent
PATH = ROOT / 'POWER_INPUT.kicad_sch'

def definition(name):
    pins = [
        ('power_out','VCAP','1','0 -12 0',True),
        ('power_in','GND','2','20 -1.5 180',False),
        ('input','EN','3','20 -4.5 180',False),
        ('input','CATHODE','4','20 1.5 180',False),
        ('output','GATE','5','0 12 0',True),
        ('input','ANODE','6','20 4.5 180',False),
    ]
    ps = ' '.join(f'(pin {typ} line (at {at}) (length 5){" hide" if hidden else ""} (name "{n}" (effects (font (size 1 1)))) (number "{num}" (effects (font (size 1 1)))))' for typ,n,num,at,hidden in pins)
    return f'''(symbol "PiSXMeRevAClean:{name}" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes)
 (property "Reference" "U" (at 0 -10 0) (effects (font (size 1 1))))
 (property "Value" "LM74700Q1" (at 0 10 0) (effects (font (size 1 1))))
 (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes)))
 (symbol "{name}_1_1" (rectangle (start -15 -8) (end 15 8) (stroke (width 0.254) (type default)) (fill (type background))) {ps}) (embedded_fonts no))'''

def replace_definition(text, name):
    marker = f'(symbol "PiSXMeRevAClean:{name}"'
    start = text.index(marker); old = balanced(text,start)
    return text[:start] + definition(name) + text[start+len(old):]

def replace_instance(text, ref, y, branch):
    pos = text.index(f'(property "Reference" "{ref}"')
    start = text.rfind('(symbol (lib_id', 0, pos); old = balanced(text,start)
    block = old
    block = re.sub(r'\(pin "1".*?\(instances',
                   ''.join(f'(pin "{n}" (uuid {make_uuid(0xd0000000000000000000000000000000 + (1 if ref == "U1" else 2)*100 + n)}))\n' for n in range(1,7)) + '(instances', block, flags=re.S)
    block = block.replace('(at 50 95 0)', f'(at 50 {y} 0)', 1)
    block = block.replace(f'(reference "{ref}")', f'(reference "{ref}")')
    return text[:start] + block + text[start+len(old):]

def move_branch_labels(text, prefix, dy):
    # The four generated branch labels carry the branch-specific UUID prefix.
    for suffix in ('064','065','066','067'):
        pat = rf'(label "[^"]+" \(at 70 )([0-9.]+)( 0\).*?\(uuid {prefix}-0000-0000-0000-{suffix}\))'
        text = re.sub(pat, lambda m: m.group(1)+f'{float(m.group(2))+dy:g}'+m.group(3), text)
    return text

def add_label(text, name, x, y, uid):
    marker = '  (sheet_instances '
    label = f'(label "{name}" (at {x} {y} 0) (effects (font (size 1 1)) (justify left)) (uuid {make_uuid(uid)}))\n'
    return text.replace(marker, label + marker, 1)

def main():
    text = PATH.read_text()
    text = replace_definition(text, 'LM74700Q1')
    text = replace_definition(text, 'LM74700Q2')
    text = replace_instance(text, 'U1', 95, 'A')
    text = replace_instance(text, 'U2', 145, 'B')
    text = move_branch_labels(text, 'd4000000', 50)
    # The controller ANODE is downstream of the branch fuse, and EN is always on.
    text = text.replace('(label "12V_IN_A" (at 70 90.5 0)', '(label "FUSED_12V_A" (at 70 90.5 0)', 1)
    text = text.replace('(label "POWER_PG_FAULT" (at 70 99.5 0)', '(label "12V_IN_A" (at 70 99.5 0)', 1)
    text = text.replace('(label "12V_IN_B" (at 70 140.5 0)', '(label "FUSED_12V_B" (at 70 140.5 0)', 1)
    text = text.replace('(label "POWER_PG_FAULT" (at 70 149.5 0)', '(label "12V_IN_B" (at 70 149.5 0)', 1)
    if 'label "VCAP_A"' not in text:
        for name,x,y,uid in [('VCAP_A',50,107,0xf7000000000000000000000000000000),('GATE_A',50,83,0xf7000000000000000000000000000001),('VCAP_B',50,157,0xf7000000000000000000000000000002),('GATE_B',50,133,0xf7000000000000000000000000000003)]:
            text = add_label(text,name,x,y,uid)
    PATH.write_text(text)
    print('exact LM74700 DBV mapping applied: U1/U2 pins=1..6; branches separated')

if __name__ == '__main__': main()
