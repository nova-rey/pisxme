#!/usr/bin/env python3
"""Detect the known lane-role conflict in the retained WIP root receipt.

This is a negative-evidence audit.  A PASS means the WIP source still exposes
the conflict and therefore must not be used as the Path-B wiring oracle.
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "authority-inventory" / "rtl9210b"
WIP = ROOT / "RTL9210B_ROOT.xml"
M2 = ROOT / "M.2_0.xml"


def net_nodes(root, name):
    for net in root.findall(".//nets/net"):
        if net.get("name") == name:
            return {(n.get("ref"), n.get("pin")) for n in net.findall("node")}
    raise AssertionError(f"missing net {name}")


def audit(wip_path: Path, m2_path: Path):
    wip = ET.parse(wip_path).getroot()
    m2 = ET.parse(m2_path).getroot()
    # Physical platform-side authority: TX on 49/47, RX on 43/41.
    m2_by_name = {n.get("name") or "": n for n in m2.findall(".//nets/net")}
    for net_name, pin, function in (
        ("Net-(CN6-PETp0/SATA-A+)", "49", "PETp0/SATA-A+"),
        ("Net-(CN6-PETn0/SATA-A-)", "47", "PETn0/SATA-A-"),
    ):
        net = m2_by_name.get(net_name)
        if net is None or not any(
            n.get("ref") == "CN6" and n.get("pin") == pin
            and function in (n.get("pinfunction") or "")
            for n in net.findall("node")
        ):
            raise AssertionError(f"missing platform TX contact {net_name} CN6.{pin}")

    # The WIP root instead attaches controller TX to platform RX contacts and
    # controller RX to the TX-side coupling-capacitor nets.
    require_tx = {("CN6", "43"), ("U2", "68")}
    require_rx = {("CN6", "41"), ("U2", "67")}
    if net_nodes(wip, "/M.2_0/PCIE_RXI0+") != require_tx:
        raise AssertionError("WIP TX mismatch no longer matches retained receipt")
    if net_nodes(wip, "/M.2_0/PCIE_RXI0-") != require_rx:
        raise AssertionError("WIP TX- mismatch no longer matches retained receipt")
    if net_nodes(wip, "/M.2_0/PCIE_TXO_0+") != {("C89", "1"), ("U2", "64")}:
        raise AssertionError("WIP RX+ mismatch no longer matches retained receipt")
    if net_nodes(wip, "/M.2_0/PCIE_TXO_0-") != {("C90", "1"), ("U2", "65")}:
        raise AssertionError("WIP RX- mismatch no longer matches retained receipt")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--negative-control", action="store_true")
    args = ap.parse_args()
    if not WIP.exists() or not M2.exists():
        print("FAIL missing retained WIP/root or M.2 XML")
        return 1
    try:
        audit(WIP, M2)
    except (AssertionError, ET.ParseError) as exc:
        print(f"FAIL {exc}")
        return 1
    print("PASS retained WIP hierarchy conflict is detected and quarantined")
    if args.negative_control:
        text = WIP.read_text(errors="replace")
        bad = re.sub(r'pin="43"', 'pin="49"', text, count=1)
        if bad == text:
            print("FAIL negative control could not mutate WIP receipt")
            return 1
        with tempfile.NamedTemporaryFile("w", suffix=".xml") as fh:
            fh.write(bad)
            fh.flush()
            try:
                audit(Path(fh.name), M2)
            except AssertionError:
                print("PASS negative control: WIP conflict mutation is detected")
            else:
                print("FAIL negative control did not fail")
                return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
