#!/usr/bin/env python3
"""V3: move both power transitions clear of the QFN/other-net corridors."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_3V3_SUPPORT.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_5V_1V1_SUPPORT_V3.kicad_pcb'
def main():
 text=BASE.read_text()
 def s(net,a,b,layer): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{layer}") (net "{net}"))'
 def v(net,p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "{net}"))'
 r=[]
 r += [s('RTL_5V',(83.95,59.2),(85.0,59.2),'F.Cu'),s('RTL_5V',(85.0,59.2),(85.0,41.0),'F.Cu'),v('RTL_5V',(85.0,41.0)),s('RTL_5V',(85.0,41.0),(115.0,41.0),'B.Cu'),s('RTL_5V',(115.0,41.0),(115.0,51.0),'B.Cu'),s('RTL_5V',(115.0,51.0),(107.4,51.0),'B.Cu'),v('RTL_5V',(107.4,51.0)),s('RTL_5V',(107.4,51.0),(106.4,51.0),'F.Cu')]
 r += [s('RTL_1V1',(82.8,58.05),(82.8,59.0),'F.Cu'),s('RTL_1V1',(82.8,59.0),(83.5,59.0),'F.Cu'),v('RTL_1V1',(83.5,59.0)),s('RTL_1V1',(83.5,59.0),(83.5,44.0),'B.Cu'),s('RTL_1V1',(83.5,44.0),(103.4,44.0),'B.Cu'),s('RTL_1V1',(103.4,44.0),(103.4,50.0),'B.Cu'),v('RTL_1V1',(103.4,50.0)),s('RTL_1V1',(103.4,50.0),(103.4,51.0),'F.Cu')]
 text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1); OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
