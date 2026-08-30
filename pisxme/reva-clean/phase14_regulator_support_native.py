"""Add label-connected TPSM support parts after the native pin probe."""
from pathlib import Path
from phase3_scaffold import balanced, make_uuid

ROOT=Path(__file__).resolve().parent
PATH=ROOT/'REGULATORS.kicad_sch'
NATIVE_LIB=ROOT/'authority-inventory/cm5io-rev2/CM5IO.kicad_sch'
LOCAL_LIB=ROOT/'POWER_INPUT.kicad_sch'

def lib_def():
    return '''(symbol "PiSXMeRevAClean:SUPPORT_PASSIVE" (pin_names (offset 0.6)) (exclude_from_sim no) (in_bom yes) (on_board yes)
 (property "Reference" "R" (at 0 -2 0) (effects (font (size 1 1))))
 (property "Value" "R" (at 0 2 0) (effects (font (size 1 1))))
 (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes)))
 (symbol "SUPPORT_PASSIVE_1_1" (rectangle (start -2 -1) (end 2 1) (stroke (width 0.1524) (type default)) (fill (type background)))
  (pin passive line (at -5 0 0) (length 3) (name "1" (effects (font (size 1 1)))) (number "1" (effects (font (size 1 1)))))
  (pin passive line (at 5 0 180) (length 3) (name "2" (effects (font (size 1 1)))) (number "2" (effects (font (size 1 1))))) ) (embedded_fonts no))'''

def add_lib(s):
    ls=s.index('(lib_symbols'); e=ls+len(balanced(s,ls))-1
    additions=[]
    native=NATIVE_LIB.read_text()
    for name in ('Device:C','Device:R'):
        if f'(symbol "{name}"' not in s:
            st=native.index(f'(symbol "{name}"')
            additions.append(balanced(native,st))
    local=LOCAL_LIB.read_text()
    if '(symbol "PiSXMeRevAClean:VCAP_100NF"' not in s:
        st=local.index('(symbol "PiSXMeRevAClean:VCAP_100NF"')
        additions.append(balanced(local,st))
    return s[:e].rstrip()+'\n'+'\n'.join(additions)+s[e:]

def part(ref, uid, value, mpn, x, y, a, b):
    fp=('C_1210_3225Metric' if mpn.startswith('GRM32') else 'C_1206_3216Metric' if mpn.startswith('C3216') else 'C_0805_2012Metric') if ref.startswith('C') else 'R_0402_1005Metric'
    source=LOCAL_LIB.read_text()
    p=source.index('(symbol (lib_id "PiSXMeRevAClean:VCAP_100NF"')
    block=balanced(source,p)
    block=block.replace('C3',ref).replace('100nF VCAP A',value)
    block=block.replace('PiSXMeRevAClean:VCAP_100NF', 'Device:C' if ref.startswith('C') else 'Device:R')
    # Match KiCad 10's native instance serialization.  In particular,
    # fields_autoplaced/dnp are not cosmetic here: omitting them makes the
    # headless resolver silently discard these child-sheet instances.
    block=block.replace('(on_board yes) (dnp no) (uuid', '(on_board yes) (dnp no) (fields_autoplaced no) (uuid')
    block=block.replace('GRM188R71H104KA93D',mpn)
    block=block.replace('PiSXMeRevAClean:C_0603_1608Metric',f'PiSXMeRevAClean:{fp}')
    block=block.replace('(at 110 55 0)',f'(at {x} {y} 0)')
    block=block.replace('(at 110 47 0)',f'(at {x} {y-8} 0)')
    block=block.replace('(at 110 63 0)',f'(at {x} {y+8} 0)')
    block=block.replace('f5000000-0000-0000-0000-000000000000',make_uuid(uid))
    block=block.replace('f5000000-0000-0000-0000-000000000001',make_uuid(uid+1))
    block=block.replace('f5000000-0000-0000-0000-000000000002',make_uuid(uid+2))
    block=block.replace(f'(pin "1" (uuid {make_uuid(uid)}))', f'(pin "1" (uuid {make_uuid(uid+1)}))')
    block=block.replace(f'(pin "2" (uuid {make_uuid(uid+1)}))', f'(pin "2" (uuid {make_uuid(uid+2)}))')
    block=block.replace('/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000004','/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000005')
    return f'''(label "{a}" (at {x} {y-3.81} 0) (effects (font (size 1 1)) (justify left)) (uuid {make_uuid(uid+10)}))
(label "{b}" (at {x} {y+3.81} 0) (effects (font (size 1 1)) (justify left)) (uuid {make_uuid(uid+11)}))
(wire (pts (xy {x} {y-3.81}) (xy {x-1} {y-3.81})) (stroke (width 0) (type default)) (uuid {make_uuid(uid+12)}))
(wire (pts (xy {x} {y+3.81}) (xy {x+1} {y+3.81})) (stroke (width 0) (type default)) (uuid {make_uuid(uid+13)}))
{block}'''

def main():
    s=add_lib(PATH.read_text())
    begin='; PHASE14_NATIVE_SUPPORT_BEGIN\n'; end='; PHASE14_NATIVE_SUPPORT_END\n'
    if begin in s:
        a=s.index(begin); b=s.index(end,a)+len(end); s=s[:a]+s[b:]
    out=[begin]
    # Exact TI table/reference-design networks for the two closed rows.
    specs=[
      ('5V',95,'CM5_5V','40.2k','RC0402FR-0740K2L','22p','CM5_5V','C5','C6','C7','C8','C9',('10uF 50V','10uF 50V','22uF','22uF','22pF')),
      ('3V3',95,'BRIDGE_3V3','23.2k','RC0402FR-0723K2L','47p','BRIDGE_3V3','C14','C15','C16','C17','C18',('10uF 50V','10uF 50V','22uF','22uF','47pF')),
    ]
    uid=0xf8000000000000000000000000000000
    for row,(suffix,y,outnet,rfbt,rfmpn,cff,cffnet,c1,c2,c3,c4,c5,vals) in enumerate(specs):
        rail = 'CM5_5V' if suffix == '5V' else 'BRIDGE_3V3'
        entries=[(c1,vals[0],'C3216X7R1H106K160AC','12V_PROTECTED','POWER_GND'),(c2,vals[1],'C3216X7R1H106K160AC','12V_PROTECTED','POWER_GND'),(c3,vals[2],'GRM32ER71C226KEA8K',outnet,'POWER_GND'),(c4,vals[3],'GRM32ER71C226KEA8K',outnet,'POWER_GND'),(c5,vals[4],'GCM1555C1H220JA16','FB_'+rail,outnet),(f'R{3 if suffix=="5V" else 11}',rfbt,rfmpn,outnet,'FB_'+rail),(f'R{4 if suffix=="5V" else 12}','10k','RC0402FR-0710KL','FB_'+rail,'POWER_GND'),(f'R{5 if suffix=="5V" else 13}','13k' if suffix=='5V' else '27k','RC0402FR-0713KL' if suffix=='5V' else 'RC0402FR-0727KL','RT_'+rail,'POWER_GND'),(f'R{6 if suffix=="5V" else 14}','100k','RC0402FR-07100KL',outnet,'PG_'+rail)]
        for i,(ref,val,mpn,a,b) in enumerate(entries):
            out.append(part(ref,uid,val,mpn,115+(i%5)*17,75+row*35+(i//5)*10,a,b)); uid+=0x20
        if suffix == '3V3':
            out.append(part('C19',uid,'22uF','GRM32ER71C226KEA8K',200,85,'BRIDGE_3V3','POWER_GND')); uid+=0x20
    # The 1.1-V row is deliberately only a bias/enable/PG scaffold until its
    # non-table FB, RT and effective-COUT calculation is independently closed.
    for i,(ref,val,mpn,a,b) in enumerate((
        ('C23','10uF 50V','C3216X7R1H106K160AC','12V_PROTECTED','POWER_GND'),
        ('C24','1uF','GRM188R71H104KA93D','12V_PROTECTED','POWER_GND'),
        ('C25','10uF 50V','C3216X7R1H106K160AC','12V_PROTECTED','POWER_GND'),
        ('R19','1k','RC0402FR-0710KL','BRIDGE_1V1','FB_BRIDGE_1V1'),
        ('R20','10k','RC0402FR-0710KL','FB_BRIDGE_1V1','POWER_GND'),
        ('R21','2k','RC0402FR-072KL','RT_BRIDGE_1V1','POWER_GND'),
        ('R22','100k','RC0402FR-07100KL','BRIDGE_1V1','PG_BRIDGE_1V1'),
        *[(f'C{n}','22uF','GRM32ER71C226KEA8K','BRIDGE_1V1','POWER_GND') for n in range(26, 42)],
    )):
        out.append(part(ref,uid,val,mpn,115+(i*17),180,a,b)); uid+=0x20
    out.append(end)
    anchor='  (sheet_instances '
    s=s.replace(anchor,'\n'.join(out)+'\n'+anchor,1)
    PATH.write_text(s)
    print('native TPSM support network applied')
if __name__=='__main__': main()
