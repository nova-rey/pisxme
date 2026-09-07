#!/usr/bin/env python3
"""Move only the QFN-side oscillator transitions in the V3 fixture route."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_LOCAL_V2.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_LOCAL_OSCILLATOR_V4.kicad_pcb"


def main():
    text = BASE.read_text()
    ids = {n: int(c) for c, n in re.findall(r'\(net (\d+) "([^"]+)"\)', text)}

    def s(name, a, b, layer="F.Cu"):
        return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{layer}") (net {ids[name]}))'

    def v(name, p):
        return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net {ids[name]}))'

    routes = []
    # XTAL_IN: left transition, then B.Cu to pad-side vias below the row.
    routes += [s("XTAL_IN", (76.05, 59.2), (72.0, 59.2)), v("XTAL_IN", (72.0, 59.2)),
               s("XTAL_IN", (72.0, 59.2), (72.0, 56.5), "B.Cu"),
               s("XTAL_IN", (72.0, 56.5), (69.3, 56.5), "B.Cu"),
               v("XTAL_IN", (69.3, 56.5)), s("XTAL_IN", (69.3, 56.5), (66.4, 56.5), "B.Cu"),
               v("XTAL_IN", (66.4, 56.5)), s("XTAL_IN", (69.3, 56.5), (69.3, 55.0)),
               s("XTAL_IN", (66.4, 56.5), (66.4, 55.0))]
    # XTAL_OUT: route around the right side of the QFN, then above C2's ground pad.
    routes += [s("XTAL_OUT", (76.05, 59.6), (78.0, 59.6)),
               s("XTAL_OUT", (78.0, 59.6), (78.0, 53.0)),
               s("XTAL_OUT", (78.0, 53.0), (70.7, 53.0)),
               s("XTAL_OUT", (70.7, 53.0), (70.7, 55.0)),
               s("XTAL_OUT", (70.7, 53.0), (72.4, 53.0)),
               s("XTAL_OUT", (72.4, 53.0), (72.4, 55.0))]
    # RSET remains the V3 separated B.Cu corridor.
    routes += [s("RSET", (76.8, 58.05), (75.5, 57.0)), v("RSET", (75.5, 57.0)),
               s("RSET", (75.5, 57.0), (78.0, 49.0), "B.Cu"),
               s("RSET", (78.0, 49.0), (69.4, 49.0), "B.Cu"), v("RSET", (69.4, 49.0)),
               s("RSET", (69.4, 49.0), (69.4, 51.0))]
    text = text.replace('  (gr_rect ', '\n'.join(routes) + '\n  (gr_rect ', 1)
    OUT.write_text(text)
    print(OUT)


if __name__ == "__main__":
    main()
