"""Disposable JMS_VCCO via translation for the integrated storage workbench."""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
base = R / os.environ.get("P24_VCCO_BASE", "PHASE24_STORAGE_SELECTOR_SATA_ESCAPE_V4_MODE.kicad_pcb")
out = R / os.environ.get("P24_VCCO_OUT", "PHASE24_STORAGE_VCCO_VIA_V6.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def add_track(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board); t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(net)
    t.SetNetCode(net.GetNetCode()); board.Add(t)
def add_via(board, net, xy):
    v = pcbnew.PCB_VIA(board); v.SetPosition(P(*xy)); v.SetWidth(pcbnew.FromMM(.50))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F, B); v.SetNet(net)
    v.SetNetCode(net.GetNetCode()); board.Add(v)

b = pcbnew.LoadBoard(str(base))
if b is None: raise SystemExit(f"cannot load {base}")
n = b.FindNet("JMS_VCCO")
if n is None: raise SystemExit("missing JMS_VCCO")
for item in list(b.GetTracks()):
    if item.GetNetCode() == n.GetNetCode(): b.RemoveNative(item)
# Preserve the existing coherent source/destination corridor, moving only
# the destination transition away from C86.1 and its USB_TXP1 launch.
add_track(b, n, F, (136.35, 134.0), (132.0, 136.0))
add_via(b, n, (132.0, 136.0))
add_track(b, n, B, (132.0, 136.0), (132.0, 145.0))
add_track(b, n, B, (132.0, 145.0), (147.0, 147.0))
add_via(b, n, (147.0, 147.0))
add_track(b, n, F, (147.0, 147.0), (147.5, 147.0))
b.BuildListOfNets(); b.Save(str(out)); print(out)
