#!/usr/bin/env python3
"""Try an ordinary-via/B.Cu SPI escape on the isolated RTL9210B fixture."""
from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_BRINGUP_FIXTURE.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPI_BCU_FIXTURE.kicad_pcb"


def ids(text: str) -> dict[str, int]:
    return {n: int(c) for c, n in re.findall(r'\(net (\d+) "([^"]+)"\)', text)}


def seg(code: int, a, b, layer: str, width=0.2) -> str:
    return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width {width:.3f}) (layer "{layer}") (net {code}))'


def via(code: int, p) -> str:
    return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.300) (drill 0.150) (layers "F.Cu" "B.Cu") (net {code}))'


def main() -> None:
    text = BASE.read_text()
    n = ids(text)
    # Source pads on U1 right edge, destination pads on U2 top row.  The
    # ordered channel heights prevent the B.Cu fanout corridors crossing.
    lanes = [
        ("SPICS", (83.950, 62.800), (85.000, 62.800), (99.800, 48.000), (98.800, 42.000)),
        ("SPISO", (83.950, 63.200), (85.250, 63.200), (101.000, 48.000), (100.000, 43.000)),
        ("SPISI", (83.950, 65.200), (85.500, 65.200), (104.600, 48.000), (103.600, 44.000)),
        ("SPICLK", (83.950, 64.800), (85.750, 64.800), (105.800, 48.000), (104.800, 45.000)),
        ("SPISO3", (83.950, 63.600), (86.000, 63.600), (107.000, 48.000), (106.000, 46.000)),
    ]
    routes: list[str] = []
    for name, source, source_via, target, target_via in lanes:
        code = n[name]
        routes += [seg(code, source, source_via, "F.Cu"), via(code, source_via)]
        routes += [seg(code, source_via, (source_via[0], target_via[1]), "B.Cu"),
                   seg(code, (source_via[0], target_via[1]), target_via, "B.Cu"), via(code, target_via),
                   seg(code, target_via, target, "F.Cu")]
    marker = '  (gr_rect '
    text = text.replace(marker, '\n'.join(routes) + '\n' + marker, 1)
    OUT.write_text(text)
    print(OUT)


if __name__ == "__main__":
    main()
