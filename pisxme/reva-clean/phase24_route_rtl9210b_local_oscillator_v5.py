#!/usr/bin/env python3
"""Native-coordinate oscillator/RSET route with separated QFN escapes."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_LOCAL_V2.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_LOCAL_OSCILLATOR_V5.kicad_pcb"


def main():
    text = BASE.read_text()
    ids = {n: int(c) for c, n in re.findall(r'\(net (\d+) "([^"]+)"\)', text)}

    def s(name, a, b, layer="F.Cu"):
        return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{layer}") (net {ids[name]}))'

    def v(name, p):
        return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net {ids[name]}))'

    routes = []
    # XTAL_IN stays on F.Cu after a leftward escape; it never crosses the
    # XTAL_OUT B.Cu corridor or the exposed QFN pad field.
    routes += [s("XTAL_IN", (76.05, 59.2), (74.8, 59.2)),
               s("XTAL_IN", (74.8, 59.2), (74.8, 57.5)),
               s("XTAL_IN", (74.8, 57.5), (69.3, 57.5)),
               s("XTAL_IN", (69.3, 57.5), (69.3, 55.0)),
               s("XTAL_IN", (69.3, 57.5), (66.4, 57.5)),
               s("XTAL_IN", (66.4, 57.5), (66.4, 55.0))]
    # XTAL_OUT transitions left of the QFN and uses B.Cu to reach both load
    # pads.  The final F.Cu dogbones are outside the XTAL_IN horizontal run.
    routes += [s("XTAL_OUT", (76.05, 59.6), (75.5, 59.6)),
               v("XTAL_OUT", (75.5, 59.6)),
               s("XTAL_OUT", (75.5, 59.6), (75.5, 56.5), "B.Cu"),
               s("XTAL_OUT", (75.5, 56.5), (70.7, 56.5), "B.Cu"),
               v("XTAL_OUT", (70.7, 56.5)),
               s("XTAL_OUT", (70.7, 56.5), (70.7, 55.0)),
               s("XTAL_OUT", (70.7, 56.5), (72.4, 56.5), "B.Cu"),
               v("XTAL_OUT", (72.4, 56.5)),
               s("XTAL_OUT", (72.4, 56.5), (72.4, 55.0))]
    # RSET keeps the known separated B.Cu corridor and uses a left QFN escape.
    routes += [s("RSET", (76.8, 58.05), (75.5, 58.05)),
               v("RSET", (75.5, 58.05)),
               s("RSET", (75.5, 58.05), (78.0, 49.0), "B.Cu"),
               s("RSET", (78.0, 49.0), (69.4, 49.0), "B.Cu"),
               v("RSET", (69.4, 49.0)),
               s("RSET", (69.4, 49.0), (69.4, 51.0))]
    text = text.replace('  (gr_rect ', '\n'.join(routes) + '\n  (gr_rect ', 1)
    OUT.write_text(text)
    print(OUT)


if __name__ == "__main__":
    main()
