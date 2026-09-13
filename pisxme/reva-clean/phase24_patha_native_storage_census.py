#!/usr/bin/env python3
"""Emit a native KiCad connectivity census for the selected Path-A island.

This is an evidence tool only.  It derives connected components from saved
PCB pads/tracks/vias and never adds expected graph edges.  It intentionally
reports open required storage branches so an integrated repair owner can pick
one bounded next action without treating an isolated fixture as closure.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import pcbnew


STORAGE_REFS = ("U7", "U11", "U12", "U13", "U14", "J3")
NETS = (
    "STORAGE_SEL", "USB_OE_N", "AUTO_PEDET", "MODE_IN", "STORAGE_3V3",
    "CM5_STORAGE_USB2_DP", "CM5_STORAGE_USB2_DM", "BRIDGE_USB_DP",
    "BRIDGE_USB_DM", "USB_DP", "USB_DM", "TUSB_SATA_TXP",
    "TUSB_SATA_TXN", "TUSB_SATA_RXP", "TUSB_SATA_RXN",
    "M2_SATA_A_P_PCIE_TXP0", "M2_SATA_A_N_PCIE_TXN0",
    "M2_SATA_B_P_PCIE_RXN0", "M2_SATA_B_N_PCIE_RXP0", "M2_REFCLK_P",
    "M2_REFCLK_N", "M2_PERST_N", "M2_CLKREQ_N", "M2_PEWake_N",
    "JMS_PCIE_TXP0", "JMS_PCIE_TXN0", "JMS_PCIE_RXP0", "JMS_PCIE_RXN0",
    "JMS_USB3_TXP", "JMS_USB3_TXN", "USB_TXP1", "USB_TXN1", "USB_RXP1",
    "USB_RXN1", "JMS_REXT", "JMS_RESET_N", "JMS_AVDD33", "JMS_AVDDL",
    "JMS_VCCO", "JMS_VCCK", "JMS_VDDREG_5V", "XIN", "XOUT", "LXO",
    "POWER_GND",
)


def pad_key(pad):
    return f"{pad.GetParentFootprint().GetReference()}.{pad.GetNumber()}"


def net_name(pad):
    return pad.GetNetname() or "<no-net>"


def connected_pad_keys(connectivity, pad):
    return sorted(
        pad_key(item)
        for item in connectivity.GetConnectedItems(pad)
        if isinstance(item, pcbnew.PAD)
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pcb", type=Path)
    ap.add_argument("output", type=Path)
    args = ap.parse_args()
    board = pcbnew.LoadBoard(str(args.pcb))
    if board is None:
        raise SystemExit(f"cannot load {args.pcb}")
    board.BuildConnectivity()
    connectivity = board.GetConnectivity()
    pads = [pad for fp in board.GetFootprints() for pad in fp.Pads()]
    pads_by_key = {pad_key(pad): pad for pad in pads}
    storage_pads = {
        key: pad for key, pad in pads_by_key.items()
        if key.split(".", 1)[0] in STORAGE_REFS
    }

    by_net = {}
    for key, pad in storage_pads.items():
        by_net.setdefault(net_name(pad), []).append(pad)
    summaries = {}
    for name in sorted(set(NETS) | set(by_net)):
        members = by_net.get(name, [])
        seen = set()
        component_sizes = []
        for pad in members:
            key = pad_key(pad)
            if key in seen:
                continue
            component = set(connected_pad_keys(connectivity, pad))
            component &= set(pad_key(item) for item in members)
            seen |= component
            component_sizes.append(sorted(component))
        tracks = [item for item in board.GetTracks()
                  if item.GetNetname() == name]
        vias = [item for item in tracks if isinstance(item, pcbnew.PCB_VIA)]
        summaries[name] = {
            "storage_pad_count": len(members),
            "storage_component_count": len(component_sizes),
            "storage_component_sizes": sorted(
                (len(component) for component in component_sizes), reverse=True
            ),
            "storage_components": component_sizes,
            "track_count": len(tracks),
            "via_count": len(vias),
            "pad_keys": sorted(pad_key(pad) for pad in members),
        }

    # Explicitly retain the required Path-A physical branches.  These are
    # contract checks, not synthetic connectivity assertions.
    required = [
        ("U7.57", "C30.2", "BRIDGE_SATA_TX_P"),
        ("U7.56", "C31.2", "BRIDGE_SATA_TX_N"),
        ("U7.60", "C32.2", "BRIDGE_SATA_RX_P"),
        ("U7.59", "C33.2", "BRIDGE_SATA_RX_N"),
        ("C30.1", "U13.38", "TUSB_SATA_TXP"),
        ("C31.1", "U13.37", "TUSB_SATA_TXN"),
        ("C32.1", "U13.36", "TUSB_SATA_RXP"),
        ("C33.1", "U13.35", "TUSB_SATA_RXN"),
        ("U13.2", "J3.49", "M2_SATA_A_P_PCIE_TXP0"),
        ("U13.3", "J3.47", "M2_SATA_A_N_PCIE_TXN0"),
        ("U13.6", "J3.41", "M2_SATA_B_P_PCIE_RXN0"),
        ("U13.7", "J3.43", "M2_SATA_B_N_PCIE_RXP0"),
        ("J7.128", "U12.16", "CM5_USB3_RX_N"),
        ("J7.130", "U12.15", "CM5_USB3_RX_P"),
        ("J7.140", "U12.12", "CM5_USB3_TX_N"),
        ("J7.142", "U12.11", "CM5_USB3_TX_P"),
        ("U11.50", "Y10.1", "XIN"),
        ("U11.51", "Y10.2", "XOUT"),
        ("U11.39", "R80.1", "JMS_REXT"),
        ("U11.64", "L10.1", "LXO"),
        ("U11.1", "L10.2", "JMS_VDDREG_5V"),
        ("U11.19", "C80.1", "JMS_AVDD33"),
        ("U11.20", "C83.1", "JMS_AVDDL"),
        ("U14.4", "U12.9", "STORAGE_SEL"),
        ("U14.4", "U13.9", "STORAGE_SEL"),
        # AUTO_PEDET is the J3/J8 strap; U14.2 is MODE_IN (see corrected
        # native netlist/parity audit retained 2026-09-13).
        ("J3.69", "J8.2", "AUTO_PEDET"),
    ]
    endpoint_results = []
    for left, right, name in required:
        lpad, rpad = pads_by_key.get(left), pads_by_key.get(right)
        if lpad is None or rpad is None:
            endpoint_results.append({
                "net": name, "left": left, "right": right,
                "status": "MISSING_SERIALIZED_ENDPOINT",
                "left_net": net_name(lpad) if lpad else None,
                "right_net": net_name(rpad) if rpad else None,
            })
            continue
        reached = set(connected_pad_keys(connectivity, lpad))
        endpoint_results.append({
            "net": name, "left": left, "right": right,
            "status": "PASS" if right in reached else "OPEN",
            "left_net": net_name(lpad), "right_net": net_name(rpad),
            "left_component_size": len(reached),
        })

    result = {
        "schema": "pisxme.phase24.patha.native-storage-census.v1",
        "pcb": str(args.pcb),
        "tool": "KiCad pcbnew native connectivity",
        "storage_refs": list(STORAGE_REFS),
        "storage_pad_total": len(storage_pads),
        "net_summaries": summaries,
        "required_endpoint_results": endpoint_results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "storage_pad_total": len(storage_pads),
        "open_required_endpoints": sum(
            x["status"] != "PASS" for x in endpoint_results
        ),
        "required_endpoint_total": len(endpoint_results),
        "output": str(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
