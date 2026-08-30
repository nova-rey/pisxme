"""Generate the schematic-only USB2 SERVICE UFP island."""
from pathlib import Path
from phase3_scaffold import balanced, make_uuid
ROOT=Path(__file__).resolve().parent

def symbol(name,pins):
    rows=[]
    for i,p in enumerate(pins):
        y=(i-(len(pins)-1)/2)*2.5
        rows.append('(pin passive line (at 20 %g 180) (length 5) (name "%s" (effects (font (size 1 1)))) (number "%d" (effects (font (size 1 1)))))'%(y,p,i+1))
    return '(symbol "PiSXMeRevAClean:%s" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes) (property "Reference" "J" (at 0 -12 0) (effects (font (size 1 1)))) (property "Value" "%s" (at 0 12 0) (effects (font (size 1 1)))) (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes))) (symbol "%s_1_1" (rectangle (start -15 -10) (end 15 10) (stroke (width 0.254) (type default)) (fill (type background))) %s) (embedded_fonts no))'%(name,name,name,'\n'.join(rows))

def part(lib,ref,mpn,nets,uid):
    labels=[]; pins=[]
    for i,net in enumerate(nets):
        y=95+(i-(len(nets)-1)/2)*2.5
        labels.append('(label "%s" (at 70 %g 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid %s))'%(net,y,make_uuid(uid+100+i)))
        pins.append('(pin "%d" (uuid %s))'%(i+1,make_uuid(uid+i)))
    return '\n'.join(labels)+'\n(symbol (lib_id "PiSXMeRevAClean:%s") (at 50 95 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid %s) (property "Reference" "%s" (at 50 82 0) (effects (font (size 1.1 1.1)))) (property "Value" "%s" (at 50 108 0) (effects (font (size 1.1 1.1)))) (property "MPN" "%s" (at 50 95 0) (effects (font (size 1 1)) (hide yes))) (property "Footprint" "" (at 50 95 0) (effects (font (size 1 1)) (hide yes))) %s (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000" (reference "%s") (unit 1)))) )'%(lib,make_uuid(uid),ref,mpn,mpn,'\n'.join(pins),ref)

def main():
    path=ROOT/'SERVICE.kicad_sch'; text=path.read_text()
    if 'property "MPN" "USB2_UFP_CONNECTOR"' in text: return
    defs=(symbol('USB2_UFP_CONNECTOR',('USB2_DP','USB2_DM','VBUS_SENSE','SERVICE_GND','CC1_RD','CC2_RD')),
          symbol('USB2_ESD',('USB2_DP','USB2_DM','VBUS_SENSE','SERVICE_GND')),
          symbol('USB2_RD_5K1',('CC','SERVICE_GND')))
    s=text.index('(lib_symbols'); e=s+len(balanced(text,s))-1
    text=text[:e].rstrip()+'\n'+'\n'.join(defs)+text[e:]
    body=part('USB2_UFP_CONNECTOR','J_SERVICE','USB2_UFP_CONNECTOR',('SERVICE_USB2_DP','SERVICE_USB2_DM','SERVICE_VBUS_SENSE','SERVICE_GND','SERVICE_RD_A','SERVICE_RD_B'),0xdd000000000000000000000000000000)
    body+=part('USB2_ESD','U_SERVICE_ESD','USB2 connector-boundary ESD',('SERVICE_USB2_DP','SERVICE_USB2_DM','SERVICE_VBUS_SENSE','SERVICE_GND'),0xde000000000000000000000000000000)
    body+=part('USB2_RD_5K1','R_RD_A','5.1k Rd',('SERVICE_RD_A','SERVICE_GND'),0xdf000000000000000000000000000000)
    body+=part('USB2_RD_5K1','R_RD_B','5.1k Rd',('SERVICE_RD_B','SERVICE_GND'),0xe000000000000000000000000000000)
    text=text.replace('  (sheet_instances ',body+'\n  (sheet_instances ',1)
    path.write_text(text); print('Phase 8 SERVICE island generated: USB2 UFP, ESD, VBUS sense, two Rd')
if __name__=='__main__': main()
