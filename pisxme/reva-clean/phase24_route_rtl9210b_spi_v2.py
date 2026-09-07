#!/usr/bin/env python3
"""SPI support route using ordinary vias and separated outer-layer corridors."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_LOCAL_V2.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPI_V2.kicad_pcb"

def main():
    text = BASE.read_text()
    ids = {n:int(c) for c,n in re.findall(r'\(net (\d+) "([^"]+)"\)', text)}
    def s(n,a,b,l="F.Cu"):
        return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net {ids[n]}))'
    def v(n,p):
        return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net {ids[n]}))'
    r=[]
    # Monotonic B.Cu channels for the source/destination-order-preserving trio.
    for n,src,sv,dv in [
        ("SPICS",(83.95,62.8),(85.0,62.8),(90.8,55.5)),
        ("SPISO",(83.95,63.2),(85.5,63.2),(92.0,55.5)),
        ("SPISO3",(83.95,63.6),(86.0,63.6),(98.0,55.5)),
    ]:
        r += [s(n,src,sv),v(n,sv),s(n,sv,(sv[0],50.0),"B.Cu"),s(n,(sv[0],50.0),(dv[0],50.0),"B.Cu"),s(n,(dv[0],50.0),dv,"B.Cu"),v(n,dv),s(n,dv,(dv[0],58.0))]
    # The inverted pair endpoints use isolated F.Cu outer corridors.
    n="SPICLK"; src=(83.95,64.8); sv=(86.5,64.8); dv=(96.8,69.0)
    r += [s(n,src,sv),s(n,sv,(sv[0],69.0)),s(n,(sv[0],69.0),dv),v(n,dv),s(n,dv,(dv[0],58.0))]
    n="SPISI"; src=(83.95,65.2); sv=(87.5,65.2); dv=(95.6,46.0)
    r += [s(n,src,sv),s(n,sv,(sv[0],46.0)),s(n,(sv[0],46.0),dv),v(n,dv),s(n,dv,(dv[0],58.0))]
    OUT.write_text(text.replace('  (gr_rect ','\n'.join(r)+'\n  (gr_rect ',1))
    print(OUT)
if __name__ == '__main__': main()
