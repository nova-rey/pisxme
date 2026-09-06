#!/usr/bin/env python3
"""Synchronize the PCB bridge rails from the native schematic netlist.

This does not invent connectivity: every pad reassigned below must be present
on the same canonical net in the KiCad-exported schematic netlist.
"""
from pathlib import Path
import argparse
import xml.etree.ElementTree as ET
import pcbnew

ALIASES = {
    "/STORAGE/BRIDGE_3V3": "BRIDGE_3V3",
    "/REGULATORS/BRIDGE_3V3": "BRIDGE_3V3",
    "/STORAGE/BRIDGE_1V1": "BRIDGE_1V1",
    "/REGULATORS/BRIDGE_1V1": "BRIDGE_1V1",
}

def net_members(xml_path):
    root = ET.parse(xml_path).getroot()
    out = {name: set() for name in set(ALIASES.values())}
    for net in root.findall(".//nets/net"):
        name = net.attrib.get("name")
        if name in out:
            for node in net.findall("node"):
                out[name].add((node.attrib["ref"], node.attrib["pin"]))
    if any(not members for members in out.values()):
        raise SystemExit(f"missing authoritative net members: {out}")
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pcb")
    ap.add_argument("xml")
    ap.add_argument("output")
    args = ap.parse_args()
    members = net_members(args.xml)
    board = pcbnew.LoadBoard(args.pcb)
    canonical = {}
    for name in members:
        existing = board.FindNet(name)
        canonical[name] = existing or pcbnew.NETINFO_ITEM(board, name)
        if not existing:
            board.Add(canonical[name])
    changed = 0
    for fp in board.GetFootprints():
        ref = fp.GetReference()
        for pad in fp.Pads():
            old = pad.GetNetname()
            if old not in ALIASES:
                continue
            new = ALIASES[old]
            if (ref, pad.GetNumber()) not in members[new]:
                # The old PCB assigned a net to an unrepresented/unused
                # package pad (U7.3/PWM1 is the known case).  The saved
                # schematic is the authority: clear that stale assignment;
                # do not silently promote it into a supply rail.
                pad.SetNetCode(0)
                changed += 1
                continue
            pad.SetNet(canonical[new])
            changed += 1
    for item in list(board.GetTracks()):
        old = item.GetNetname()
        if old in ALIASES:
            item.SetNetCode(canonical[ALIASES[old]].GetNetCode())
    for zone in board.Zones():
        old = zone.GetNetname()
        if old in ALIASES:
            zone.SetNet(canonical[ALIASES[old]])
    board.SynchronizeNetsAndNetClasses(False)
    board.Save(args.output)
    print(f"reassigned {changed} authoritative bridge-rail pads; saved {args.output}")

if __name__ == "__main__":
    main()
