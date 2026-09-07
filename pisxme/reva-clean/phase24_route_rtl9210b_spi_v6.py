#!/usr/bin/env python3
"""SPI V6 gives SPICLK a top perimeter corridor around the inverted pair."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_LOCAL_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SPI_V6.kicad_pcb'
def main():
    text=BASE.read_text(); ids={n:int(c) for c,n in re.findall(r'\(net (\d+) "([^"]+)"\)',text)}
    def s(n,a,b,l='F.Cu'): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net {ids[n]}))'
    def v(n,p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net {ids[n]}))'
    r=[]
    lanes=[('SPICS',(83.95,62.8),(85.0,62.8),(85.0,61.0),(86.0,61.0),(90.8,48.0)),('SPISO',(83.95,63.2),(85.5,63.2),(85.5,62.0),(87.0,62.0),(92.0,49.0)),('SPISO3',(83.95,63.6),(86.0,63.6),(86.0,63.0),(88.0,63.0),(98.0,50.0))]
    for n,src,a,b,sv,dv in lanes:
        r += [s(n,src,a),s(n,a,b),s(n,b,sv),v(n,sv),s(n,sv,(sv[0],dv[1]),'B.Cu'),s(n,(sv[0],dv[1]),dv,'B.Cu'),v(n,dv),s(n,dv,(dv[0],58.0))]
    n='SPICLK'; r += [s(n,(83.95,64.8),(84.5,64.8)),s(n,(84.5,64.8),(84.5,44.0)),s(n,(84.5,44.0),(96.8,44.0)),s(n,(96.8,44.0),(96.8,58.0))]
    n='SPISI'; r += [s(n,(83.95,65.2),(85.5,65.2)),s(n,(85.5,65.2),(85.5,70.0)),s(n,(85.5,70.0),(95.6,70.0)),s(n,(95.6,70.0),(95.6,46.0)),s(n,(95.6,46.0),(95.6,58.0))]
    OUT.write_text(text.replace('  (gr_rect ','\n'.join(r)+'\n  (gr_rect ',1)); print(OUT)
if __name__=='__main__': main()
