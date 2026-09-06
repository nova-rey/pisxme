"""Connect both switched USB2 branches to their actual bridge endpoints."""
from pathlib import Path
P=Path(__file__).resolve().parent/'STORAGE.kicad_sch'
def main():
    s=P.read_text()
    for a,b in {'TUSB_USB2_DP':'BRIDGE_USB_DP','TUSB_USB2_DM':'BRIDGE_USB_DM',
                'JMS_USB2_DP':'USB_DP','JMS_USB2_DM':'USB_DM'}.items(): s=s.replace(a,b)
    P.write_text(s); print('reconciled storage USB2 selector ownership')
if __name__=='__main__': main()
