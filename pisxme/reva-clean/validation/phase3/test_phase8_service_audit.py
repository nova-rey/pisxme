#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
    t=(ROOT/'SERVICE.kicad_sch').read_text()
    assert t.count('property "MPN" "10171746-00021LF"')==1
    assert t.count('property "MPN" "USB2 connector-boundary ESD"')==1
    assert t.count('property "Value" "5.1k Rd"')==2
    for n in ('SERVICE_USB2_DP','SERVICE_USB2_DM','SERVICE_VBUS_SENSE','SERVICE_RD_A','SERVICE_RD_B','SERVICE_GND'):
        assert n in t
    assert 'USB3' not in t.upper() and 'DRP' not in t.upper() and 'VBUS_SOURCE' not in t.upper()
    print('Phase 8 SERVICE audit: PASS; USB2 UFP, ESD, VBUS sense, Rd=2, source=0')
if __name__=='__main__': main()
