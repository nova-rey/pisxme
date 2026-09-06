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

JMS={1:'JMS_VDDREG_5V',2:'JMS_VCCK',3:'JMS_SPI_SO_DNP',4:'JMS_SPI_SCK_DNP',5:'JMS_SPI_SI_DNP',6:'JMS_VCCO',7:'JMS_SPI_CS_N_DNP',8:'JMS_GPIO4_NC',9:'JMS_GPIO5_NC',10:'JMS_VBUS_SENSE',11:'JMS_VCCO',12:'JMS_GPIO7_NC',13:'JMS_GPIO8_NC',14:'JMS_GPIO9_NC',15:'JMS_RESET_N',16:'VBUS',17:'USB_DM',18:'USB_DP',19:'JMS_AVDD33',20:'JMS_AVDDL',21:'USB_TXP1',22:'USB_TXN1',23:'USB_TXN2',24:'USB_TXP2',25:'JMS_AVDDL',26:'USB_RXP1',27:'USB_RXN1',28:'USB_RXN2',29:'USB_RXP2',30:'JMS_AVDDL',31:'JMS_VCCK',32:'JMS_VCCO',33:'JMS_AVDDL',34:'PCIE_RXN1',35:'PCIE_RXP1',36:'JMS_AVDDL',37:'PCIE_TXN1',38:'PCIE_TXP1',39:'JMS_REXT',40:'JMS_AVDDL',41:'PCIE_RXN0',42:'PCIE_RXP0',43:'JMS_AVDDL',44:'PCIE_TXN0',45:'PCIE_TXP0',46:'JMS_AVDDL',47:'REFCLK_N',48:'REFCLK_P',49:'JMS_AVDDL',50:'XIN',51:'XOUT',52:'JMS_XAVDDH',53:'JMS_VCCK',54:'PCIE_RESET_N',55:'PCIE_CLKREQ_N',56:'JMS_VCCO',57:'JMS_GPIO12_NC',58:'JMS_GPIO11_NC',59:'JMS_GPIO10_NC',60:'TME',61:'JMS_CC2_NC',62:'JMS_CC1_NC',63:'POWER_GND',64:'LXO'}
USB={6:'USB_OE_N',7:'CM5_USB2_DM',8:'CM5_USB2_DP',9:'USB_SEL',10:'POWER_GND',11:'CM5_SSTXP',12:'CM5_SSTXN',13:'STORAGE_3V3',14:'POWER_GND',15:'CM5_SSRXP',16:'CM5_SSRXN',17:'POWER_GND',18:'NC_18',19:'POWER_GND',20:'STORAGE_3V3',21:'POWER_GND',22:'JMS_SSRXN',23:'JMS_SSRXP',24:'JMS_SSTXN',25:'JMS_SSTXP',26:'TUSB_SSRXN',27:'TUSB_SSRXP',28:'TUSB_SSTXN',29:'TUSB_SSTXP',30:'STORAGE_3V3',31:'TUSB_USB2_DP',32:'TUSB_USB2_DM',33:'JMS_USB2_DP',34:'JMS_USB2_DM',35:'NC_35',36:'NC_36',37:'NC_37',38:'NC_38',39:'NC_39',40:'NC_40',41:'NC_41',42:'NC_42'}
MUX={1:'POWER_GND',2:'M2_SATA_A_P_PCIE_TXP0',3:'M2_SATA_A_N_PCIE_TXN0',4:'POWER_GND',5:'STORAGE_3V3',6:'M2_PCIE_TXP1',7:'M2_PCIE_TXN1',8:'NC_8',9:'STORAGE_SEL',10:'POWER_GND',11:'M2_PCIE_TXP2',12:'M2_PCIE_TXN2',13:'STORAGE_3V3',14:'POWER_GND',15:'M2_PCIE_TXP3',16:'M2_PCIE_TXN3',17:'POWER_GND',18:'NC_18',19:'POWER_GND',20:'STORAGE_3V3',21:'POWER_GND',22:'JMS_PCIE_RXN1',23:'JMS_PCIE_RXP1',24:'JMS_PCIE_TXN1',25:'JMS_PCIE_TXP1',26:'NC_26',27:'NC_27',28:'NC_28',29:'NC_29',30:'STORAGE_3V3',31:'JMS_PCIE_RXN0',32:'JMS_PCIE_RXP0',33:'JMS_PCIE_TXN0',34:'JMS_PCIE_TXP0',35:'TUSB_SATA_RXN',36:'TUSB_SATA_RXP',37:'TUSB_SATA_TXN',38:'TUSB_SATA_TXP',39:'NC_39',40:'NC_40',41:'NC_41',42:'NC_42'}
M2={1:'M2_CONFIG3',2:'M2_3V3',3:'M2_GND',4:'M2_3V3',5:'M2_PCIE_RXN3',7:'M2_PCIE_RXP3',9:'M2_GND',10:'M2_DAS_DSS',11:'M2_PCIE_TXN3',12:'M2_3V3',13:'M2_PCIE_TXP3',14:'M2_3V3',15:'M2_GND',16:'M2_3V3',17:'M2_PCIE_RXN2',18:'M2_3V3',19:'M2_PCIE_RXP2',21:'M2_CONFIG0',23:'M2_PCIE_TXN2',25:'M2_PCIE_TXP2',27:'M2_GND',29:'M2_PCIE_RXN1',31:'M2_PCIE_RXP1',33:'M2_GND',35:'M2_PCIE_TXN1',37:'M2_PCIE_TXP1',38:'M2_DEVSLP',39:'M2_GND',41:'M2_SATA_B_P_PCIE_RXN0',43:'M2_SATA_B_N_PCIE_RXP0',45:'M2_GND',47:'M2_SATA_A_N_PCIE_TXN0',49:'M2_SATA_A_P_PCIE_TXP0',50:'M2_PERST_N',51:'M2_GND',52:'M2_CLKREQ_N',53:'M2_REFCLK_N',54:'M2_PEWake_N',55:'M2_REFCLK_P',56:'M2_MFG1',57:'M2_GND',58:'M2_MFG2',68:'M2_SUSCLK',69:'M2_PEDET',70:'M2_3V3',71:'M2_GND',72:'M2_3V3',73:'M2_GND',74:'M2_3V3',75:'M2_CONFIG2'}

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
    if 'property "Reference" "U11"' in text:
        print('already integrated'); return
    # Remove obsolete connector definition and instance only. Existing U7 and
    # its validated SATA support remain untouched.
    text=remove_block(text,'(symbol "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000"')
    text=remove_block(text,'(symbol (lib_id "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000")')
    lib_end=text.index('(lib_symbols'); lib_close=lib_end+len(balanced(text,lib_end))-1
    defs='\n'.join((definition('JMS583_QFN64',JMS),definition('HD3SS6126_RUA0042A',USB),definition('HD3SS3412_RUA0042A',MUX),definition('TE_1-2199230-4_MKEY',M2)))
    text=text[:lib_close].rstrip()+'\n'+defs+'\n'+text[lib_close:]
    marker='\n  (sheet_instances '
    instances='\n'.join((instance('JMS583_QFN64','U11','JMS583-QHFA3A',JMS,0xf1000000000000000000000000000000,50,165,'PiSXMeRevAClean:JMS583_QFN64_8x8'),instance('HD3SS6126_RUA0042A','U12','HD3SS6126RUAR',USB,0xf1000000000000000000000000000100,100,165,'PiSXMeRevAClean:HD3SS6126_RUA0042A'),instance('HD3SS3412_RUA0042A','U13','HD3SS3412RUAR',MUX,0xf1000000000000000000000000000200,150,165,'PiSXMeRevAClean:HD3SS3412_RUA0042A'),instance('TE_1-2199230-4_MKEY','J3','1-2199230-4',M2,0xf1000000000000000000000000000300,220,165,'PiSXMeRevAClean:TE_1-2199230-4_MKEY')))
    text=text.replace(marker,'\n'+instances+marker,1)
    SCH.write_text(text)
    print('integrated U8/U9/U10/J3 into STORAGE.kicad_sch')
if __name__=='__main__': main()
