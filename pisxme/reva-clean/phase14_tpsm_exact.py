"""Promote the three TPSM63606 rail contracts to the 20-pad package map."""
from pathlib import Path
import re
from phase3_scaffold import balanced, make_uuid

ROOT = Path(__file__).resolve().parent
PATH = ROOT / 'REGULATORS.kicad_sch'

PIN_NAMES = {1:'VIN1',2:'SW',3:'CBOOT',4:'RBOOT',5:'VLDOIN',6:'AGND',7:'VCC',8:'VOUT1',9:'VOUT2',10:'FB',11:'AGND',12:'RT',13:'PG',14:'EN/SYNC',15:'NC',16:'VIN2',17:'PGND',18:'PGND',19:'PGND',20:'PGND'}

def definition(name, visible):
    ps=[]
    for n in range(1,21):
        if n in visible:
            y = visible[n]
            ps.append(f'(pin passive line (at 20 {y} 180) (length 5) (name "{PIN_NAMES[n]}" (effects (font (size 1 1)))) (number "{n}" (effects (font (size 1 1)))))')
        else:
            ps.append(f'(pin passive line (at 0 0 0) (length 0) hide (name "{PIN_NAMES[n]}" (effects (font (size 1 1)))) (number "{n}" (effects (font (size 1 1)))))')
    return f'''(symbol "PiSXMeRevAClean:{name}" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes)
 (property "Reference" "U" (at 0 -10 0) (effects (font (size 1 1))))
 (property "Value" "TPSM63606RDLR" (at 0 10 0) (effects (font (size 1 1))))
 (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes)))
 (symbol "{name}_1_1" (rectangle (start -15 -8) (end 15 8) (stroke (width 0.254) (type default)) (fill (type background))) {' '.join(ps)}) (embedded_fonts no))'''

def replace_definition(text,name,visible):
    marker=f'(symbol "PiSXMeRevAClean:{name}"'; start=text.index(marker); old=balanced(text,start)
    return text[:start]+definition(name,visible)+text[start+len(old):]

def replace_instance(text,ref,base):
    pos=text.index(f'(property "Reference" "{ref}"'); start=text.rfind('(symbol (lib_id',0,pos); old=balanced(text,start)
    pins=''.join(f'(pin "{n}" (uuid {make_uuid(base+n)}))\n' for n in range(1,21))
    block=re.sub(r'\(pin "1".*?\(instances',pins+'(instances',old,flags=re.S)
    return text[:start]+block+text[start+len(old):]

def main():
    text=PATH.read_text()
    text=replace_definition(text,'TPSM63606RDLR_5V',{1:4.5,8:1.5,6:-1.5,13:-4.5})
    text=replace_definition(text,'TPSM63606RDLR_3V3',{1:4.5,8:1.5,6:-1.5,14:-4.5})
    text=replace_definition(text,'TPSM63606RDLR_1V1',{1:4.5,8:1.5,6:-1.5,14:-4.5})
    for ref,base in [('U3',0xd5000000000000000000000000000000),('U4',0xd6000000000000000000000000000000),('U5',0xd7000000000000000000000000000000)]:
        text=replace_instance(text,ref,base)
    PATH.write_text(text)
    print('exact TPSM63606 20-pad mappings applied to U3/U4/U5')

if __name__=='__main__': main()
