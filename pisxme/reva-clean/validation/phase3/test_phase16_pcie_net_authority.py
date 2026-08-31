#!/usr/bin/env python3
"""Regression for direct PCIe root connectivity and PET0 split authority."""
from pathlib import Path
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]


def net_nodes(xml_path):
    root = ET.parse(xml_path).getroot()
    return {
        net.attrib["name"]: {(n.attrib["ref"], n.attrib["pin"])
                              for n in net.findall("node")}
        for net in root.findall(".//nets/net")
    }


def main():
    text = (ROOT / "PiSXMe_RevA_Clean.kicad_sch").read_text()
    assert text.count("c1000000-0000-0000-0000-000000000") == 7
    with tempfile.TemporaryDirectory(prefix="pisxme-phase16-net-") as td:
        out = ROOT / ".phase16-netlist-test.xml"
        subprocess.run([
            "xvfb-run", "-a", "kicad-cli", "sch", "export", "netlist",
            "--format", "kicadxml", "--output", str(out),
            "PiSXMe_RevA_Clean.kicad_sch",
        ], cwd=ROOT, check=True)
        nets = net_nodes(out)
        out.unlink()
    def containing(ref, pin):
        return [name for name, nodes in nets.items() if (ref, pin) in nodes]
    direct = {
        "CM5_PER0_P": {("J7", "116"), ("J1", "A2"), ("X1", "1"), ("X2", "1")},
        "CM5_PER0_N": {("J7", "118"), ("J1", "A3"), ("X1", "2"), ("X2", "2")},
        "CM5_REFCLK_P": {("J7", "110"), ("J1", "E7"), ("X1", "5"), ("X2", "5")},
        "CM5_REFCLK_N": {("J7", "112"), ("J1", "F7"), ("X1", "6"), ("X2", "6")},
        "CM5_PERST": {("J7", "109"), ("J1", "E18"), ("X1", "7"), ("X2", "7")},
    }
    for suffix, expected in direct.items():
        matches = [nodes for name, nodes in nets.items() if name.endswith("/" + suffix)]
        assert matches == [expected], (suffix, matches)
    assert {("J7", "122"), ("C1", "1"), ("X1", "3"), ("X2", "3")} in nets.values()
    assert {("J7", "124"), ("C2", "1"), ("X1", "4"), ("X2", "4")} in nets.values()
    # PET0 must not be accidentally shorted across its coupling capacitors.
    assert {("J7", "122"), ("C1", "1"), ("X1", "3"), ("X2", "3")} in nets.values()
    assert {("J7", "124"), ("C2", "1"), ("X1", "4"), ("X2", "4")} in nets.values()
    print("Phase 16 PCIe root net authority: PASS; direct=5; PET0 split=preserved")


if __name__ == "__main__":
    main()
