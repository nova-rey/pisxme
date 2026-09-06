"""Audit dual-mode storage USB3 connectivity from saved native PCB objects.

Expected endpoint pairs are assertions only.  Connectivity comes exclusively
from KiCad's saved pads, tracks, and vias after native connectivity rebuild.
"""
from pathlib import Path
import argparse
import pcbnew

ROOT = Path(__file__).resolve().parent
CHECKS = (
    ("CM5_USB3_RX_N", "J7.128", "U12.16"),
    ("CM5_USB3_RX_P", "J7.130", "U12.15"),
    ("CM5_USB3_TX_N", "J7.140", "U12.12"),
    ("CM5_USB3_TX_P", "J7.142", "U12.11"),
    ("USB_TXP1", "U11.21", "C86.1"),
    ("USB_TXN1", "U11.22", "C87.1"),
    ("JMS_USB3_TXP", "C86.2", "U12.25"),
    ("JMS_USB3_TXN", "C87.2", "U12.24"),
    ("USB_RXP1", "U11.26", "U12.23"),
    ("USB_RXN1", "U11.27", "U12.22"),
)


def token(pad):
    return f"{pad.GetParentFootprint().GetReference()}.{pad.GetNumber()}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pcb", nargs="?", type=Path,
                    default=ROOT / "PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED.kicad_pcb")
    board = pcbnew.LoadBoard(str(ap.parse_args().pcb))
    if board is None:
        raise SystemExit("cannot load PCB")
    board.BuildConnectivity()
    conn = board.GetConnectivity()
    pads = {token(p): p for f in board.GetFootprints() for p in f.Pads()}
    failures = []
    for net, left, right in CHECKS:
        if left not in pads or right not in pads:
            failures.append(f"{net}: missing endpoint {left} or {right}")
            continue
        if not pads[left].GetNetname().endswith("/" + net) and pads[left].GetNetname() != net:
            failures.append(f"{net}: wrong net on {left}: {pads[left].GetNetname()}")
            continue
        reached = {token(p) for p in conn.GetConnectedItems(pads[left])
                   if type(p).__name__ == "PAD"}
        if right not in reached:
            failures.append(f"{net}: disconnected {left} -> {right}")
        else:
            print(f"{net}: PASS ({left} <-> {right})")
    if failures:
        for failure in failures:
            print(failure)
        raise SystemExit(1)
    print("dual-mode storage USB3 native connectivity: PASS")


if __name__ == "__main__":
    main()
