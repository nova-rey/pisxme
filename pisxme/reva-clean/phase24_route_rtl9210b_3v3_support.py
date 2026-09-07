#!/usr/bin/env python3
"""Route the local RTL_3V3 support bus on the isolated Path-B fixture."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SPI_V7_GND_PLANES_V3.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_SUPPORT.kicad_pcb'
def main():
 text=BASE.read_text(); net='RTL_3V3'
 def s(a,b): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.250) (layer "F.Cu") (net "{net}"))'
 r=[s((93.2,58.0),(93.2,42.0)),s((99.2,58.0),(99.2,42.0)),s((100.4,51.0),(100.4,42.0)),s((110.6,51.0),(110.6,42.0)),s((113.6,51.0),(113.6,42.0)),s((93.2,42.0),(113.6,42.0))]
 text=re.sub(r'(?m)^(\s*\(gr_rect\b)', '\n'.join(r)+'\n\\1', text, count=1)
 OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
