#!/usr/bin/env python3
"""SPI V3 with staggered source transitions outside the U1 pad row."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_LOCAL_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SPI_V3.kicad_pcb'
def main():
    text=BASE.read_text(); ids={n:int(c) for c,n in re.findall(r'\(net (\d+) "([^"]+)"\)',text)}
    def s(n,a,b,l='F.Cu'): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net {ids[n]}))'
    def v(n,p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net {ids[n]}))'
    r=[]
    # Staggered F.Cu fanout, then monotonic B.Cu channels.
    lanes=[('SPICS',(83.95,62.8),(84.6,62.8),(84.6,61.0),(85.5,61.0),(90.8,48.0)),
           ('SPISO',(83.95,63.2),(85.0,63.2),(85.0,62.0),(86.5,62.0),(92.0,49.0)),
           ('SPISO3',(83.95,63.6),(85.4,63.6),(85.4,63.0),(87.5,63.0),(98.0,50.0))]
    for n,src,a,b,sv,dv in lanes:
        r += [s(n,src,a),s(n,a,b),s(n,b,sv),v(n,sv),s(n,sv,(sv[0],dv[1]),'B.Cu'),s(n,(sv[0],dv[1]),dv,'B.Cu'),v(n,dv),s(n,dv,(dv[0],58.0))]
    n='SPICLK'; src=(83.95,64.8); a=(88.5,64.8); dv=(96.8,69.0)
    r += [s(n,src,a),s(n,a,(88.5,69.0)),s(n,(88.5,69.0),dv),v(n,dv),s(n,dv,(dv[0],58.0))]
    n='SPISI'; src=(83.95,65.2); a=(89.5,65.2); dv=(95.6,46.0)
    r += [s(n,src,a),s(n,a,(89.5,46.0)),s(n,(89.5,46.0),dv),v(n,dv),s(n,dv,(dv[0],58.0))]
    OUT.write_text(text.replace('  (gr_rect ','\n'.join(r)+'\n  (gr_rect ',1)); print(OUT)
if __name__=='__main__': main()
