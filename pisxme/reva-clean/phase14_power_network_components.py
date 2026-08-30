"""Add the external protection components required by the Phase 5 topology."""
from pathlib import Path
from phase3_scaffold import balanced, make_uuid

ROOT = Path(__file__).resolve().parent
PATH = ROOT / 'POWER_INPUT.kicad_sch'

def defn(name, pins):
    ps = ' '.join(f'(pin passive line (at {x} {y} {a}) (length 5) (name "{n}" (effects (font (size 1 1)))) (number "{num}" (effects (font (size 1 1)))))' for num,n,x,y,a in pins)
    return f'''(symbol "PiSXMeRevAClean:{name}" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes)
 (property "Reference" "U" (at 0 -8 0) (effects (font (size 1 1))))
 (property "Value" "{name}" (at 0 8 0) (effects (font (size 1 1))))
 (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes)))
 (symbol "{name}_1_1" (rectangle (start -15 -6) (end 15 6) (stroke (width 0.254) (type default)) (fill (type background))) {ps}) (embedded_fonts no))'''

def part(ref, uid, lib, value, mpn, footprint, x, y, nets, count):
    labels = ''.join(f'(label "{net}" (at {x + (-12 if count == 2 and i == 0 else 12 if count == 2 else (-20 if i == 0 else 20))} {y + (0 if count != 3 or i < 2 else 5)} 0) (effects (font (size 1 1)) (justify left)) (uuid {make_uuid(uid+100+i)}))\n' for i,net in enumerate(nets))
    pins = ''.join(f'(pin "{i+1}" (uuid {make_uuid(uid+i)}))\n' for i in range(count))
    return f'''{labels}(symbol (lib_id "PiSXMeRevAClean:{lib}") (at {x} {y} 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid {make_uuid(uid)})
 (property "Reference" "{ref}" (at {x} {y-8} 0) (effects (font (size 1 1))))
 (property "Value" "{value}" (at {x} {y+8} 0) (effects (font (size 1 1))))
 (property "MPN" "{mpn}" (at {x} {y} 0) (effects (font (size 1 1)) (hide yes)))
 (property "Footprint" "PiSXMeRevAClean:{footprint}" (at {x} {y} 0) (effects (font (size 1 1)) (hide yes)))
 {pins}(instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000004" (reference "{ref}") (unit 1)))) )'''

def main():
    text = PATH.read_text()
    if 'property "MPN" "CSD19536KCS"' in text:
        return
    s = text.index('(lib_symbols'); e = s + len(balanced(text,s)) - 1
    defs = defn('FUSE_HOLDER_17861650001', [('1','RAW',-12,0,0),('2','FUSED',12,0,180)])
    defs += defn('CSD19536KCS', [('1','SOURCE',-20,0,0),('2','DRAIN',20,0,180),('3','GATE',20,5,180)])
    defs += defn('VCAP_100NF', [('1','VCAP',-12,0,0),('2','GND',12,0,180)])
    text = text[:e].rstrip() + '\n' + defs + text[e:]
    body = part('F1',0xf1000000000000000000000000000000,'FUSE_HOLDER_17861650001','0297015.U / 178.6165.0001','0297015.U','ATO_FuseHolder_17861650001',90,40,('12V_IN_A','FUSED_12V_A'),2)
    body += part('F2',0xf2000000000000000000000000000000,'FUSE_HOLDER_17861650001','0297015.U / 178.6165.0001','0297015.U','ATO_FuseHolder_17861650001',90,80,('12V_IN_B','FUSED_12V_B'),2)
    body += part('Q1',0xf3000000000000000000000000000000,'CSD19536KCS','CSD19536KCS','CSD19536KCS','CSD19536KCS_TO220',130,40,('FUSED_12V_A','12V_PROTECTED','GATE_A'),3)
    body += part('Q2',0xf4000000000000000000000000000000,'CSD19536KCS','CSD19536KCS','CSD19536KCS','CSD19536KCS_TO220',130,80,('FUSED_12V_B','12V_PROTECTED','GATE_B'),3)
    body += part('C3',0xf5000000000000000000000000000000,'VCAP_100NF','100nF VCAP A','GRM188R71H104KA93D','C_0603_1608Metric',110,55,('VCAP_A','12V_IN_A'),2)
    body += part('C4',0xf6000000000000000000000000000000,'VCAP_100NF','100nF VCAP B','GRM188R71H104KA93D','C_0603_1608Metric',110,95,('VCAP_B','12V_IN_B'),2)
    text = text.replace('  (sheet_instances ', body + '\n  (sheet_instances ', 1)
    PATH.write_text(text)
    print('Phase 5 protection components added: F1/F2, Q1/Q2, C3/C4')

if __name__ == '__main__': main()
