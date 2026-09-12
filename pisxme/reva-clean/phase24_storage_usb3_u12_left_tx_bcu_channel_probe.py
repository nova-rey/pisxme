#!/usr/bin/env python3
"""Disposable second TX strategy: B.Cu channel around the RX trunk."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_STORAGE_MKEY_USB3_U12_LEFT_R80_MOVE_20260912.kicad_pcb"
OUT = ROOT / "PHASE24_STORAGE_MKEY_USB3_U12_LEFT_TX_BCU_CHANNEL_20260912.kicad_pcb"
TX = ("CM5_USB3_TX_N", "CM5_USB3_TX_P")

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def track(board, name, a, z, layer=pcbnew.F_Cu):
    net = board.FindNet(name); t = pcbnew.PCB_TRACK(board)
    t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(.13208)); t.SetNet(net); t.SetNetCode(net.GetNetCode()); board.Add(t)
def via(board, name, p):
    net = board.FindNet(name); v = pcbnew.PCB_VIA(board)
    v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30))
    v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)

board = pcbnew.LoadBoard(str(BASE))
if board is None: raise SystemExit("cannot load base")
# Remove the old U12-side TX fanout and its source-side F.Cu tail.
for item in list(board.GetTracks()):
    if isinstance(item, pcbnew.PCB_VIA) or item.GetNetname() not in TX:
        continue
    a, z = item.GetStart(), item.GetEnd()
    ax, ay, zx, zy = map(pcbnew.ToMM, (a.x, a.y, z.x, z.y))
    if max(ay, zy) > 120.0 and min(ax, zx) > 140.0:
        board.RemoveNative(item)

# TX_N: F.Cu source escape -> via -> parallel B.Cu channel -> via -> pad.
track(board, "CM5_USB3_TX_N", (149.0,108.0), (149.0,124.0))
via(board, "CM5_USB3_TX_N", (149.0,124.0))
track(board, "CM5_USB3_TX_N", (149.0,124.0), (147.2,124.0), pcbnew.B_Cu)
track(board, "CM5_USB3_TX_N", (147.2,124.0), (147.2,134.5), pcbnew.B_Cu)
via(board, "CM5_USB3_TX_N", (147.2,134.5))
track(board, "CM5_USB3_TX_N", (147.2,134.5), (148.7,136.2))

# TX_P: staggered source turn, then a parallel B.Cu channel 0.6 mm away.
track(board, "CM5_USB3_TX_P", (151.0,112.0), (151.0,126.0))
via(board, "CM5_USB3_TX_P", (151.0,126.0))
track(board, "CM5_USB3_TX_P", (151.0,126.0), (147.8,126.0), pcbnew.B_Cu)
track(board, "CM5_USB3_TX_P", (147.8,126.0), (147.8,133.8), pcbnew.B_Cu)
via(board, "CM5_USB3_TX_P", (147.8,133.8))
track(board, "CM5_USB3_TX_P", (147.8,133.8), (148.3,135.8))
board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
