#!/usr/bin/env python3
"""Test V121 geometry with normal trace width and footprint-local pad clearance."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_STORAGE_MKEY_USB3_SERIALIZED_V121_20260912.kicad_pcb"
OUT = ROOT / "PHASE24_STORAGE_MKEY_USB3_V121_LOCAL_PAD_RULE_20260912.kicad_pcb"
NETS = {"CM5_USB3_RX_N", "CM5_USB3_RX_P", "CM5_USB3_TX_N", "CM5_USB3_TX_P"}

board = pcbnew.LoadBoard(str(BASE))
if board is None: raise SystemExit("cannot load base")
for item in board.GetTracks():
    if item.GetNetname() in NETS and not isinstance(item, pcbnew.PCB_VIA):
        item.SetWidth(pcbnew.FromMM(0.20))
u12 = board.FindFootprintByReference("U12")
if u12 is None: raise SystemExit("missing U12")
for pad in u12.Pads():
    pad.SetLocalClearance(pcbnew.FromMM(0.15))
board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
