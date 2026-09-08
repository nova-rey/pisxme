#!/usr/bin/env python3
"""Audit the native root USB3 authority against a saved PCB candidate.

The XML assertions describe the schematic's resolved ownership; connectivity
is checked from KiCad's loaded pads/tracks/vias only.  No graph edges are
invented by this audit.
"""
from pathlib import Path
import argparse
import xml.etree.ElementTree as ET
import pcbnew

ROOT = Path(__file__).resolve().parent
NETS = {
    "CM5_USB3_RX_N": (("J7", "128"), ("U12", "16"), ("U7", "42")),
    "CM5_USB3_RX_P": (("J7", "130"), ("U12", "15"), ("U7", "43")),
    "CM5_USB3_TX_N": (("J7", "140"), ("U12", "12"), ("U7", "45")),
    "CM5_USB3_TX_P": (("J7", "142"), ("U12", "11"), ("U7", "46")),
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pcb", type=Path)
    ap.add_argument("xml", type=Path)
    args = ap.parse_args()
    root = ET.parse(args.xml).getroot()
    resolved = {}
    for net in root.findall(".//nets/net"):
        name = net.get("name", "").rsplit("/", 1)[-1]
        if name in NETS:
            resolved[name] = {(n.get("ref"), n.get("pin")) for n in net.findall("node")}
    failures = []
    for name, endpoints in NETS.items():
        expected = set(endpoints)
        if resolved.get(name) is None or not expected.issubset(resolved[name]):
            failures.append(f"{name}: root XML does not resolve {sorted(expected)}")
    board = pcbnew.LoadBoard(str(args.pcb))
    board.BuildConnectivity()
    pads = {(f.GetReference(), str(p.GetNumber())): p
            for f in board.GetFootprints() for p in f.Pads()}
    conn = board.GetConnectivity()
    for name, endpoints in NETS.items():
        missing = [e for e in endpoints if e not in pads]
        wrong = [f"{e[0]}.{e[1]}={pads[e].GetNetname()}" for e in endpoints
                 if e in pads and pads[e].GetNetname().rsplit("/", 1)[-1] != name]
        if missing or wrong:
            failures.append(f"{name}: PCB ownership missing={missing} wrong={wrong}")
            continue
        reached = {(p.GetParentFootprint().GetReference(), str(p.GetNumber()))
                   for p in conn.GetConnectedItems(pads[endpoints[0]])
                   if type(p).__name__ == "PAD"}
        if not set(endpoints).issubset(reached):
            failures.append(f"{name}: native PCB connectivity reaches {sorted(reached)}")
        else:
            print(f"{name}: root authority and native PCB connectivity PASS")
    if failures:
        for failure in failures:
            print(failure)
        raise SystemExit(1)
    print("phase24 root USB3 authority: PASS")

if __name__ == "__main__":
    main()
