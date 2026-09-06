"""Integrate the reviewed dual-mode storage symbols into STORAGE.kicad_sch.

The edit is deterministic and idempotent. It replaces only the obsolete B-key
connector and adds the storage-local bridge/selectors; existing U7 and local
SATA support are retained. All pin numbers come from retained authorities.
"""
from pathlib import Path
import re
from phase3_scaffold import balanced, make_uuid

ROOT=Path(__file__).resolve().parent
SCH=ROOT/'STORAGE.kicad_sch'
PATH='/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000007'

JMS={16:'VBUS',17:'USB_DM',18:'USB_DP',21:'USB_TXP1',22:'USB_TXN1',23:'USB_TXN2',24:'USB_TXP2',26:'USB_RXP1',27:'USB_RXN1',28:'USB_RXN2',29:'USB_RXP2',34:'PCIE_RXN1',35:'PCIE_RXP1',37:'PCIE_TXN1',38:'PCIE_TXP1',41:'PCIE_RXN0',42:'PCIE_RXP0',44:'PCIE_TXN0',45:'PCIE_TXP0',47:'REFCLK_N',48:'REFCLK_P',50:'XIN',51:'XOUT',54:'PCIE_RESET_N',55:'PCIE_CLKREQ_N',60:'TME',63:'GND',64:'LXO'}
USB={6:'USB_OE_N',9:'USB_SEL',10:'GND',11:'CM5_SSTXP',12:'CM5_SSTXN',15:'CM5_SSRXP',16:'CM5_SSRXN',22:'JMS_SSRXN',23:'JMS_SSRXP',24:'JMS_SSTXN',25:'JMS_SSTXP',26:'TUSB_SSRXN',27:'TUSB_SSRXP',28:'TUSB_SSTXN',29:'TUSB_SSTXP',30:'STORAGE_3V3',31:'NC',32:'NC',33:'CM5_USB2_DP',34:'CM5_USB2_DM',35:'NC',36:'NC',37:'NC',38:'NC',39:'NC',40:'NC',41:'NC',42:'NC'}
MUX={2:'SOCKET_P0_TX',3:'SOCKET_P0_RX',5:'STORAGE_3V3',6:'SOCKET_P1_TX',7:'SOCKET_P1_RX',9:'STORAGE_SEL',10:'GND',11:'SOCKET_P2_TX',12:'SOCKET_P2_RX',15:'SOCKET_P3_TX',16:'SOCKET_P3_RX',22:'JMS_PCIE_TXN0',23:'JMS_PCIE_TXP0',24:'JMS_PCIE_RXN0',25:'JMS_PCIE_RXP0',26:'TUSB_SATA_RXN',27:'TUSB_SATA_RXP',28:'TUSB_SATA_TXN',29:'TUSB_SATA_TXP',31:'NC',32:'NC',33:'NC',34:'NC',35:'NC',36:'NC',37:'NC',38:'NC',39:'NC',40:'NC',41:'NC',42:'NC'}
M2={1:'M2_CONFIG3',2:'M2_3V3',3:'M2_GND',4:'M2_3V3',5:'M2_PCIE_RXN3',7:'M2_PCIE_RXP3',9:'M2_GND',10:'M2_DAS_DSS',11:'M2_PCIE_TXN3',12:'M2_3V3',13:'M2_PCIE_TXP3',14:'M2_3V3',15:'M2_GND',16:'M2_3V3',17:'M2_PCIE_RXN2',18:'M2_3V3',19:'M2_PCIE_RXP2',21:'M2_CONFIG0',23:'M2_PCIE_TXN2',25:'M2_PCIE_TXP2',27:'M2_GND',29:'M2_PCIE_RXN1',31:'M2_PCIE_RXP1',33:'M2_GND',35:'M2_PCIE_TXN1',37:'M2_PCIE_TXP1',38:'M2_DEVSLP',39:'M2_GND',41:'M2_SATA_B_P_PCIE_RXN0',43:'M2_SATA_B_N_PCIE_RXP0',45:'M2_GND',47:'M2_SATA_A_N_PCIE_TXN0',49:'M2_SATA_A_P_PCIE_TXP0',50:'M2_PERST_N',51:'M2_GND',52:'M2_CLKREQ_N',53:'M2_REFCLK_N',54:'M2_PEWake_N',55:'M2_REFCLK_P',56:'M2_MFG1',57:'M2_GND',58:'M2_MFG2',68:'M2_SUSCLK',69:'M2_CONFIG1',70:'M2_3V3',71:'M2_GND',72:'M2_3V3',73:'M2_GND',74:'M2_3V3',75:'M2_CONFIG2'}

def definition(name, pinmap):
    rows=[]
    for i in range(1,max(pinmap)+1):
        y=(i-(max(pinmap)+1)/2)*1.27
        rows.append(f'(pin passive line (at 20 {y:g} 180) (length 5) (name "{pinmap.get(i,"NC_"+str(i))}" (effects (font (size 1 1)))) (number "{i}" (effects (font (size 1 1)))))')
    return f'''(symbol "PiSXMeRevAClean:{name}" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes)
 (property "Reference" "U" (at 0 -10 0) (effects (font (size 1 1))))
 (property "Value" "{name}" (at 0 10 0) (effects (font (size 1 1))))
 (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes)))
 (symbol "{name}_1_1" (rectangle (start -15 -8) (end 15 8) (stroke (width 0.254) (type default)) (fill (type background)))
 {' '.join(rows)}) (embedded_fonts no))'''

def instance(name, ref, mpn, pinmap, uid, x, y, footprint):
    labels=[]; pins=[]
    count=max(pinmap)
    for i in range(1,count+1):
        py=y-(i-(count+1)/2)*1.27
        net=pinmap.get(i,'NC_'+str(i))
        labels.append(f'(label "{net}" (at {x+20:g} {py:g} 0) (effects (font (size 0.8 0.8)) (justify left)) (uuid {make_uuid(uid+100+i)}))')
        pins.append(f'(pin "{i}" (uuid {make_uuid(uid+i)}))')
    return f'''{''.join(labels)}
(symbol (lib_id "PiSXMeRevAClean:{name}") (at {x:g} {y:g} 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid {make_uuid(uid)})
 (property "Reference" "{ref}" (at {x:g} {y-12:g} 0) (effects (font (size 1.1 1.1))))
 (property "Value" "{mpn}" (at {x:g} {y+12:g} 0) (effects (font (size 1.1 1.1))))
 (property "MPN" "{mpn}" (at {x:g} {y:g} 0) (effects (font (size 1 1)) (hide yes)))
 (property "Footprint" "{footprint}" (at {x:g} {y:g} 0) (effects (font (size 1 1)) (hide yes)))
 {' '.join(pins)} (instances (project "PiSXMe_RevA_Clean" (path "{PATH}" (reference "{ref}") (unit 1)))) )'''

def remove_block(text, needle):
    start=text.index(needle); return text[:start]+text[start+len(balanced(text,start)):]

def main():
    text=SCH.read_text()
    if 'property "Reference" "U8"' in text:
        print('already integrated'); return
    # Remove obsolete connector definition and instance only. Existing U7 and
    # its validated SATA support remain untouched.
    text=remove_block(text,'(symbol "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000"')
    text=remove_block(text,'(symbol (lib_id "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000")')
    lib_end=text.index('(lib_symbols'); lib_close=lib_end+len(balanced(text,lib_end))-1
    defs='\n'.join((definition('JMS583_QFN64',JMS),definition('HD3SS6126_RUA0042A',USB),definition('HD3SS3412_RUA0042A',MUX),definition('TE_1-2199230-4_MKEY',M2)))
    text=text[:lib_close].rstrip()+'\n'+defs+'\n'+text[lib_close:]
    marker='\n  (sheet_instances '
    instances='\n'.join((instance('JMS583_QFN64','U8','JMS583-QHFA3A',JMS,0xf1000000000000000000000000000000,50,165,'PiSXMeRevAClean:JMS583_QFN64_8x8'),instance('HD3SS6126_RUA0042A','U9','HD3SS6126RUAR',USB,0xf1000000000000000000000000000100,100,165,'PiSXMeRevAClean:HD3SS6126_RUA0042A'),instance('HD3SS3412_RUA0042A','U10','HD3SS3412RUAR',MUX,0xf1000000000000000000000000000200,150,165,'PiSXMeRevAClean:HD3SS3412_RUA0042A'),instance('TE_1-2199230-4_MKEY','J3','1-2199230-4',M2,0xf1000000000000000000000000000300,220,165,'PiSXMeRevAClean:TE_1-2199230-4_MKEY')))
    text=text.replace(marker,'\n'+instances+marker,1)
    SCH.write_text(text)
    print('integrated U8/U9/U10/J3 into STORAGE.kicad_sch')
if __name__=='__main__': main()
