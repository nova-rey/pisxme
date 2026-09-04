"""Regression for the native regulator child-to-root power association."""

import subprocess
import tempfile
import xml.etree.ElementTree as ET
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    child = (ROOT / "REGULATORS.kicad_sch").read_text()
    assert child.count('(global_label "12V_PROTECTED"') == 1
    assert child.count('(global_label "POWER_GND"') == 1
    for name in ("VCC_U3_INTERNAL", "VCC_U4_INTERNAL", "VCC_U5_INTERNAL"):
        assert f'(label "{name}"' in child
    out = ROOT / f".phase15-net-authority-{os.getpid()}.xml"
    try:
        result = subprocess.run(
            ["xvfb-run", "-a", "kicad-cli", "sch", "export", "netlist",
             "--format", "kicadxml", "--output", out.name,
             "PiSXMe_RevA_Clean.kicad_sch"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
        assert not result.stderr.strip(), result.stderr
        nets = ET.parse(out).getroot().find("nets")
        named = {net.attrib["name"]: net for net in nets}
        assert "/REGULATORS/12V_PROTECTED" not in named
        assert "/REGULATORS/POWER_GND" not in named
        assert {"12V_PROTECTED", "POWER_GND"} <= named.keys()
        for ref in ("U3", "U4", "U5"):
            assert any(node.attrib.get("ref") == ref and node.attrib.get("pin") == "1"
                       for node in named["12V_PROTECTED"].findall("node"))
            assert any(node.attrib.get("ref") == ref and node.attrib.get("pin") == "17"
                       for node in named["POWER_GND"].findall("node"))
        for ref, net_name in (("U3", "/REGULATORS/CM5_5V"),
                              ("U4", "/REGULATORS/BRIDGE_3V3"),
                              ("U5", "/REGULATORS/BRIDGE_1V1")):
            assert any(node.attrib.get("ref") == ref and node.attrib.get("pin") == "5"
                       for node in named[net_name].findall("node"))
        for ref, net_name in (("U3", "/REGULATORS/VCC_U3_INTERNAL"),
                              ("U4", "/REGULATORS/VCC_U4_INTERNAL"),
                              ("U5", "/REGULATORS/VCC_U5_INTERNAL")):
            assert net_name in named
            nodes = named[net_name].findall("node")
            assert [(n.attrib.get("ref"), n.attrib.get("pin")) for n in nodes] == [(ref, "7")]
    finally:
        out.unlink(missing_ok=True)
    print("Phase 15 regulator net authority: PASS; root power continuity and isolated VCC")


if __name__ == "__main__":
    main()
