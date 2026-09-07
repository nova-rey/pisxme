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
SCRUBBED = HERE / ".phase24_support_branch_scrubbed.kicad_pcb"
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

def scrub_affected_copper(src):
    """Remove serialized segment/via blocks without SWIG collection mutation."""
    text = src.read_text()
    starts = []
    i = 0
    while i < len(text):
        if text.startswith("\t(segment", i) or text.startswith("\t(via", i):
            depth = 0; j = i
            while j < len(text):
                if text[j] == "(": depth += 1
                elif text[j] == ")":
                    depth -= 1
                    if depth == 0:
                        block = text[i:j + 1]
                        if any(f'(net "{name}")' in block for name in NETS):
                            starts.append((i, j + 1))
                        i = j
                        break
                j += 1
        i += 1
    for a, z in reversed(starts):
        text = text[:a] + text[z:]
    SCRUBBED.write_text(text)

def main():
    scrub_affected_copper(BASE)
    board = pcbnew.LoadBoard(str(SCRUBBED))
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

    # Do not synthesize support joins in this placement-only candidate.  The
    # next route writer must derive each net's legal escape from these moved
    # pads; a sorted XY chain would be synthetic connectivity and could hide
    # the actual local routing problem.

    board.BuildListOfNets()
    board.Save(str(OUT))
    print(OUT)

if __name__ == "__main__":
    main()
