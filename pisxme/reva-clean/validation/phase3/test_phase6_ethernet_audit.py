#!/usr/bin/env python3
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def main():
    text=(ROOT/'ETHERNET.kicad_sch').read_text()
    assert text.count('property "MPN" "A70-112-331N126"')==1
    assert text.count('property "MPN" "TPD4E004DRYR"')==2
    for net in ('CM5_GBE_TD0_P','CM5_GBE_TD0_N','CM5_GBE_TD1_P','CM5_GBE_TD1_N','CM5_GBE_TD2_P','CM5_GBE_TD2_N','CM5_GBE_TD3_P','CM5_GBE_TD3_N','GBE_SHIELD'):
        assert net in text
    assert text.count('EDAC_A70_112_331N126_Ethernet')>=2
    assert text.count('TPD4E004DRYR')>=2
    print('Phase 6 Ethernet audit: PASS; MDI pairs=4; two 4-channel ESD arrays; shield=explicit')

if __name__=='__main__': main()
