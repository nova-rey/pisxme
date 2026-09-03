"""Generate the schematic-only CM5IO-derived Ethernet island."""
from pathlib import Path
from phase3_scaffold import balanced, make_uuid

ROOT = Path(__file__).resolve().parent

PIN_UUID_BASES = {
    'EDAC_A70_112_331N126_Ethernet': 0x60000000000000000000000000000000,
    'TPD4E004DRYR': 0x61000000000000000000000000000000,
}

def pin_uuid(name, index):
    return make_uuid(PIN_UUID_BASES[name] + index)

def symbol(name, pins):
    rows = []
    for i, pin in enumerate(pins):
        # KiCad schematic Y grows downward; keep pin 1 at the upper boundary
        # so the generated boundary labels and native pin numbers coincide.
        y = ((len(pins)-1)/2 - i) * 2.5
        rows.append('(pin passive line (at 20 %g 180) (length 5) (name "%s" (effects (font (size 1 1)))) (number "%d" (effects (font (size 1 1)))) (uuid %s))' % (y, pin, i+1, pin_uuid(name, i)))
    return '(symbol "PiSXMeRevAClean:%s" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes) (property "Reference" "U" (at 0 -12 0) (effects (font (size 1 1)))) (property "Value" "%s" (at 0 12 0) (effects (font (size 1 1)))) (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes))) (symbol "%s_1_1" (rectangle (start -15 -10) (end 15 10) (stroke (width 0.254) (type default)) (fill (type background))) %s) (embedded_fonts no))' % (name, name, name, '\n'.join(rows))

def part(lib, ref, mpn, x, y, nets, uid, footprint=''):
    labels=[]; refs=[]
    for i, net in enumerate(nets):
        py=y+(i-(len(nets)-1)/2)*2.5
        labels.append('(label "%s" (at %g %g 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid %s))' % (net,x+20,py,make_uuid(uid+100+i)))
        # Instance pin UUIDs must be unique within the symbol instance and
        # must not collide with the instance UUID itself.  KiCad resolves the
        # library pin by number; the UUID is instance identity only.
        refs.append('(pin "%d" (uuid %s))' % (i+1,make_uuid(uid + 0x100 + i)))
    return '\n'.join(labels)+'\n(symbol (lib_id "PiSXMeRevAClean:%s") (at %s %s 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid %s) (property "Reference" "%s" (at %s %s 0) (effects (font (size 1.1 1.1)))) (property "Value" "%s" (at %s %s 0) (effects (font (size 1.1 1.1)))) (property "MPN" "%s" (at %s %s 0) (effects (font (size 1 1)) (hide yes))) (property "Footprint" "%s" (at %s %s 0) (effects (font (size 1 1)) (hide yes))) %s (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000" (reference "%s") (unit 1)))) )' % (lib,x,y,make_uuid(uid),ref,x,y-13,mpn,x,y+13,mpn,x,y,footprint,x,y,'\n'.join(refs),ref)

def main():
    path=ROOT/'ETHERNET.kicad_sch'; text=path.read_text()
    if 'property "MPN" "TPD4E004DRYR"' in text:
        return
    defs=(symbol('EDAC_A70_112_331N126_Ethernet',('TRD0+','TRD0-','TRD1+','TRD1-','TRD2+','TRD2-','TRD3+','TRD3-','VC1','VC2','VC3','VC4','LEDY_A','LEDY_K','LEDG_A','LEDG_K','SHIELD_A','SHIELD_B')),
          symbol('TPD4E004DRYR',('MDI0_P','MDI0_N','MDI1_P','MDI1_N','VCC','GND')))
    s=text.index('(lib_symbols'); e=s+len(balanced(text,s))-1
    text=text[:e].rstrip()+'\n'+'\n'.join(defs)+text[e:]
    mag_nets=('CM5_GBE_TD0_P','CM5_GBE_TD0_N','CM5_GBE_TD1_P','CM5_GBE_TD1_N','CM5_GBE_TD2_P','CM5_GBE_TD2_N','CM5_GBE_TD3_P','CM5_GBE_TD3_N','ETH_CT1','ETH_CT2','ETH_CT3','ETH_CT4','GBE_LED_Y_A','GBE_LED_Y_K','GBE_LED_G_A','GBE_LED_G_K','GBE_SHIELD','GBE_SHIELD')
    esd_nets=('CM5_GBE_TD0_P','CM5_GBE_TD0_N','ETH_GND','CM5_GBE_TD1_P','CM5_GBE_TD1_N','ETH_POWER')
    body=part('EDAC_A70_112_331N126_Ethernet','J_ETHERNET','A70-112-331N126',50,100,mag_nets,0xd9000000000000000000000000000000,'PiSXMeRevAClean:EDAC_A70_112_331N126')
    body+=part('TPD4E004DRYR','U_ETH_ESD_A','TPD4E004DRYR',50,145,('CM5_GBE_TD0_P','CM5_GBE_TD0_N','CM5_GBE_TD1_P','CM5_GBE_TD1_N','ETH_POWER','ETH_GND'),0xda000000000000000000000000000000,'Package_DFN_QFN:WSON-6-1EP_1.5x1.5mm_P0.5mm_EP0.95x0.95mm')
    body+=part('TPD4E004DRYR','U_ETH_ESD_B','TPD4E004DRYR',50,165,('CM5_GBE_TD2_P','CM5_GBE_TD2_N','ETH_GND','CM5_GBE_TD3_P','CM5_GBE_TD3_N','ETH_POWER'),0xdb000000000000000000000000000000,'Package_DFN_QFN:WSON-6-1EP_1.5x1.5mm_P0.5mm_EP0.95x0.95mm')
    text=text.replace('  (sheet_instances ',body+'\n  (sheet_instances ',1)
    path.write_text(text)
    print('Phase 6 Ethernet island generated')

if __name__=='__main__': main()
