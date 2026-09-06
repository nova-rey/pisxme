#!/usr/bin/env python3
"""Audit support circuitry present in the retained RTL9210B reference netlist.

This is deliberately a corroborating-source audit.  It proves what the
native KiCad export contains; it does not promote the WIP community design to
Path-B production authority and it does not synthesize missing connections.
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "authority-inventory" / "rtl9210b"
XML = ROOT / "RTL9210B_0.xml"


def parse(path: Path):
    root = ET.parse(path).getroot()
    comps = {}
    for comp in root.findall(".//comp"):
        ref = comp.get("ref")
        if ref:
            comps[ref] = {
                "value": comp.findtext("value") or "",
                "footprint": comp.findtext("footprint") or "",
            }
    nets = {}
    for net in root.findall(".//nets/net"):
        name = net.get("name") or ""
        nets[name] = {
            (node.get("ref"), node.get("pin"), node.get("pinfunction") or "")
            for node in net.findall("node")
        }
    return comps, nets


def require(condition: bool, message: str):
    if not condition:
        raise AssertionError(message)


def audit(path: Path):
    comps, nets = parse(path)

    # Values are evidence from the WIP source, not accepted production BOM.
    expected_components = {
        "U2": "RTL9210B-CG",
        "U1": "25MHz 10pF",
        "CN3": "W25Q128FVIQ_Connector",
        "U3": "MIC2545A-1YM",
        "U12": "MIC2545A-2YM-TR",
        "L5": "1uH",
        "R17": "12k",
        "R15": "76.8",
        "R16": "76.8",
    }
    for ref, value in expected_components.items():
        require(ref in comps, f"missing corroborating component {ref}")
        require(comps[ref]["value"] == value,
                f"{ref} value changed: {comps[ref]['value']!r} != {value!r}")

    def has(net: str, ref: str, pin: str):
        require(net in nets, f"missing net {net}")
        require(any(r == ref and p == pin for r, p, _ in nets[net]),
                f"{ref}.{pin} absent from {net}")

    # USB, shared lane 0, PCIe reference/sidebands, PEDET and reset.
    for net, ref, pin in (
        ("/USB2.0_D+", "U2", "37"),
        ("/USB2.0_D-", "U2", "38"),
        ("/USB3.0_TX+", "U2", "41"),
        ("/USB3.0_TX-", "U2", "42"),
        ("/USB3.0_RX+", "U2", "46"),
        ("/USB3.0_RX-", "U2", "47"),
        ("/PCIE_TXO_0+", "U2", "68"),
        ("/PCIE_TXO_0-", "U2", "67"),
        ("/PCIE_RXI0+", "U2", "64"),
        ("/PCIE_RXI0-", "U2", "65"),
        ("/PCIE_REFCLK+", "U2", "61"),
        ("/PCIE_REFCLK-", "U2", "62"),
        ("/PERST#", "U2", "14"),
        ("/CLKREQ#", "U2", "13"),
        ("/PDET", "U2", "8"),
        ("/ISOLATEB", "U2", "12"),
    ):
        has(net, ref, pin)

    # Controller support: crystal, flash, RSET, reset RC and internal rails.
    for net, endpoints in {
        "/XTALI": (("U2", "53"), ("U1", "1")),
        "/XTALO": (("U2", "54"), ("U1", "2")),
        "/SPI_CS": (("U2", "24"), ("CN3", "1")),
        "/SPI_CLK": (("U2", "19"), ("CN3", "6")),
        "/SPI_SI": (("U2", "18"), ("CN3", "5")),
        "/SPI_SO": (("U2", "23"), ("CN3", "2")),
        "/SPI_WP": (("U2", "21"), ("CN3", "3")),
        "/SPI_HD": (("U2", "22"), ("CN3", "7")),
        ("Net-(U2-RSET)" if "Net-(U2-RSET)" in nets else "Net-(U2-RSET)"): (("U2", "51"), ("R17", "1")),
        ("Net-(U2-RST_INPIN/NC)" if "Net-(U2-RST_INPIN/NC)" in nets else "Net-(U2-RST_INPIN/NC)"): (("U2", "3"), ("R12", "1")),
        ("Net-(U2-SWR_5TO1_OUT)" if "Net-(U2-SWR_5TO1_OUT)" in nets else "Net-(U2-SWR_5TO1_OUT)"): (("U2", "16"), ("L5", "2")),
    }.items():
        for ref, pin in endpoints:
            has(net, ref, pin)

    # The WIP source explicitly leaves these pins unconnected; preserve that
    # fact for review instead of treating it as a safe Path-B decision.
    unconnected = {ref + "." + pin for net in nets if net.startswith("unconnected-(")
                  for ref, pin, _ in nets[net]}
    for pin in ("5", "6", "9", "10", "27", "28", "43", "44", "48", "49"):
        require("U2." + pin in unconnected,
                f"expected WIP unconnected U2.{pin} evidence is absent")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--negative-control", action="store_true")
    args = parser.parse_args()
    if not XML.exists():
        print(f"FAIL missing {XML}")
        return 1
    try:
        audit(XML)
    except (AssertionError, ET.ParseError) as exc:
        print(f"FAIL {exc}")
        return 1
    print("PASS native corroborating RTL9210B support-netlist assertions")
    if args.negative_control:
        text = XML.read_text(errors="replace")
        bad = re.sub(r"(<value>)RTL9210B-CG(</value>)", r"\1REMOVED\2", text, count=1)
        if bad == text:
            print("FAIL negative control could not mutate component value")
            return 1
        with tempfile.NamedTemporaryFile("w", suffix=".xml") as fh:
            fh.write(bad)
            fh.flush()
            try:
                audit(Path(fh.name))
            except AssertionError:
                print("PASS negative control: mutated RTL9210B component identity fails")
            else:
                print("FAIL negative control did not fail")
                return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
