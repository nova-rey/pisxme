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
    assert text.count("c1000000-0000-0000-0000-000000000") == 5
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
    for j7_pin, j1_pin in (("116", "A2"), ("118", "A3"),
                           ("110", "E7"), ("112", "F7"),
                           ("109", "E18")):
        a, b = containing("J7", j7_pin), containing("J1", j1_pin)
        assert a and b and set(a) & set(b), (j7_pin, j1_pin, a, b)
    # PET0 must not be accidentally shorted across its coupling capacitors.
    assert not any(set(nodes) >= {("J7", "122"), ("C1", "1")}
                   for nodes in nets.values())
    assert not any(set(nodes) >= {("J7", "124"), ("C2", "1")}
                   for nodes in nets.values())
    print("Phase 16 PCIe root net authority: PASS; direct=5; PET0 split=preserved")


if __name__ == "__main__":
    main()
