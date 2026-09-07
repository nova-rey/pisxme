#!/usr/bin/env python3
"""Route only low-speed RTL9210B bring-up support nets on a disposable copy."""
from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_BRINGUP_FIXTURE.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_BRINGUP_SUPPORT_ROUTED.kicad_pcb"


def net_ids(text: str) -> dict[str, int]:
    return {name: int(code) for code, name in re.findall(r'\(net (\d+) "([^"]+)"\)', text)}


def seg(code: int, a: tuple[float, float], b: tuple[float, float], width: float = 0.15) -> str:
    return (f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) '
            f'(width {width:.3f}) (layer "F.Cu") (net {code}))')


def path(code: int, points: list[tuple[float, float]]) -> list[str]:
    return [seg(code, a, b) for a, b in zip(points, points[1:])]


def main() -> None:
    text = BASE.read_text()
    ids = net_ids(text)
    required = {name: ids[name] for name in ("XTAL_IN", "XTAL_OUT", "RSET", "SPICS", "SPISO", "SPISI", "SPICLK", "SPISO3")}
    routes: list[str] = []

    # Crystal and load capacitors.  Separate vertical corridors keep the two
    # oscillator nets independent and leave the QFN body/thermal pad clear.
    routes += path(required["XTAL_IN"], [(76.05, 59.2), (74.0, 59.2), (74.0, 54.0), (87.4, 54.0), (87.4, 48.0)])
    routes += path(required["XTAL_IN"], [(87.4, 54.0), (90.4, 54.0), (90.4, 48.0)])
    routes += path(required["XTAL_OUT"], [(76.05, 59.6), (73.0, 59.6), (73.0, 55.5), (88.6, 55.5), (88.6, 48.0)])
    routes += path(required["XTAL_OUT"], [(88.6, 55.5), (93.4, 55.5), (93.4, 48.0)])

    # RSET has a dedicated upper corridor.
    routes += path(required["RSET"], [(76.8, 58.05), (72.0, 58.05), (72.0, 52.0), (96.4, 52.0), (96.4, 48.0)])

    # SPI source fanout.  Source x channels and target y channels are ordered
    # so each channel terminates before the next horizontal corridor; this is
    # intentionally a small, inspectable fixture route rather than an A* claim.
    spi = [
        ("SPICS", (83.95, 62.8), 86.0, 42.0, (99.8, 48.0)),
        ("SPISO", (83.95, 63.2), 87.0, 43.0, (101.0, 48.0)),
        ("SPISI", (83.95, 65.2), 88.0, 44.0, (104.6, 48.0)),
        ("SPICLK", (83.95, 64.8), 89.0, 45.0, (105.8, 48.0)),
        ("SPISO3", (83.95, 63.6), 90.0, 46.0, (107.0, 48.0)),
    ]
    for name, source, channel_x, channel_y, target in spi:
        routes += path(required[name], [source, (channel_x, source[1]), (channel_x, channel_y), (target[0], channel_y), target])

    marker = '  (gr_rect '
    if marker not in text:
        raise SystemExit("fixture outline marker not found")
    text = text.replace(marker, '\n'.join(routes) + '\n' + marker, 1)
    OUT.write_text(text)
    print(OUT)


if __name__ == "__main__":
    main()
