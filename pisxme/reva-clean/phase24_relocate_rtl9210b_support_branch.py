#!/usr/bin/env python3
"""Disposable Path-B experiment: move the complete local support branch.

This intentionally starts from the native V11 saved board, removes only the
affected support/control copper, translates the coherent support footprints,
and writes a candidate for native DRC.  It never modifies production CAD.
"""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_CRYSTAL_V11.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_BRANCH_RELOCATED_V1.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)
DX, DY = 0.0, 22.0
MOVED = {"U2", "C3", "C4", "C5", "R2", "R3"}
NETS = {"RTL_3V3", "RTL_1V1", "RTL_5V", "SPICS", "SPISO", "SPISI",
        "SPICLK", "SPISO3", "PEDET", "CLKREQ_N"}

def v(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def seg(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(v(*a)); t.SetEnd(v(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    board.Add(t)

def main():
    board = pcbnew.LoadBoard(str(BASE))
    codes = {board.FindNet(name).GetNetCode() for name in NETS
             if board.FindNet(name)}
    # This first candidate deliberately preserves copper.  Removing mixed
    # tracks/vias through the KiCad 10 SWIG wrapper is not stable in this
    # disposable writer; stale-copper DRC is therefore classified as a route
    # implementation failure, not as a placement verdict.
    _ = codes

    for ref in MOVED:
        fp = next((item for item in board.GetFootprints()
                   if item.GetReference() == ref), None)
        if fp is None:
            raise RuntimeError(f"missing footprint {ref}")
        fp.SetPos(fp.GetPosition() + v(DX, DY))

    # Add deliberately simple local support joins at the relocated branch.
    # Long/global fanout remains intentionally open for the next routing pass.
    for name in ("RTL_3V3", "RTL_1V1", "RTL_5V"):
        net = board.FindNet(name)
        pads = []
        for fp in board.GetFootprints():
            for pad in fp.Pads():
                if pad.GetNetCode() == net.GetNetCode():
                    p = pad.GetPosition()
                    pads.append((pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)))
        pads.sort(key=lambda p: (p[1], p[0]))
        for a, z in zip(pads, pads[1:]):
            if abs(a[0] - z[0]) + abs(a[1] - z[1]) < 18:
                seg(board, net, F, a, (z[0], a[1]))
                seg(board, net, F, (z[0], a[1]), z)

    board.BuildListOfNets()
    board.Save(str(OUT))
    print(OUT)

if __name__ == "__main__":
    main()
