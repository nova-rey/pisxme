#!/usr/bin/env python3
"""Disposable channel-planned TX pair fanout for the frozen U12 baseline."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_STORAGE_MKEY_USB3_U12_LEFT_R80_MOVE_20260912.kicad_pcb"
OUT = ROOT / "PHASE24_STORAGE_MKEY_USB3_U12_LEFT_TX_CHANNEL_20260912.kicad_pcb"
TX = ("CM5_USB3_TX_N", "CM5_USB3_TX_P")

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))

def add(board, name, pts):
    net = board.FindNet(name)
    for a, z in zip(pts, pts[1:]):
        t = pcbnew.PCB_TRACK(board)
        t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.F_Cu)
        t.SetWidth(pcbnew.FromMM(.13208)); t.SetNet(net); t.SetNetCode(net.GetNetCode())
        board.Add(t)

board = pcbnew.LoadBoard(str(BASE))
if board is None: raise SystemExit("cannot load base")
# Remove only the old U12-side TX fanout, retaining the accepted source escape.
for item in list(board.GetTracks()):
    if isinstance(item, pcbnew.PCB_VIA) or item.GetNetname() not in TX:
        continue
    a, z = item.GetStart(), item.GetEnd()
    ax, ay, zx, zy = map(pcbnew.ToMM, (a.x, a.y, z.x, z.y))
    if max(ay, zy) > 120.0 and min(ax, zx) > 140.0:
        board.RemoveNative(item)

# Source-side lanes turn at different y values, then remain parallel on the
# left side of U12's exposed pad and power pad.  The last segments terminate
# on the actual U12 TX pads after the local 0.15 mm pad-field override.
add(board, "CM5_USB3_TX_N", [(149.0,108.0),(149.0,124.0),(147.2,124.0),
                             (147.2,136.2),(148.7,136.2)])
add(board, "CM5_USB3_TX_P", [(151.0,112.0),(151.0,126.0),(147.8,126.0),
                             (147.8,135.8),(148.3,135.8)])
board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
