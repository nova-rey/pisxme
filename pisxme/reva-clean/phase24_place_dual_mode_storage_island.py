"""Create a disposable native PCB placement candidate for the new storage island.

This is deliberately a placement/authority fixture, not a claim of completed
routing. It starts from the selected storage macro ancestor and replaces only
J3/adds U8-U10 inside the storage acreage.
"""
from pathlib import Path
import re, uuid
from phase3_scaffold import balanced

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_BCU_INTEGRATED_ASTAR_V3.kicad_pcb'
OUT=ROOT/'PHASE24_DUAL_MODE_STORAGE_PLACEMENT.kicad_pcb'
LIB=ROOT/'PiSXMe_RevA_Clean.pretty'

MAPS={
 'JMS583_QFN64_8x8.kicad_mod':('U11',{16:'STORAGE_USB_VBUS',17:'STORAGE_USB_DN',18:'STORAGE_USB_DP',21:'JMS_USB_TXP1',22:'JMS_USB_TXN1',23:'JMS_USB_TXN2',24:'JMS_USB_TXP2',26:'JMS_USB_RXP1',27:'JMS_USB_RXN1',28:'JMS_USB_RXN2',29:'JMS_USB_RXP2',34:'JMS_PCIE_RXN1',35:'JMS_PCIE_RXP1',37:'JMS_PCIE_TXN1',38:'JMS_PCIE_TXP1',41:'JMS_PCIE_RXN0',42:'JMS_PCIE_RXP0',44:'JMS_PCIE_TXN0',45:'JMS_PCIE_TXP0',47:'JMS_REFCLK_N',48:'JMS_REFCLK_P',50:'JMS_XIN',51:'JMS_XOUT',54:'JMS_PERST_N',55:'JMS_CLKREQ_N',60:'GND',63:'POWER_GND',64:'JMS_LXO'}),
 'HD3SS6126_RUA0042A.kicad_mod':('U12',{6:'USB_SEL_OE_N',7:'CM5_USB2_DN',8:'CM5_USB2_DP',9:'STORAGE_USB_SEL',10:'POWER_GND',11:'CM5_USB3_TXP',12:'CM5_USB3_TXN',15:'CM5_USB3_RXP',16:'CM5_USB3_RXN',22:'JMS_USB3_RXN',23:'JMS_USB3_RXP',24:'JMS_USB3_TXN',25:'JMS_USB3_TXP',26:'TUSB_USB3_RXN',27:'TUSB_USB3_RXP',28:'TUSB_USB3_TXN',29:'TUSB_USB3_TXP',31:'TUSB_USB2_DP',32:'TUSB_USB2_DN',33:'JMS_USB2_DP',34:'JMS_USB2_DN',13:'STORAGE_3V3',20:'STORAGE_3V3',30:'STORAGE_3V3'}),
 'HD3SS3412_RUA0042A.kicad_mod':('U13',{2:'M2_PCIE_TXP0',3:'M2_PCIE_RXP0',5:'STORAGE_3V3',6:'M2_PCIE_TXP1',7:'M2_PCIE_RXP1',9:'STORAGE_SEL',10:'POWER_GND',11:'M2_PCIE_TXP2',12:'M2_PCIE_RXP2',15:'M2_PCIE_TXP3',16:'M2_PCIE_RXP3',22:'JMS_PCIE_TXN0',23:'JMS_PCIE_TXP0',24:'JMS_PCIE_RXN0',25:'JMS_PCIE_RXP0',26:'TUSB_SATA_RXN',27:'TUSB_SATA_RXP',28:'TUSB_SATA_TXN',29:'TUSB_SATA_TXP',30:'STORAGE_3V3'}),
 'TE_1-2199230-4_MKEY.kicad_mod':('J3',{2:'M2_3V3',3:'POWER_GND',4:'M2_3V3',41:'M2_SATA_B_P_PCIE_RXN0',43:'M2_SATA_B_N_PCIE_RXP0',47:'M2_SATA_A_N_PCIE_TXN0',49:'M2_SATA_A_P_PCIE_TXP0',50:'M2_PERST_N',52:'M2_CLKREQ_N',53:'M2_REFCLK_N',54:'M2_PEWake_N',55:'M2_REFCLK_P',68:'M2_SUSCLK',70:'M2_3V3',71:'POWER_GND',72:'M2_3V3',73:'POWER_GND',74:'M2_3V3'})}

def append_pad_metadata(text, nets, stem):
    def repl(m):
        n=m.group(1); body=m.group(0)
        if int(n) in nets:
            body=body[:-1] + f' (net "{nets[int(n)]}") (pinfunction "{nets[int(n)]}") (pintype "passive") (uuid "{uuid.uuid5(uuid.NAMESPACE_URL,stem+":"+n)}"))'
        return body
    return re.sub(r'\(pad "([0-9]+)"[^\n]*\)$', repl, text, flags=re.MULTILINE)
def pcb_footprint(mod, ref, x, y, nets):
    t=mod.read_text(); t=t.replace('(footprint "','(footprint "',1)
    t=t.replace(' (layer "F.Cu")','\n (layer "F.Cu")\n (at %g %g)'%(x,y),1)
    t=t.replace('(property "Reference" "REF**"','(property "Reference" "%s"'%ref,1)
    t=append_pad_metadata(t,nets,ref)
    t=t.rstrip(); t=t[:-1]+f'\n (uuid "{uuid.uuid5(uuid.NAMESPACE_URL,"PiSXMe:"+ref)}")\n)'
    return t
def main():
    text=BASE.read_text()
    # Replace only the old socket footprint; its old copper is retained as
    # historical context in this disposable candidate and is not promoted.
    s=text.index('(footprint "JAE_SM3ZS067U410ABR1000_BKEY"'); text=text[:s]+pcb_footprint(LIB/'TE_1-2199230-4_MKEY.kicad_mod','J3',220,165,MAPS['TE_1-2199230-4_MKEY.kicad_mod'][1])+text[s+len(balanced(text,s)):]
    additions=[]
    for fname,(ref,nets) in MAPS.items():
        if ref=='J3': continue
        additions.append(pcb_footprint(LIB/fname,ref,{'U11':150,'U12':165,'U13':180}[ref],150,nets))
    text=text.rstrip(); assert text.endswith(')')
    text=text[:-1]+'\n'+'\n'.join(additions)+'\n)\n'
    OUT.write_text(text); print(OUT)
if __name__=='__main__':main()
