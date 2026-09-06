"""Fail-closed audit of the saved dual-mode storage schematic."""
from pathlib import Path
import argparse
from phase3_scaffold import balanced

REQUIRED={
 'U11':('JMS583-QHFA3A','JMS583_QFN64_8x8',('USB_DM','USB_DP','USB_TXP1','USB_RXP1','PCIE_RXN0','PCIE_RXP0','PCIE_TXN0','PCIE_TXP0','REFCLK_N','REFCLK_P','PCIE_RESET_N','PCIE_CLKREQ_N')),
 'U12':('HD3SS6126RUAR','HD3SS6126_RUA0042A',('USB_SEL','USB_OE_N','CM5_USB3_TX_P','CM5_USB3_RX_P','TUSB_SSTXP','TUSB_SSRXP','USB_TXP1','USB_RXP1','CM5_STORAGE_USB2_DP','CM5_STORAGE_USB2_DM')),
 'U13':('HD3SS3412RUAR','HD3SS3412_RUA0042A',('STORAGE_SEL','M2_SATA_A_P_PCIE_TXP0','M2_SATA_A_N_PCIE_TXN0','TUSB_SATA_TXP','TUSB_SATA_RXP','JMS_PCIE_TXP0','JMS_PCIE_RXP0')),
 'J3':('1-2199230-4','TE_1-2199230-4_MKEY',('M2_3V3','M2_GND','M2_SATA_B_P_PCIE_RXN0','M2_SATA_B_N_PCIE_RXP0','M2_SATA_A_N_PCIE_TXN0','M2_SATA_A_P_PCIE_TXP0','M2_PERST_N','M2_CLKREQ_N','M2_REFCLK_N','M2_REFCLK_P')),
}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input',nargs='?',default=str(Path(__file__).with_name('STORAGE.kicad_sch'))); ap.add_argument('--expect-missing',default=''); a=ap.parse_args()
    t=Path(a.input).read_text(); failures=[]
    if 'SM3ZS067U410ABR1000' in t or 'JAE_SM3ZS067U410ABR1000' in t: failures.append('obsolete B-key J3 remains')
    for ref,(mpn,fp,nets) in REQUIRED.items():
        token=f'(property "Reference" "{ref}"';
        if token not in t: failures.append(ref+' missing'); continue
        s=t.rfind('(symbol (lib_id',0,t.index(token)); b=t[s:s+len(balanced(t,s))]
        for needle in (f'"{mpn}"',f'PiSXMeRevAClean:{fp}'):
            if needle not in b: failures.append(ref+' missing '+needle)
        for net in nets:
            if f'(label "{net}"' not in t and f'(global_label "{net}"' not in t:
                failures.append(ref+' missing label '+net)
    if a.expect_missing and f'(label "{a.expect_missing}"' in t: failures.append('negative control did not remove '+a.expect_missing)
    for f in failures: print('FAIL',f)
    if failures: raise SystemExit(1)
    print('PASS dual-mode schematic instances, footprints, and required net labels')
if __name__=='__main__': main()
