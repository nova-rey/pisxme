#!/usr/bin/env python3
"""V7: move the XTAL_OUT transition clear of the XTAL_IN escape."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_LOCAL_V2.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_LOCAL_OSCILLATOR_V7.kicad_pcb"

def main():
    text = BASE.read_text()
    ids = {n: int(c) for c, n in re.findall(r'\(net (\d+) "([^"]+)"\)', text)}
    def s(n,a,b,l="F.Cu"):
        return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net {ids[n]}))'
    def v(n,p):
        return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net {ids[n]}))'
    r = [
        s("XTAL_IN",(76.05,59.2),(73.0,59.2)), v("XTAL_IN",(73.0,59.2)),
        s("XTAL_IN",(73.0,59.2),(73.0,57.5),"B.Cu"), s("XTAL_IN",(73.0,57.5),(69.3,57.5),"B.Cu"),
        v("XTAL_IN",(69.3,57.5)), s("XTAL_IN",(69.3,57.5),(69.3,55.0)),
        s("XTAL_IN",(69.3,57.5),(66.4,57.5),"B.Cu"), v("XTAL_IN",(66.4,57.5)), s("XTAL_IN",(66.4,57.5),(66.4,55.0)),
        s("XTAL_OUT",(76.05,59.6),(74.0,59.6)), s("XTAL_OUT",(74.0,59.6),(74.0,60.0)), v("XTAL_OUT",(74.0,60.0)),
        s("XTAL_OUT",(74.0,60.0),(74.0,56.5),"B.Cu"), s("XTAL_OUT",(74.0,56.5),(70.7,56.5),"B.Cu"),
        v("XTAL_OUT",(70.7,56.5)), s("XTAL_OUT",(70.7,56.5),(70.7,55.0)),
        s("XTAL_OUT",(70.7,56.5),(72.4,56.5),"B.Cu"), v("XTAL_OUT",(72.4,56.5)), s("XTAL_OUT",(72.4,56.5),(72.4,55.0)),
        s("RSET",(76.8,58.05),(75.5,58.05)), v("RSET",(75.5,58.05)), s("RSET",(75.5,58.05),(80.0,58.05),"B.Cu"),
        s("RSET",(80.0,58.05),(80.0,49.0),"B.Cu"), s("RSET",(80.0,49.0),(69.4,49.0),"B.Cu"), v("RSET",(69.4,49.0)), s("RSET",(69.4,49.0),(69.4,51.0)),
    ]
    OUT.write_text(text.replace('  (gr_rect ', '\n'.join(r)+'\n  (gr_rect ', 1))
    print(OUT)
if __name__ == "__main__": main()
