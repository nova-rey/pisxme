#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
    t=(ROOT/'STORAGE.kicad_sch').read_text()
    assert t.count('property "MPN" "TUSB9261IPVP"')==1
    assert t.count('property "MPN" "SM3ZS067U410ABR1000"')==1
    for n in ('CM5_USB3_TX_P','CM5_USB3_TX_N','CM5_USB3_RX_P','CM5_USB3_RX_N','BRIDGE_SATA_TX_P','BRIDGE_SATA_TX_N','BRIDGE_SATA_RX_P','BRIDGE_SATA_RX_N','M2_3V3'):
        assert n in t
    assert 'NVME' not in t.upper() and 'SERVICE_USB2' not in t
    assert t.count('JAE_SM3ZS067U410ABR1000')>=2
    print('Phase 7 storage audit: PASS; USB3-only bridge path, SATA-only B-key M.2, NVMe=excluded')
if __name__=='__main__': main()
