#!/usr/bin/env python3
"""V3: replace the inherited RTL_1V1 B.Cu y=44 corridor with y=42."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_V3.kicad_pcb'
def remove_net_objects(text,net):
 pat=re.compile(r'(?ms)^\s*\((segment|via)\n.*?^\s*\)\n')
 return pat.sub(lambda m: '' if f'(net "{net}")' in m.group(0) else m.group(0),text)
def main():
 text=remove_net_objects(BASE.read_text(),'RTL_1V1')
 def s(a,b,l): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net "RTL_1V1"))'
 def v(p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "RTL_1V1"))'
 r=[s((82.8,58.05),(82.8,56.8),'F.Cu'),s((82.8,56.8),(83.5,56.8),'F.Cu'),v((83.5,56.8)),s((83.5,56.8),(83.5,42.0),'B.Cu'),s((83.5,42.0),(103.4,42.0),'B.Cu'),s((103.4,42.0),(103.4,50.0),'B.Cu'),v((103.4,50.0)),s((103.4,50.0),(103.4,51.0),'F.Cu')]
 text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1); OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
