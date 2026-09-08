#!/usr/bin/env python3
"""Prove the USB3 audit is sensitive to removal of necessary copper."""
from pathlib import Path
import argparse
import pcbnew

CHECKS = (("CM5_USB3_RX_N", "J7", "128", "U12", "16"),
          ("CM5_USB3_RX_P", "J7", "130", "U12", "15"),
          ("CM5_USB3_TX_N", "J7", "140", "U12", "12"),
          ("CM5_USB3_TX_P", "J7", "142", "U12", "11"))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("pcb", type=Path)
    b = pcbnew.LoadBoard(str(ap.parse_args().pcb)); b.BuildConnectivity()
    pads = {(f.GetReference(), str(p.GetNumber())): p
            for f in b.GetFootprints() for p in f.Pads()}
    conn = b.GetConnectivity()
    for name, ar, an, br, bn in CHECKS:
        left, right = pads[(ar, an)], pads[(br, bn)]
        if not any(type(x).__name__ == "PAD" and
                   x.GetParentFootprint().GetReference() == br and
                   str(x.GetNumber()) == bn for x in conn.GetConnectedItems(left)):
            raise SystemExit(f"baseline unexpectedly disconnected: {name}")
    removed = None
    for item in list(b.GetTracks()):
        if item.GetNetname() == "CM5_USB3_RX_N" and type(item).__name__ == "PCB_TRACK":
            removed = item; b.RemoveNative(item); break
    if removed is None:
        raise SystemExit("no necessary RX_N track found to remove")
    b.BuildConnectivity(); left, right = pads[("J7", "128")], pads[("U12", "16")]
    if any(type(x).__name__ == "PAD" and
           x.GetParentFootprint().GetReference() == "U12" and
           str(x.GetNumber()) == "16" for x in b.GetConnectivity().GetConnectedItems(left)):
        raise SystemExit("negative control failed: removed track did not break RX_N")
    print("USB3 baseline native connectivity: PASS")
    print("USB3 removed-trace negative control: PASS (audit fails as required)")

if __name__ == "__main__": main()
