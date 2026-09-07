#!/usr/bin/env python3
"""V9: dogleg PEDET around the inherited RTL_5V via without moving rails."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V9.kicad_pcb'
def main():
    text=BASE.read_text()
    pat=re.compile(r'(?ms)^\s*\((segment|via)\n.*?^\s*\)\n')
    text=pat.sub(lambda m:'' if '(net "PEDET")' in m.group(0) else m.group(0),text)
    def s(a,b,l): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net "PEDET"))'
    def v(p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "PEDET"))'
    r=[s((79.6,65.95),(79.6,68.5),'F.Cu'),v((79.6,68.5)),
       s((79.6,68.5),(68,68.5),'B.Cu'),s((68,68.5),(68,48),'B.Cu'),v((68,48)),
       s((68,48),(71,48),'F.Cu'),s((68,48),(68,43),'B.Cu'),v((68,43)),
       s((68,43),(68,40.6),'F.Cu'),s((68,40.6),(84,40.6),'F.Cu'),
       s((84,40.6),(84,42.2),'F.Cu'),s((84,42.2),(86,42.2),'F.Cu'),
       s((86,42.2),(86,40.6),'F.Cu'),s((86,40.6),(144,40.6),'F.Cu'),
       s((144,40.6),(144,61.5),'F.Cu'),s((144,61.5),(140.75,61.5),'F.Cu'),
       s((140.75,61.5),(140.75,62.725),'F.Cu')]
    text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1)
    OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
