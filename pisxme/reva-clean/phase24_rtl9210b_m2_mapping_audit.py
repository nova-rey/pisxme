#!/usr/bin/env python3
"""Assert the socket-side M-key contact mapping used by Path B.

This audit checks native KiCad XML labels and contact pin identities. It does
not add controller-to-socket edges; that physical connection remains a future
fixture/production-netlist gate.
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

XML = Path(__file__).resolve().parent / "authority-inventory" / "rtl9210b" / "M.2_0.xml"


def audit(path: Path):
    root = ET.parse(path).getroot()
    nets = {n.get("name") or "": n for n in root.findall(".//nets/net")}

    expected = {
        "/PCIE_TXO_0+": ("C89", "1", "1_1"),
        "/PCIE_TXO_0-": ("C90", "1", "1_1"),
        "Net-(CN6-PETp0/SATA-A+)": ("CN6", "49", "PETp0/SATA-A+"),
        "Net-(CN6-PETn0/SATA-A-)": ("CN6", "47", "PETn0/SATA-A-"),
        "/PCIE_RXI0+": ("CN6", "43", "PERp0/SATA-B-"),
        "/PCIE_RXI0-": ("CN6", "41", "PERn0/SATA-B+"),
        "/PCIE_REFCLK+": ("CN6", "55", "REFCLKp"),
        "/PCIE_REFCLK-": ("CN6", "53", "REFCLKn"),
        "/PERST#": ("CN6", "50", "~{PERST}"),
        "/CLKREQ#": ("CN6", "52", "~{CLKREQ}"),
        "/PDET": ("CN6", "69", "PEDET"),
    }
    for net_name, (ref, pin, function) in expected.items():
        if net_name not in nets:
            raise AssertionError(f"missing native M.2 net {net_name}")
        found = any(
            node.get("ref") == ref
            and node.get("pin") == pin
            and function in (node.get("pinfunction") or "")
            for node in nets[net_name].findall("node")
        )
        if not found:
            raise AssertionError(f"{net_name} is not {ref}.{pin} {function}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--negative-control", action="store_true")
    args = ap.parse_args()
    if not XML.exists():
        print(f"FAIL missing {XML}")
        return 1
    try:
        audit(XML)
    except (AssertionError, ET.ParseError) as exc:
        print(f"FAIL {exc}")
        return 1
    print("PASS native M-key contact mapping assertions")
    if args.negative_control:
        text = XML.read_text(errors="replace")
        bad = re.sub(r'pin="49"', 'pin="43"', text, count=1)
        if bad == text:
            print("FAIL negative control could not mutate contact mapping")
            return 1
        with tempfile.NamedTemporaryFile("w", suffix=".xml") as fh:
            fh.write(bad)
            fh.flush()
            try:
                audit(Path(fh.name))
            except AssertionError:
                print("PASS negative control: TX contact permutation fails")
            else:
                print("FAIL negative control did not fail")
                return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
