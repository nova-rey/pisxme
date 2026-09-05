"""Repair the generated SERVICE sheet's duplicated, overlapping instances."""
from pathlib import Path
import re
from phase3_scaffold import balanced

R=Path(__file__).resolve().parent
P=R/'SERVICE.kicad_sch'

def move_instance(text, ref, xy):
    start=0
    while True:
        pos=text.find('(symbol (lib_id ',start)
        if pos<0: raise RuntimeError('missing '+ref)
        end=pos+len(balanced(text,pos)); block=text[pos:end]
        if f'(property "Reference" "{ref}"' in block:
            old='(at 50 95 0)'
            if old not in block: raise RuntimeError('unexpected '+ref+' placement')
            block=block.replace(old, f'(at {xy[0]} {xy[1]} 0)', 1)
            return text[:pos]+block+text[end:]
        start=end

def label_xy(text, prefix, x, dy):
    pat=re.compile(r'(\(label "[^"]+" \(at )70 ([0-9]+(?:\.[0-9]+)?) (0\) .*?\(uuid '+re.escape(prefix)+r'[0-9a-f-]+\)\))')
    def repl(m):
        y=float(m.group(2))+dy
        return m.group(1)+f'{x:g} {y:g} '+m.group(3)
    return pat.sub(repl,text)

def main():
    text=P.read_text()
    # phase14_service_authority left the original four-label U8 group in
    # front of the corrected three-label group. Remove only that exact stale
    # group, retaining the corrected U8 DP/DM/GND labels.
    stale=re.compile(r'\(label "SERVICE_USB2_DP" \(at 70 91\.25 0\).*?\(uuid de000000-0000-0000-0000-000000000064\)\)\n'
                     r'\(label "SERVICE_USB2_DM" \(at 70 93\.75 0\).*?\(uuid de000000-0000-0000-0000-000000000065\)\)\n'
                     r'\(label "SERVICE_VBUS_SENSE" \(at 70 96\.25 0\).*?\(uuid de000000-0000-0000-0000-000000000066\)\)\n'
                     r'\(label "SERVICE_GND" \(at 70 98\.75 0\).*?\(uuid de000000-0000-0000-0000-000000000067\)\)\n')
    text,count=stale.subn('',text,count=1)
    if count!=1: raise RuntimeError('stale U8 label group not found')
    text=move_instance(text,'J4',(30,95))
    text=move_instance(text,'U8',(70,95))
    text=move_instance(text,'R1',(50,110))
    text=move_instance(text,'R2',(70,110))
    text=label_xy(text,'dd000000',50,0)
    text=label_xy(text,'de000000',90,0)
    text=label_xy(text,'df000000',70,15)
    text=label_xy(text,'0e000000',90,15)
    P.write_text(text)
    print('SERVICE instances separated: J4(30,95) U8(70,95) R1(50,110) R2(70,110)')
if __name__=='__main__': main()
