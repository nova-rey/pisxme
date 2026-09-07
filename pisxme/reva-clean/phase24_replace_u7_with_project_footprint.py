#!/usr/bin/env python3
"""Replace embedded U7 in a disposable board with project-local footprint authority.

This is an evidence fixture only. It preserves the board's native pad nets and
placement while testing whether the project-local TUSB9261 land pattern removes
legacy embedded-footprint geometry debt.
"""
import argparse
from pathlib import Path
import pcbnew

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    a = ap.parse_args()
    board = pcbnew.LoadBoard(a.input)
    if board is None:
        raise SystemExit("native board load failed")
    old = board.FindFootprintByReference("U7")
    if old is None:
        raise SystemExit("missing U7")
    libdir = str(Path(__file__).resolve().parent / "PiSXMe_RevA_Clean.pretty")
    fresh = pcbnew.FootprintLoad(libdir, "TUSB9261IPVP_PVP0064A")
    if fresh is None:
        raise SystemExit("project-local TUSB9261 footprint load failed")
    fresh.SetReference("U7")
    fresh.SetValue(old.GetValue())
    fresh.SetPosition(old.GetPosition())
    fresh.SetOrientation(old.GetOrientation())
    fresh.SetLayer(old.GetLayer())
    pad_nets = {}
    for number in range(1, 66):
        src = old.FindPadByNumber(str(number))
        dst = fresh.FindPadByNumber(str(number))
        if src is None or dst is None:
            raise SystemExit(f"pad mismatch at U7.{number}")
        pad_nets[number] = src.GetNetname()
    board.Remove(old)
    board.Add(fresh)
    board.BuildListOfNets()
    for number, netname in pad_nets.items():
        if not netname:
            continue
        dst = fresh.FindPadByNumber(str(number))
        net = board.FindNet(netname)
        if net is None:
            raise SystemExit(f"missing board net after replacement: {netname}")
        dst.SetNet(net)
        dst.SetNetCode(net.GetNetCode())
    board.Save(a.output)
    print(a.output)

if __name__ == "__main__":
    main()
