#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
    t=(ROOT/'ACREAGE_FLOORPLAN.kicad_pcb').read_text()
    for z in ('POWER INPUT','REGULATORS','SERVICE / DEBUG','V100 MODULE / TOP COOLING DATUM','ETHERNET','STORAGE BRIDGE','M.2 2280 SERVICE'):
        assert z in t
    assert '(segment ' not in t and '(via ' not in t and 'NO ROUTING' in t
    assert '(gr_rect (start 0 0) (end 300 180)' in t
    assert '(end 300 180)' in t
    print('Phase 11/12 floorplan audit: PASS; acreage=300x180; routing=0; neighborhoods=7')
if __name__=='__main__': main()
