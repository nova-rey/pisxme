"""Disposable integrated USB3 lane-discipline experiment.

This intentionally does not use a synthetic connectivity graph.  It uses
native J7/U7 pads and net objects, reserves the observed PCIe B.Cu spine as a
hard routing band, and gives each USB3 lane a distinct west-side escape and
monotonic south corridor.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_REVIEW.kicad_pcb"
OUT = R / "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_LANE_ESCAPE.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.15)
LANES = (("CM5_USB3_RX_N", "128", "42"), ("CM5_USB3_RX_P", "130", "43"),
         ("CM5_USB3_TX_N", "140", "45"), ("CM5_USB3_TX_P", "142", "46"))

def V(p): return pcbnew.VECTOR2I_MM(*p)
def xy(p):
    q = p.GetPosition()
    return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)
def add_track(board, n, a, z, layer):
    t = pcbnew.PCB_TRACK(board); t.SetStart(V(a)); t.SetEnd(V(z))
    t.SetLayer(layer); t.SetWidth(W); t.SetNet(n); board.Add(t)
def add_via(board, n, p):
    v = pcbnew.PCB_VIA(board); v.SetPosition(V(p)); v.SetWidth(pcbnew.FromMM(.5))
    v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F, B); v.SetNet(n); board.Add(v)
def path(board, n, points, layer):
    for a, z in zip(points, points[1:]): add_track(board, n, a, z, layer)

board = pcbnew.LoadBoard(str(BASE))
j7, u7 = board.FindFootprintByReference("J7"), board.FindFootprintByReference("U7")
for item in list(board.GetTracks()):
    if any(name in item.GetNetname() for name, _, _ in LANES): board.Remove(item)

# The PCIe PET0 B.Cu spine occupies approximately x=84..190,
# y=99.5..110.5.  All USB3 travel crosses east only below that band.
source_exit_y = (112.0, 113.0, 114.0, 115.0)
target_via_y = (124.6, 125.5, 126.4, 127.3)
for i, (name, jpad, upad) in enumerate(LANES):
    n = board.FindNet(name) or board.FindNet("/CORE_CM5/" + name)
    if n is None: raise RuntimeError(name)
    source = xy(j7.FindPadByNumber(jpad))
    destination = xy(u7.FindPadByNumber(upad))
    ey, ty = source_exit_y[i], target_via_y[i]
    # Exit left from the native B.Cu pad field, drop outside the PCIe band,
    # then use a unique lane below the band.  The x=64 vertical section keeps
    # the four source escapes ordered and off the PCIe via field.
    path(board, n, [source, (64.0, source[1]), (64.0, ey), (88.0, ey), (88.0, ty)], B)
    add_via(board, n, (88.0, ty))
    if i >= 2:
        path(board, n, [(88.0, ty), (91.0, destination[1]), destination], F)
    else:
        path(board, n, [(88.0, ty), destination], F)
board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
