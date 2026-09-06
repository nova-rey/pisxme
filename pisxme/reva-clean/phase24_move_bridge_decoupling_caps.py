#!/usr/bin/env python3
"""Disposable Phase 24 experiment: move only U7 bridge decoupling caps.

The coordinated CM5IO-derived USB3/SATA donor route is retained verbatim;
this script changes footprint placement only, so native DRC can discriminate
local power-support collision from route/topology failure.
"""
import os
from pathlib import Path
import pcbnew

BASE = Path(os.environ.get("PISXME_CAP_BASE", "PHASE24_SELECTED_MACRO_STORAGE_PROVEN_USB3_SATA_RXN_STITCH.kicad_pcb"))
OUT = Path(os.environ.get("PISXME_CAP_OUT", "PHASE24_STORAGE_CAP_MOVE.kicad_pcb"))
POS = os.environ.get("PISXME_CAP_POS", "95,118;101,118;107,118")
BOTTOM = os.environ.get("PISXME_CAP_BOTTOM", "0") == "1"

board = pcbnew.LoadBoard(str(BASE))
positions = [tuple(map(float, item.split(","))) for item in POS.split(";")]
if len(positions) != 3:
    raise SystemExit("PISXME_CAP_POS must contain C16, C17, and C19 positions")
for ref, (x, y) in zip(("C16", "C17", "C19"), positions):
    fp = board.FindFootprintByReference(ref)
    if fp is None:
        raise SystemExit(f"missing {ref}")
    fp.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(x), pcbnew.FromMM(y)))
    if BOTTOM:
        fp.Flip(pcbnew.VECTOR2I(pcbnew.FromMM(x), pcbnew.FromMM(y)), True)
board.Save(str(OUT))
print(OUT)
