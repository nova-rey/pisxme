#!/usr/bin/env python3
"""Route PERST_N to the M-key socket and its test point."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_5V_1V1_SUPPORT_V6.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PERST.kicad_pcb'
def main():
 text=BASE.read_text(); net='PERST_N'
 def s(a,b): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "F.Cu") (net "{net}"))'
 r=[s((82.0,65.95),(82.0,72.0)),s((82.0,72.0),(136.0,72.0)),s((136.0,72.0),(136.0,70.275)),s((108.0,72.0),(108.0,78.0))]
 text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1); OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
