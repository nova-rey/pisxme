#!/usr/bin/env python3
"""Route only crystal and RSET support on the relocated Path-B fixture."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_LOCAL_V2.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_LOCAL_OSCILLATOR.kicad_pcb"


def main():
    text = BASE.read_text()
    ids = {n: int(c) for c, n in re.findall(r'\(net (\d+) "([^"]+)"\)', text)}

    def seg(name, a, b):
        return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "F.Cu") (net {ids[name]}))'

    routes = []
    # XTAL_IN: U1.53 -> Y1.1 and C1.1.
    routes += [seg("XTAL_IN", (76.05, 59.2), (75.0, 59.2)),
               seg("XTAL_IN", (75.0, 59.2), (75.0, 54.5)),
               seg("XTAL_IN", (75.0, 54.5), (69.4, 54.5)),
               seg("XTAL_IN", (69.4, 54.5), (69.4, 55.0)),
               seg("XTAL_IN", (69.4, 54.5), (66.4, 54.5)),
               seg("XTAL_IN", (66.4, 54.5), (66.4, 55.0))]
    # XTAL_OUT: separate corridor and branch to C2.
    routes += [seg("XTAL_OUT", (76.05, 59.6), (74.0, 59.6)),
               seg("XTAL_OUT", (74.0, 59.6), (74.0, 53.5)),
               seg("XTAL_OUT", (74.0, 53.5), (70.6, 53.5)),
               seg("XTAL_OUT", (70.6, 53.5), (70.6, 55.0)),
               seg("XTAL_OUT", (70.6, 53.5), (72.4, 53.5)),
               seg("XTAL_OUT", (72.4, 53.5), (72.4, 55.0))]
    # RSET: top-side source pin to relocated R1.1.
    routes += [seg("RSET", (76.8, 58.05), (77.0, 58.05)),
               seg("RSET", (77.0, 58.05), (77.0, 50.0)),
               seg("RSET", (77.0, 50.0), (69.4, 50.0)),
               seg("RSET", (69.4, 50.0), (69.4, 51.0))]
    marker = '  (gr_rect '
    text = text.replace(marker, '\n'.join(routes) + '\n' + marker, 1)
    OUT.write_text(text)
    print(OUT)


if __name__ == "__main__":
    main()
