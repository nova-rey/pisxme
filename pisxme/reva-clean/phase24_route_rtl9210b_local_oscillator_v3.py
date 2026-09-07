#!/usr/bin/env python3
"""Separate oscillator/RSET corridors by layer and pad-side approach."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_LOCAL_V2.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_LOCAL_OSCILLATOR_V3.kicad_pcb"


def main():
    text = BASE.read_text()
    ids = {n: int(c) for c, n in re.findall(r'\(net (\d+) "([^"]+)"\)', text)}

    def s(name, a, b, layer="F.Cu"):
        return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{layer}") (net {ids[name]}))'

    def v(name, p):
        return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net {ids[name]}))'

    routes = []
    # XTAL_IN on B.Cu, with pad approaches from below the support row.
    routes += [s("XTAL_IN", (76.05, 59.2), (74.0, 59.2)), v("XTAL_IN", (74.0, 59.2)),
               s("XTAL_IN", (74.0, 59.2), (74.0, 56.5), "B.Cu"),
               s("XTAL_IN", (74.0, 56.5), (69.3, 56.5), "B.Cu"),
               v("XTAL_IN", (69.3, 56.5)), s("XTAL_IN", (69.3, 56.5), (66.4, 56.5), "B.Cu"),
               v("XTAL_IN", (66.4, 56.5)), s("XTAL_IN", (69.3, 56.5), (69.3, 55.0)),
               s("XTAL_IN", (66.4, 56.5), (66.4, 55.0))]
    # XTAL_OUT stays on F.Cu above the XTAL_IN pad approaches.
    routes += [s("XTAL_OUT", (76.05, 59.6), (74.0, 59.6)),
               s("XTAL_OUT", (74.0, 59.6), (74.0, 53.0)),
               s("XTAL_OUT", (74.0, 53.0), (70.7, 53.0)),
               s("XTAL_OUT", (70.7, 53.0), (70.7, 55.0)),
               s("XTAL_OUT", (70.7, 53.0), (72.4, 53.0)),
               s("XTAL_OUT", (72.4, 53.0), (72.4, 55.0))]
    # RSET uses a separate B.Cu upper-right corridor.
    routes += [s("RSET", (76.8, 58.05), (75.5, 57.0)), v("RSET", (75.5, 57.0)),
               s("RSET", (75.5, 57.0), (78.0, 49.0), "B.Cu"),
               s("RSET", (78.0, 49.0), (69.4, 49.0), "B.Cu"), v("RSET", (69.4, 49.0)),
               s("RSET", (69.4, 49.0), (69.4, 51.0))]

    text = text.replace('  (gr_rect ', '\n'.join(routes) + '\n  (gr_rect ', 1)
    OUT.write_text(text)
    print(OUT)


if __name__ == "__main__":
    main()
