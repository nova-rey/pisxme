"""Regression for the promoted native Ethernet support hierarchy."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).parents[2] / "pisxme" / "reva-clean"


def _nodes(root, name):
    net = next(n for n in root.findall(".//net") if n.get("name") == name)
    return {(n.get("ref"), n.get("pin")) for n in net.findall("node")}


def test_promoted_ethernet_support_netlist_is_native_and_complete():
    xml = ROOT / "phase24-production.xml"
    erc = ROOT / "PHASE24_PRODUCTION_AFTER_ETHERNET_SUPPORT-erc.rpt"
    root = ET.parse(xml).getroot()
    assert "Errors 0" in erc.read_text()

    assert _nodes(root, "ETH_LEDY") == {("J7", "17"), ("R30", "1")}
    assert _nodes(root, "ETH_LEDG") == {("J7", "15"), ("R31", "1")}
    assert _nodes(root, "/ETHERNET/ETH_CT1") == {("J2", "9"), ("C48", "1")}
    assert _nodes(root, "/ETHERNET/ETH_CT2") == {("J2", "10"), ("C49", "1")}
    assert _nodes(root, "/ETHERNET/ETH_CT3") == {("J2", "11"), ("C50", "1")}
    assert _nodes(root, "/ETHERNET/ETH_CT4") == {("J2", "12"), ("C51", "1")}
    assert _nodes(root, "/ETHERNET/ETH_CT_COMMON") == {
        ("C52", "1"), ("R26", "2"), ("R27", "2"), ("R28", "2"), ("R29", "2")
    }
    assert _nodes(root, "GBE_SHIELD") == {
        ("C52", "2"), ("J2", "17"), ("J2", "18"), ("X6", "3")
    }
    assert not any(n.get("name", "").startswith("unconnected-(J7A-Ethernet_nLED")
                   for n in root.findall(".//net"))
