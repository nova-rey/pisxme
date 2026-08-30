#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
    for name in ('ORIENTATION_TOP.kicad_pcb','ORIENTATION_BOTTOM.kicad_pcb'):
        t=(ROOT/name).read_text()
        assert 'NO ROUTING' in t and '(segment ' not in t and '(via ' not in t
        for anchor in ('V100_COOLER_BACKPLATE_ENVELOPE','PiSXMeRevAClean_SXM2_74221_101LF','M2_2280_RETENTION_ENVELOPE','Raspberry_Pi_5_Compute_Module'):
            assert anchor in t
    print('Phase 10 orientation audit: PASS; candidates=2; routing=0')
if __name__=='__main__': main()
