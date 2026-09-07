#!/usr/bin/env python3
"""V7: finish the localized RTL_5V and 3V3 transition corrections."""
from pathlib import Path
import re

HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V7.kicad_pcb'

def remove_net_objects(text, net):
    pat=re.compile(r'(?ms)^\s*\((segment|via)\n.*?^\s*\)\n')
    return pat.sub(lambda m:'' if f'(net "{net}")' in m.group(0) else m.group(0), text)

def main():
    text=remove_net_objects(BASE.read_text(),'RTL_5V')
    def s(n,a,b,l): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net "{n}"))'
    def v(n,p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "{n}"))'
    r=[]
    # Move the RTL_5V transition from (85,41), which PEDET must cross, to a
    # clear B.Cu channel at y=44.
    r += [s('RTL_5V',(83.2,65.95),(83.95,59.2),'F.Cu'),
          s('RTL_5V',(83.95,59.2),(85,59.2),'F.Cu'),s('RTL_5V',(85,59.2),(85,44),'F.Cu'),
          v('RTL_5V',(85,44)),s('RTL_5V',(85,44),(115,44),'B.Cu'),
          s('RTL_5V',(115,44),(115,50),'B.Cu'),s('RTL_5V',(115,50),(106.4,50),'B.Cu'),
          v('RTL_5V',(106.4,50)),s('RTL_5V',(106.4,50),(106.4,51),'F.Cu')]
    # Close the three vertical 3V3 branches onto the B.Cu bus with explicit
    # ordinary vias; the saved named-net graph remains the sole authority.
    r += [v('RTL_3V3',(93.2,42)),v('RTL_3V3',(99.2,42))]
    text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1)
    OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
