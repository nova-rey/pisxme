#!/usr/bin/env python3
"""Disposable test: move only the CM5_PERST vertical handoff to B.Cu."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_STORAGE_MKEY_USB3_V121_LOCAL_PAD_RULE_20260912.kicad_pcb"
OUT = ROOT / "PHASE24_STORAGE_MKEY_USB3_V121_PERST_BCU_20260912.kicad_pcb"
board = pcbnew.LoadBoard(str(BASE))
if board is None: raise SystemExit("cannot load base")
net = board.FindNet("CM5_PERST")
if net is None: raise SystemExit("missing CM5_PERST")
victims = []
for item in board.GetTracks():
    if item.GetNetCode() != net.GetNetCode() or isinstance(item, pcbnew.PCB_VIA): continue
    a, z = item.GetStart(), item.GetEnd()
    ax, ay = pcbnew.ToMM(a.x), pcbnew.ToMM(a.y)
    zx, zy = pcbnew.ToMM(z.x), pcbnew.ToMM(z.y)
    if abs(ax-zx) < 0.01 and abs(ay-zy) > 20 and 150 < ax < 155:
        victims.append(item)
if len(victims) != 1: raise SystemExit(f"expected one vertical PERST segment, got {len(victims)}")
old = victims[0]; start, end = old.GetStart(), old.GetEnd()
board.RemoveNative(old)
for point in (start, end):
    v = pcbnew.PCB_VIA(board); v.SetPosition(point); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)
item = pcbnew.PCB_TRACK(board); item.SetStart(start); item.SetEnd(end); item.SetLayer(pcbnew.B_Cu); item.SetWidth(pcbnew.FromMM(.20)); item.SetNet(net); item.SetNetCode(net.GetNetCode()); board.Add(item)
board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
