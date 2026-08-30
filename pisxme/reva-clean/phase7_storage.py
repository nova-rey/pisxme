"""Generate the schematic-only USB3-to-SATA storage island."""
from pathlib import Path
from phase3_scaffold import balanced, make_uuid

ROOT=Path(__file__).resolve().parent

def symbol(name,pins):
    rows=[]
    for i,p in enumerate(pins):
        y=(i-(len(pins)-1)/2)*2.5
        rows.append('(pin passive line (at 20 %g 180) (length 5) (name "%s" (effects (font (size 1 1)))) (number "%d" (effects (font (size 1 1)))))'%(y,p,i+1))
    return '(symbol "PiSXMeRevAClean:%s" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes) (property "Reference" "U" (at 0 -12 0) (effects (font (size 1 1)))) (property "Value" "%s" (at 0 12 0) (effects (font (size 1 1)))) (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes))) (symbol "%s_1_1" (rectangle (start -15 -10) (end 15 10) (stroke (width 0.254) (type default)) (fill (type background))) %s) (embedded_fonts no))'%(name,name,name,'\n'.join(rows))

def part(lib,ref,mpn,nets,uid,footprint=''):
    labels=[]; pins=[]
    for i,net in enumerate(nets):
        y=95+(i-(len(nets)-1)/2)*2.5
        labels.append('(label "%s" (at 70 %g 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid %s))'%(net,y,make_uuid(uid+100+i)))
        pins.append('(pin "%d" (uuid %s))'%(i+1,make_uuid(uid+i)))
    return '\n'.join(labels)+'\n(symbol (lib_id "PiSXMeRevAClean:%s") (at 50 95 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid %s) (property "Reference" "%s" (at 50 82 0) (effects (font (size 1.1 1.1)))) (property "Value" "%s" (at 50 108 0) (effects (font (size 1.1 1.1)))) (property "MPN" "%s" (at 50 95 0) (effects (font (size 1 1)) (hide yes))) (property "Footprint" "%s" (at 50 95 0) (effects (font (size 1 1)) (hide yes))) %s (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000" (reference "%s") (unit 1)))) )'%(lib,make_uuid(uid),ref,mpn,mpn,footprint,'\n'.join(pins),ref)

def main():
    path=ROOT/'STORAGE.kicad_sch'; text=path.read_text()
    if 'property "MPN" "TUSB9261IPVP"' in text: return
    defs=(symbol('TUSB9261IPVP_STORAGE',('USB3_TX_P','USB3_TX_N','USB3_RX_P','USB3_RX_N','SATA_TX_P','SATA_TX_N','SATA_RX_P','SATA_RX_N','BRIDGE_3V3','BRIDGE_1V1','RESET','SPI_CFG')),
          symbol('JAE_SM3ZS067U410ABR1000',('SATA_TX_P','SATA_TX_N','SATA_RX_P','SATA_RX_N','M2_3V3','M2_GND')))
    s=text.index('(lib_symbols'); e=s+len(balanced(text,s))-1
    text=text[:e].rstrip()+'\n'+'\n'.join(defs)+text[e:]
    bridge=part('TUSB9261IPVP_STORAGE','U_STORAGE_BRIDGE','TUSB9261IPVP',('CM5_USB3_TX_P','CM5_USB3_TX_N','CM5_USB3_RX_P','CM5_USB3_RX_N','BRIDGE_SATA_TX_P','BRIDGE_SATA_TX_N','BRIDGE_SATA_RX_P','BRIDGE_SATA_RX_N','BRIDGE_3V3','BRIDGE_1V1','BRIDGE_RESET','BRIDGE_CFG'),0xdb000000000000000000000000000000,'PiSXMeRevAClean:TUSB9261IPVP')
    socket=part('JAE_SM3ZS067U410ABR1000','J_STORAGE_M2','SM3ZS067U410ABR1000',('BRIDGE_SATA_TX_P','BRIDGE_SATA_TX_N','BRIDGE_SATA_RX_P','BRIDGE_SATA_RX_N','M2_3V3','M2_GND'),0xdc000000000000000000000000000000,'PiSXMeRevAClean:SM3ZS067U410ABR1000')
    text=text.replace('  (sheet_instances ',bridge+'\n'+socket+'\n  (sheet_instances ',1)
    path.write_text(text)
    print('Phase 7 storage island generated: USB3 -> TUSB9261 -> SATA -> B-key M.2')

if __name__=='__main__': main()
