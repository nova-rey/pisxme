"""Add the two selected dual 12 V Molex input headers to POWER_INPUT."""
from pathlib import Path
from phase3_scaffold import balanced, make_uuid

ROOT = Path(__file__).resolve().parent
PATH = ROOT / 'POWER_INPUT.kicad_sch'

def symbol():
    return '''(symbol "PiSXMeRevAClean:POWER_INPUT_HEADER" (pin_names (offset 0.8))
 (exclude_from_sim no) (in_bom yes) (on_board yes)
 (property "Reference" "J" (at 0 -6 0) (effects (font (size 1 1))))
 (property "Value" "POWER_INPUT_HEADER" (at 0 6 0) (effects (font (size 1 1))))
 (property "Footprint" "PiSXMeRevAClean:Molex_0039300020_5569_2P_RA" (at 0 0 0) (effects (font (size 1 1)) (hide yes)))
 (symbol "POWER_INPUT_HEADER_1_1" (rectangle (start -12 -3) (end 12 3) (stroke (width 0.254) (type default)) (fill (type background)))
  (pin passive line (at 17 -1.25 180) (length 5) (name "12V" (effects (font (size 1 1)))) (number "1" (effects (font (size 1 1)))))
  (pin passive line (at 17 1.25 180) (length 5) (name "GND" (effects (font (size 1 1)))) (number "2" (effects (font (size 1 1))))) ) (embedded_fonts no))'''

def part(ref, uid, nets):
    labels = ''.join(f'(label "{net}" (at 70 {93.75+i*2.5} 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid {make_uuid(uid+100+i)}))\n' for i, net in enumerate(nets))
    pins = ''.join(f'(pin "{i+1}" (uuid {make_uuid(uid+i)}))\n' for i in range(2))
    return f'''{labels}(symbol (lib_id "PiSXMeRevAClean:POWER_INPUT_HEADER") (at 50 95 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid {make_uuid(uid)})
 (property "Reference" "{ref}" (at 50 82 0) (effects (font (size 1.1 1.1))))
 (property "Value" "0039300020" (at 50 108 0) (effects (font (size 1.1 1.1))))
 (property "MPN" "0039300020" (at 50 95 0) (effects (font (size 1 1)) (hide yes)))
 (property "Footprint" "PiSXMeRevAClean:Molex_0039300020_5569_2P_RA" (at 50 95 0) (effects (font (size 1 1)) (hide yes)))
 {pins}(instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000004" (reference "{ref}") (unit 1)))) )'''

def main():
    text = PATH.read_text()
    if 'property "MPN" "0039300020"' in text:
        return
    s = text.index('(lib_symbols'); e = s + len(balanced(text, s)) - 1
    text = text[:e].rstrip() + '\n' + symbol() + text[e:]
    body = part('J5', 0xe1000000000000000000000000000000, ('12V_IN_A','POWER_GND'))
    body += part('J6', 0xe2000000000000000000000000000000, ('12V_IN_B','POWER_GND'))
    text = text.replace('  (sheet_instances ', body + '\n  (sheet_instances ', 1)
    PATH.write_text(text)
    print('Phase 14 input headers: two Molex 0039300020 instances added')

if __name__ == '__main__': main()
