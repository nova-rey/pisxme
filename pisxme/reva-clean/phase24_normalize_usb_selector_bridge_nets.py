"""Normalize U12-to-JMS583 USB3 nets to the actual bridge pin names."""
from pathlib import Path
P=Path(__file__).resolve().parent/'STORAGE.kicad_sch'
def main():
    s=P.read_text()
    for a,b in {'JMS_SSRXN':'USB_RXN1','JMS_SSRXP':'USB_RXP1','JMS_SSTXN':'USB_TXN1','JMS_SSTXP':'USB_TXP1'}.items():
        s=s.replace(a,b)
    P.write_text(s); print('normalized selector bridge USB3 names')
if __name__=='__main__': main()
