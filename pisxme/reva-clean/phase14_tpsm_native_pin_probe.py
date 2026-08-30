"""Probe the proven KiCad right-facing pin/label serialization for TPSM."""
from pathlib import Path
from phase3_scaffold import balanced

P=Path(__file__).resolve().parent/'REGULATORS.kicad_sch'
N={1:'VIN1',2:'SW',3:'CBOOT',4:'RBOOT',5:'VLDOIN',6:'AGND',7:'VCC',8:'VOUT1',9:'VOUT2',10:'FB',11:'AGND',12:'RT',13:'PG',14:'EN/SYNC',15:'NC',16:'VIN2',17:'PGND',18:'PGND',19:'PGND',20:'PGND'}

def definition(name):
    pins=[]
    for n in range(1,21):
        y=-20+(n-1)*2
        pins.append(f'(pin passive line (at 20 {y} 180) (length 5) (name "{N[n]}" (effects (font (size 1 1)))) (number "{n}" (effects (font (size 1 1)))))')
    return f'''(symbol "PiSXMeRevAClean:{name}" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes)
 (property "Reference" "U" (at 0 -24 0) (effects (font (size 1 1))))
 (property "Value" "TPSM63606RDLR" (at 0 24 0) (effects (font (size 1 1))))
 (property "Footprint" "PiSXMeRevAClean:TPSM63606RDLR_RDL0020" (at 0 0 0) (effects (font (size 1 1)) (hide yes)))
 (symbol "{name}_1_1" (rectangle (start -15 -22) (end 15 22) (stroke (width 0.254) (type default)) (fill (type background))) {' '.join(pins)}) (embedded_fonts no))'''

def replace(text,name,block):
    st=text.index(f'(symbol "PiSXMeRevAClean:{name}"'); old=balanced(text,st)
    return text[:st]+block+text[st+len(old):]

def main():
    s=P.read_text()
    for name in ('TPSM63606RDLR_5V','TPSM63606RDLR_3V3','TPSM63606RDLR_1V1'):
        s=replace(s,name,definition(name))
    # Remove the previous four-label scaffold rows; the probe supplies one
    # explicit label for every package pin instead.
    lines=[]
    for line in s.splitlines(True):
        if line.startswith('(label ') and '(at 70 ' in line and any(f'"{x}"' in line for x in ('12V_PROTECTED','CM5_5V','BRIDGE_3V3','BRIDGE_1V1','POWER_GND','POWER_PG_FAULT','BRIDGE_ENABLE')):
            continue
        lines.append(line)
    s=''.join(lines)
    start=s.index('  (sheet_instances ')
    labels=[]
    for i,(ref,y,rail) in enumerate((('U3',95,'CM5_5V'),('U4',95,'BRIDGE_3V3'),('U5',95,'BRIDGE_1V1'))):
        nets={1:'12V_PROTECTED',2:f'SW_{rail}',3:f'CBOOT_{rail}',4:f'RBOOT_{rail}',5:'12V_PROTECTED',6:'POWER_GND',7:'VCC_INTERNAL',8:rail,9:rail,10:f'FB_{rail}',11:'POWER_GND',12:f'RT_{rail}',13:f'PG_{rail}',14:f'ENABLE_{rail}',15:'NC',16:'12V_PROTECTED',17:'POWER_GND',18:'POWER_GND',19:'POWER_GND',20:'POWER_GND'}
        for n in range(1,21):
            py=y-(-20+(n-1)*2)
            labels.append(f'(label "{nets[n]}" (at 70 {py} 0) (effects (font (size 1.0 1.0)) (justify left)) (uuid 0a000000-0000-{i:04x}-0000-{n:012x}))\n')
    s=s[:start]+''.join(labels)+s[start:]
    P.write_text(s)
    print('TPSM right-facing native pin probe applied')
if __name__=='__main__': main()
