#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
    v=(ROOT/'PiSXMe_RevA_Clean.pretty/V100_COOLER_BACKPLATE_ENVELOPE.kicad_mod').read_text()
    m=(ROOT/'PiSXMe_RevA_Clean.pretty/M2_2280_RETENTION_ENVELOPE.kicad_mod').read_text()
    s=(ROOT/'PiSXMe_RevA_Clean.pretty/PiSXMeRevAClean_SXM2_74221_101LF.kicad_mod').read_text()
    assert '150x95mm' in v and '+45mm' in v
    assert '2280' in m and '2242' in m
    assert '(fp_rect (start -33.5 -13.77)' in s
    assert s.count('(pad "')==400
    print('Phase 9 mechanics audit: PASS; V100 envelope=150x95/+45mm; M.2=2280; SXM2 pads=400')
if __name__=='__main__': main()
