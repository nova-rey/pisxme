"""Add the two selected SMBJ18A branch TVS devices to POWER_INPUT."""
from pathlib import Path
from phase3_scaffold import balanced, make_uuid

ROOT=Path(__file__).resolve().parent
PATH=ROOT/'POWER_INPUT.kicad_sch'

def definition():
    return '''(symbol "PiSXMeRevAClean:SMBJ18A_TVS" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes)
 (property "Reference" "D" (at 0 -8 0) (effects (font (size 1 1))))
 (property "Value" "SMBJ18A" (at 0 8 0) (effects (font (size 1 1))))
 (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes)))
 (symbol "SMBJ18A_TVS_1_1" (rectangle (start -15 -6) (end 15 6) (stroke (width 0.254) (type default)) (fill (type background)))
  (pin passive line (at -12 0 0) (length 5) (name "A" (effects (font (size 1 1)))) (number "1" (effects (font (size 1 1)))))
  (pin passive line (at 12 0 180) (length 5) (name "K" (effects (font (size 1 1)))) (number "2" (effects (font (size 1 1))))) ) (embedded_fonts no))'''

def instance(ref,uid,x,y,net1):
    return f'''(label "{net1}" (at {x-12} {y} 0) (effects (font (size 1 1)) (justify left)) (uuid {make_uuid(uid+100)}))
(label "POWER_GND" (at {x+12} {y} 0) (effects (font (size 1 1)) (justify left)) (uuid {make_uuid(uid+101)}))
(symbol (lib_id "PiSXMeRevAClean:SMBJ18A_TVS") (at {x} {y} 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid {make_uuid(uid)})
 (property "Reference" "{ref}" (at {x} {y-8} 0) (effects (font (size 1 1))))
 (property "Value" "SMBJ18A" (at {x} {y+8} 0) (effects (font (size 1 1))))
 (property "MPN" "SMBJ18A" (at {x} {y} 0) (effects (font (size 1 1)) (hide yes)))
 (property "Footprint" "PiSXMeRevAClean:TVS_SMBJ18A_DO214AA" (at {x} {y} 0) (effects (font (size 1 1)) (hide yes)))
 (pin "1" (uuid {make_uuid(uid+1)})) (pin "2" (uuid {make_uuid(uid+2)}))
 (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000004" (reference "{ref}") (unit 1)))) )'''

def main():
    text=PATH.read_text()
    if 'property "MPN" "SMBJ18A"' in text:
        print('TVS already present'); return
    s=text.index('(lib_symbols'); e=s+len(balanced(text,s))-1
    text=text[:e].rstrip()+'\n'+definition()+text[e:]
    body=instance('D1',0xf8000000000000000000000000000000,110,40,'FUSED_12V_A')
    body+=instance('D2',0xf9000000000000000000000000000000,110,80,'FUSED_12V_B')
    text=text.replace('  (sheet_instances ',body+'\n  (sheet_instances ',1)
    PATH.write_text(text)
    print('SMBJ18A TVS branches added')

if __name__=='__main__': main()
