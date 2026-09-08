"""Create a disposable native PCB placement candidate for the new storage island.

This is deliberately a placement/authority fixture, not a claim of completed
routing. It starts from the selected storage macro ancestor and replaces only
J3/adds U8-U10 inside the storage acreage.
"""
from pathlib import Path
import re, uuid
from phase3_scaffold import balanced
from phase24_integrate_dual_mode_storage import JMS, USB, MUX, M2

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_BCU_INTEGRATED_ASTAR_V3.kicad_pcb'
OUT=ROOT/'PHASE24_DUAL_MODE_STORAGE_PLACEMENT.kicad_pcb'
LIB=ROOT/'PiSXMe_RevA_Clean.pretty'

MAPS={
 # Reuse the reviewed schematic pin maps.  Do not maintain a second partial
 # U11 map here: it previously created stale JMS_XIN/JMS_LXO aliases that
 # diverged from the native schematic nets.
 'JMS583_QFN64_8x8.kicad_mod':('U11',JMS),
 'HD3SS6126_RUA0042A.kicad_mod':('U12',{6:'USB_SEL_OE_N',7:'CM5_USB2_DN',8:'CM5_USB2_DP',9:'STORAGE_USB_SEL',10:'POWER_GND',11:'CM5_USB3_TXP',12:'CM5_USB3_TXN',15:'CM5_USB3_RXP',16:'CM5_USB3_RXN',22:'JMS_USB3_RXN',23:'JMS_USB3_RXP',24:'JMS_USB3_TXN',25:'JMS_USB3_TXP',26:'TUSB_USB3_RXN',27:'TUSB_USB3_RXP',28:'TUSB_USB3_TXN',29:'TUSB_USB3_TXP',31:'TUSB_USB2_DP',32:'TUSB_USB2_DN',33:'JMS_USB2_DP',34:'JMS_USB2_DN',13:'STORAGE_3V3',20:'STORAGE_3V3',30:'STORAGE_3V3'}),
 'HD3SS3412_RUA0042A.kicad_mod':('U13',{2:'M2_PCIE_TXP0',3:'M2_PCIE_RXP0',5:'STORAGE_3V3',6:'M2_PCIE_TXP1',7:'M2_PCIE_RXP1',9:'STORAGE_SEL',10:'POWER_GND',11:'M2_PCIE_TXP2',12:'M2_PCIE_RXP2',15:'M2_PCIE_TXP3',16:'M2_PCIE_RXP3',22:'JMS_PCIE_TXN0',23:'JMS_PCIE_TXP0',24:'JMS_PCIE_RXN0',25:'JMS_PCIE_RXP0',26:'TUSB_SATA_RXN',27:'TUSB_SATA_RXP',28:'TUSB_SATA_TXN',29:'TUSB_SATA_TXP',30:'STORAGE_3V3'}),
 'TE_1-2199230-4_MKEY.kicad_mod':('J3',{2:'M2_3V3',3:'POWER_GND',4:'M2_3V3',41:'M2_SATA_B_P_PCIE_RXN0',43:'M2_SATA_B_N_PCIE_RXP0',47:'M2_SATA_A_N_PCIE_TXN0',49:'M2_SATA_A_P_PCIE_TXP0',50:'M2_PERST_N',52:'M2_CLKREQ_N',53:'M2_REFCLK_N',54:'M2_PEWake_N',55:'M2_REFCLK_P',68:'M2_SUSCLK',70:'M2_3V3',71:'POWER_GND',72:'M2_3V3',73:'POWER_GND',74:'M2_3V3'}),
 'SOT-23-5.kicad_mod':('U14',{2:'MODE_IN',3:'POWER_GND',4:'STORAGE_SEL',5:'STORAGE_3V3'}),
 'MODE_JUMPER_1x04.kicad_mod':('J5',{1:'FORCE_SATA',2:'AUTO_PEDET',3:'FORCE_NVME',4:'MODE_IN'}),
 'R_0402_1005Metric.kicad_mod':('R80',{1:'JMS_REXT',2:'POWER_GND'}),
 'L_2520_6332Metric.kicad_mod':('L10',{1:'LXO',2:'JMS_VDDREG_5V'}),
 'Crystal_3225_4Pad.kicad_mod':('Y10',{1:'XIN',2:'XOUT',3:'POWER_GND',4:'POWER_GND'})}
SUPPORT_PCB = {
 'C80':{1:'JMS_AVDD33',2:'POWER_GND'},'C81':{1:'JMS_VCCO',2:'POWER_GND'},
 'C82':{1:'JMS_VCCK',2:'POWER_GND'},'C83':{1:'JMS_AVDDL',2:'POWER_GND'},
 'C84':{1:'JMS_XAVDDH',2:'POWER_GND'},'R81':{1:'JMS_RESET_N',2:'STORAGE_3V3'},
 'C85':{1:'JMS_RESET_N',2:'POWER_GND'},'R82':{1:'VBUS',2:'JMS_VBUS_SENSE'},
 'R83':{1:'JMS_VBUS_SENSE',2:'POWER_GND'},'C86':{1:'USB_TXP1',2:'JMS_USB3_TXP'},
 'C87':{1:'USB_TXN1',2:'JMS_USB3_TXN'},'C88':{1:'USB_TXP2',2:'JMS_USB3_TXP2'},
 'C89':{1:'USB_TXN2',2:'JMS_USB3_TXN2'},'C90':{1:'PCIE_TXP0',2:'JMS_PCIE_TXP0'},
 'C91':{1:'PCIE_TXN0',2:'JMS_PCIE_TXN0'},'C92':{1:'PCIE_TXP1',2:'JMS_PCIE_TXP1'},
 'C93':{1:'PCIE_TXN1',2:'JMS_PCIE_TXN1'}
}
SUPPORT_PCB.update({
 'R24':{1:'BRIDGE_R1',2:'BRIDGE_R1RTN'},
 'R32':{1:'CM5_5V',2:'BRIDGE_USB_VBUS'},
 'R33':{1:'BRIDGE_USB_VBUS',2:'POWER_GND'},
})

# Use the same reviewed schematic maps for the disposable PCB metadata. The
# earlier placement probe used abbreviated aliases and is not authority.
MAPS['JMS583_QFN64_8x8.kicad_mod'] = ('U11', JMS)
MAPS['HD3SS6126_RUA0042A.kicad_mod'] = ('U12', USB)
 # Pad 43 is the package exposed thermal pad, not a signal pin. TI's RUA
 # package drawing requires it soldered to the PCB; assign the saved PCB pad
 # to the established power-ground net without inventing a schematic pin.
MAPS['HD3SS3412_RUA0042A.kicad_mod'] = ('U13', {**MUX, 43:'POWER_GND'})
MAPS['TE_1-2199230-4_MKEY.kicad_mod'] = ('J3', M2)

def append_pad_metadata(text, nets, stem):
    # Do not use line-based parsing: KiCad footprint pads may wrap across
    # lines. Walk balanced pad expressions and insert metadata before the pad
    # close, preserving the source geometry verbatim.
    out=[]; pos=0
    for m in re.finditer(r'\(pad "([0-9]+)"', text):
        start=m.start(); end=start+len(balanced(text,start)); out.append(text[pos:start])
        block=text[start:end]; n=m.group(1)
        if int(n) in nets:
            block=block[:-1] + f' (net "{nets[int(n)]}") (pinfunction "{nets[int(n)]}") (pintype "passive") (uuid "{uuid.uuid5(uuid.NAMESPACE_URL,stem+":"+n)}")' + ')'
        out.append(block); pos=end
    out.append(text[pos:]); return ''.join(out)
def pcb_footprint(mod, ref, x, y, nets):
    t=mod.read_text(); t=t.replace('(footprint "','(footprint "',1)
    t=t.replace(' (layer "F.Cu")','\n (layer "F.Cu")\n (at %g %g)'%(x,y),1)
    t=re.sub(r'\(property "Reference" "[^"]+"', '(property "Reference" "%s"' % ref, t, count=1)
    t=append_pad_metadata(t,nets,ref)
    t=t.rstrip(); t=t[:-1]+f'\n (uuid "{uuid.uuid5(uuid.NAMESPACE_URL,"PiSXMe:"+ref)}")\n)'
    return t
def remove_existing_refs(text, refs):
    """Remove donor footprints whose references are owned by this generator."""
    spans=[]
    for m in re.finditer(r'\(footprint ', text):
        start=m.start(); block=text[start:start+len(balanced(text,start))]
        if any(f'(property "Reference" "{ref}"' in block for ref in refs):
            spans.append((start,start+len(block)))
    for start,end in reversed(spans): text=text[:start]+text[end:]
    return text
def main():
    text=BASE.read_text()
    owned=set(ref for _,(ref,_) in MAPS.items()) | set(SUPPORT_PCB)
    text=remove_existing_refs(text, owned)
    # Replace only the old socket footprint; its old copper is retained as
    # historical context in this disposable candidate and is not promoted.
    legacy='(footprint "JAE_SM3ZS067U410ABR1000_BKEY"'
    if legacy in text:
        s=text.index(legacy); text=text[:s]+pcb_footprint(LIB/'TE_1-2199230-4_MKEY.kicad_mod','J3',220,165,MAPS['TE_1-2199230-4_MKEY.kicad_mod'][1])+text[s+len(balanced(text,s)):]
    else:
        text=text.rstrip()[:-1]+pcb_footprint(LIB/'TE_1-2199230-4_MKEY.kicad_mod','J3',220,165,MAPS['TE_1-2199230-4_MKEY.kicad_mod'][1])+'\n)\n'
    additions=[]
    for fname,(ref,nets) in MAPS.items():
        if ref=='J3': continue
        # J5 is deliberately outboard of the M-key socket.  At the former
        # (230,165) origin its FORCE_NVME pad landed in J3's M2_3V3 pad
        # column; this is a physical placement collision, not a net issue.
        x={'U11':140,'U12':155,'U13':180,'U14':210,'J5':245,
           'R80':131,'L10':136,'Y10':145}[ref]
        y={'U11':135,'U12':135,'U13':135,'U14':150,'J5':150,
           'R80':125,'L10':125,'Y10':125}[ref]
        additions.append(pcb_footprint(LIB/fname,ref,x,y,nets))
    for ref,nets in SUPPORT_PCB.items():
        fname = 'C_0603_1608Metric.kicad_mod' if ref == 'C44' else ('Crystal_3225_4Pad.kicad_mod' if ref == 'Y2' else ('L_2520_6332Metric.kicad_mod' if ref == 'L2' else ('R_0402_1005Metric.kicad_mod' if ref.startswith('R') else 'C_0402_1005Metric.kicad_mod')))
        # Keep the generated support field inside the 300 x 180 mm acreage
        # outline.  The former 300+ mm grid silently put C80..R33 outside
        # the board, making every subsequent routing/DRC result misleading.
        idx=len(additions)
        x=120+(idx%6)*3.5; y=112+(idx//6)*2.5
        additions.append(pcb_footprint(LIB/fname,ref,x,y,nets))
    text=text.rstrip(); assert text.endswith(')')
    text=text[:-1]+'\n'+'\n'.join(additions)+'\n)\n'
    OUT.write_text(text); print(OUT)
if __name__=='__main__':main()
