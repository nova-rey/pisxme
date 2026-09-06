"""Correct selector instance labels in the saved native storage schematic.

The first integration emitted NC placeholders for several TI selector pins.
This pass replaces labels by physical pin number, confined to each instance's
own label region; it never adds synthetic connectivity.
"""
from pathlib import Path
from phase3_scaffold import balanced

ROOT=Path(__file__).resolve().parent; SCH=ROOT/'STORAGE.kicad_sch'
MAPS={
 'U12':{1:'NC_1',2:'NC_2',3:'NC_3',4:'NC_4',5:'NC_5',6:'USB_OE_N',7:'CM5_USB2_DM',8:'CM5_USB2_DP',9:'USB_SEL',10:'GND',11:'CM5_USB3_TX_P',12:'CM5_USB3_TX_N',13:'STORAGE_3V3',14:'GND',15:'CM5_USB3_RX_P',16:'CM5_USB3_RX_N',17:'GND',18:'NC_18',19:'GND',20:'STORAGE_3V3',21:'GND',22:'JMS_SSRXN',23:'JMS_SSRXP',24:'JMS_SSTXN',25:'JMS_SSTXP',26:'TUSB_SSRXN',27:'TUSB_SSRXP',28:'TUSB_SSTXN',29:'TUSB_SSTXP',30:'STORAGE_3V3',31:'TUSB_USB2_DP',32:'TUSB_USB2_DM',33:'JMS_USB2_DP',34:'JMS_USB2_DM',35:'NC_35',36:'NC_36',37:'NC_37',38:'NC_38',39:'NC_39',40:'NC_40',41:'NC_41',42:'NC_42'},
 'U13':{1:'GND',2:'M2_SATA_A_P_PCIE_TXP0',3:'M2_SATA_A_N_PCIE_TXN0',4:'GND',5:'STORAGE_3V3',6:'M2_PCIE_TXP1',7:'M2_PCIE_TXN1',8:'NC_8',9:'STORAGE_SEL',10:'GND',11:'M2_PCIE_TXP2',12:'M2_PCIE_TXN2',13:'STORAGE_3V3',14:'GND',15:'M2_PCIE_TXP3',16:'M2_PCIE_TXN3',17:'GND',18:'NC_18',19:'GND',20:'STORAGE_3V3',21:'GND',22:'JMS_PCIE_RXN1',23:'JMS_PCIE_RXP1',24:'JMS_PCIE_TXN1',25:'JMS_PCIE_TXP1',26:'NC_26',27:'NC_27',28:'NC_28',29:'NC_29',30:'STORAGE_3V3',31:'JMS_PCIE_RXN0',32:'JMS_PCIE_RXP0',33:'JMS_PCIE_TXN0',34:'JMS_PCIE_TXP0',35:'TUSB_SATA_RXN',36:'TUSB_SATA_RXP',37:'TUSB_SATA_TXN',38:'TUSB_SATA_TXP',39:'NC_39',40:'NC_40',41:'NC_41',42:'NC_42'},
}
OLD_U13={2:'SOCKET_P0_TX',3:'SOCKET_P0_RX',5:'STORAGE_3V3',6:'SOCKET_P1_TX',7:'SOCKET_P1_RX',9:'STORAGE_SEL',10:'GND',11:'SOCKET_P2_TX',12:'SOCKET_P2_RX',15:'SOCKET_P3_TX',16:'SOCKET_P3_RX',22:'JMS_PCIE_TXN0',23:'JMS_PCIE_TXP0',24:'JMS_PCIE_RXN0',25:'JMS_PCIE_RXP0',26:'TUSB_SATA_RXN',27:'TUSB_SATA_RXP',28:'TUSB_SATA_TXN',29:'TUSB_SATA_TXP',30:'STORAGE_3V3'}
def instance_start(text,ref):
    token=f'(property "Reference" "{ref}"'; idx=text.index(token); return text.rfind('(symbol (lib_id',0,idx)
def previous_end(text,start):
    poss=[]; p=0
    while True:
        p=text.find('(symbol (lib_id',p,start)
        if p<0: break
        poss.append(p); p+=1
    return len(balanced(text,poss[-1]))+poss[-1] if poss else 0
def main():
    t=SCH.read_text()
    for ref,pinmap in MAPS.items():
        pinmap={i:('POWER_GND' if n=='GND' else n) for i,n in pinmap.items()}
        s=instance_start(t,ref); prev=previous_end(t,s); seg=t[prev:s]
        x={'U12':'120','U13':'170'}[ref]
        rows=list(__import__('re').finditer(r'\(label "([^"]+)" \(at '+x+r' ',seg))
        if len(rows)==max(pinmap):
            for i,m in reversed(list(enumerate(rows,1))):
                a,b=m.start(1),m.end(1)
                seg=seg[:a]+pinmap[i]+seg[b:]
            t=t[:prev]+seg+t[s:]
            continue
        # Existing generated labels are ordered by physical pin. Replace each
        # old label only once, so repeated GND/3V3 labels remain distinct.
        old=[]
        for i in range(1,max(pinmap)+1):
            old.append(OLD_U13.get(i,'NC_'+str(i)) if ref=='U13' else 'NC_'+str(i))
        for i,new in pinmap.items():
            oldname=old[i-1]
            pos=seg.find(f'(label "{oldname}"')
            if pos<0:
                continue
            seg=seg[:pos]+seg[pos:].replace(f'(label "{oldname}"',f'(label "{new}"',1)
        t=t[:prev]+seg+t[s:]
    SCH.write_text(t); print('corrected selector labels by physical pin')
if __name__=='__main__':main()
