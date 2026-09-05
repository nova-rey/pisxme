#!/usr/bin/env python3
"""Regression for native CM5-to-SERVICE hierarchy association."""
from pathlib import Path
import subprocess, tempfile, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]

def main():
    out = ROOT / ".phase20-service-netlist.xml"
    try:
        subprocess.run([
            "xvfb-run", "-a", "kicad-cli", "sch", "export", "netlist",
            "--format", "kicadxml", "--output", str(out),
            "PiSXMe_RevA_Clean.kicad_sch",
        ], cwd=ROOT, check=True)
        root = ET.parse(out).getroot()
    finally:
        out.unlink(missing_ok=True)
    nets = {
        n.attrib["name"]: {(x.attrib["ref"], x.attrib["pin"])
                            for x in n.findall("node")}
        for n in root.findall(".//nets/net")
    }
    assert nets["/CORE_CM5/SERVICE_USB2_DP"] >= {
        ("J4", "1"), ("J7", "105"), ("U8", "1")
    }
    assert nets["/CORE_CM5/SERVICE_USB2_DM"] >= {
        ("J4", "2"), ("J7", "103"), ("U8", "2")
    }
    print("Phase 20 SERVICE native hierarchy: PASS; J7.103=DM, J7.105=DP")

if __name__ == "__main__":
    main()
