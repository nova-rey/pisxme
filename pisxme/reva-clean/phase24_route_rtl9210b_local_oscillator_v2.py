#!/usr/bin/env python3
"""Native-coordinate oscillator/RSET escape with ordinary layer transitions."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_LOCAL_V2.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_LOCAL_OSCILLATOR_V2.kicad_pcb"


def main():
    text = BASE.read_text()
    ids = {n: int(c) for c, n in re.findall(r'\(net (\d+) "([^"]+)"\)', text)}

    def seg(name, a, b, layer="F.Cu"):
        return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{layer}") (net {ids[name]}))'

    def via(name, p):
        return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net {ids[name]}))'

    routes = []
    # XTAL_IN remains on F.Cu, but branches above the capacitor pad row.
    routes += [seg("XTAL_IN", (76.05, 59.2), (75.0, 59.2)),
               seg("XTAL_IN", (75.0, 59.2), (75.0, 54.5)),
               seg("XTAL_IN", (75.0, 54.5), (69.3, 54.5)),
               seg("XTAL_IN", (69.3, 54.5), (69.3, 55.0)),
               seg("XTAL_IN", (69.3, 54.5), (69.3, 53.5)),
               seg("XTAL_IN", (69.3, 53.5), (66.4, 53.5)),
               seg("XTAL_IN", (66.4, 53.5), (66.4, 55.0))]

    # XTAL_OUT uses B.Cu for the crossing corridor, with F.Cu dogbones at the
    # QFN and the two support pads; no via is placed in a pad.
    routes += [seg("XTAL_OUT", (76.05, 59.6), (74.5, 59.6)), via("XTAL_OUT", (74.5, 59.6)),
               seg("XTAL_OUT", (74.5, 59.6), (72.4, 52.5), "B.Cu"),
               seg("XTAL_OUT", (72.4, 52.5), (70.7, 52.5), "B.Cu"),
               via("XTAL_OUT", (72.4, 52.5)), via("XTAL_OUT", (70.7, 52.5)),
               seg("XTAL_OUT", (72.4, 52.5), (72.4, 55.0)),
               seg("XTAL_OUT", (70.7, 52.5), (70.7, 55.0))]

    # RSET exits left from U1.51, then uses a B.Cu corridor to R1.1.
    routes += [seg("RSET", (76.8, 58.05), (75.0, 57.0)), via("RSET", (75.0, 57.0)),
               seg("RSET", (75.0, 57.0), (69.4, 49.5), "B.Cu"),
               via("RSET", (69.4, 49.5)), seg("RSET", (69.4, 49.5), (69.4, 51.0))]

    marker = '  (gr_rect '
    text = text.replace(marker, '\n'.join(routes) + '\n' + marker, 1)
    OUT.write_text(text)
    print(OUT)


if __name__ == "__main__":
    main()
