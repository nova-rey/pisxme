#!/usr/bin/env python3
"""V10: QFN-safe RTL_5V departure repair on the V6 control baseline."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V10.kicad_pcb'
def main():
    text=BASE.read_text()
    pat=re.compile(r'(?ms)^\s*\((segment|via)\n.*?^\s*\)\n')
    text=pat.sub(lambda m:'' if '(net "RTL_5V")' in m.group(0) else m.group(0),text)
    def s(a,b,l): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net "RTL_5V"))'
    def v(p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "RTL_5V"))'
    r=[s((83.2,65.95),(83.2,68),'F.Cu'),v((83.2,68)),s((83.2,68),(86,68),'B.Cu'),
       s((86,68),(86,44),'B.Cu'),v((86,44)),s((86,44),(115,44),'B.Cu'),
       s((115,44),(115,50),'B.Cu'),s((115,50),(106.4,50),'B.Cu'),v((106.4,50)),
       s((106.4,50),(106.4,51),'F.Cu')]
    text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1)
    OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
