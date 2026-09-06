"""Disposable native USB3 pair-corridor trial on the selected macro basis.

This is intentionally not a general maze router. Each differential pair is
kept together, assigned a permitted signal layer, and emitted as a monotonic
source-to-U7 corridor using native pad coordinates. TX uses B.Cu and ordinary
through-vias outside the TI pad field; RX uses F.Cu. No expected graph edges
are created.
"""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / os.environ.get("PISXME_USB3_PAIR_BASE", "PHASE24_SELECTED_MACRO_SWAP_STORAGE_ISOLATED.kicad_pcb")
OUT = ROOT / os.environ.get("PISXME_USB3_PAIR_OUT", "PHASE24_SELECTED_MACRO_SWAP_STORAGE_USB3_PAIR_CORRIDOR.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu
WIDTH = pcbnew.FromMM(0.1321)

def V(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def find_net(board, name):
    for candidate in (name, "/CORE_CM5/" + name, "/STORAGE/" + name):
        n = board.FindNet(candidate)
        if n is not None:
            return n
    raise RuntimeError(f"missing native net {name}")

def pad(board, ref, number):
    p = board.FindFootprintByReference(ref).FindPadByNumber(str(number))
    if p is None:
        raise RuntimeError(f"missing {ref}.{number}")
    return p

def xy(item):
    p = item.GetPosition()
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)

def track(board, net, a, z, layer):
    if a == z:
        return
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(WIDTH); t.SetNet(net); board.Add(t)

def via(board, net, p):
    v = pcbnew.PCB_VIA(board)
    v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(0.45))
    v.SetDrill(pcbnew.FromMM(0.25)); v.SetLayerPair(F, B); v.SetNet(net)
    board.Add(v)

def path(board, net, points, layer):
    for a, z in zip(points, points[1:]):
        track(board, net, a, z, layer)

board = pcbnew.LoadBoard(str(BASE))
jobs = [
    # Pair order is preserved at J7 and the corrected TI U7 field.
    # All four corridors remain on F.Cu in this no-transition control. The
    # vertical escape columns descend with source-pair order, so each upper
    # source track terminates before the lower route's vertical turn; this is
    # the monotonic non-crossing construction for the native pad ordering.
    ("RX_N", "128", "42", F, 90.0, 0.0),
    ("RX_P", "130", "43", F, 88.0, 0.0),
    ("TX_N", "140", "45", F, 86.0, 0.0),
    ("TX_P", "142", "46", F, 84.0, 0.0),
]

# Remove only existing USB3 copper from this disposable basis. The isolated
# input normally contains none; this also makes reruns deterministic.
for item in list(board.GetTracks()):
    if "CM5_USB3_" in item.GetNetname():
        board.RemoveNative(item)

for suffix, source_number, target_number, layer, column, target_column in jobs:
    name = "CM5_USB3_" + suffix
    net = find_net(board, name)
    source = xy(pad(board, "J7", source_number))
    target = xy(pad(board, "U7", target_number))
    # The two channels of each pair use adjacent, ordered columns. This keeps
    # the pair monotonic and avoids any same-layer pair crossing. The B.Cu TX
    # pair returns to F.Cu through ordinary vias before the SMD lands.
    if layer == F:
        path(board, net, [source, (column, source[1]), (column, target[1]), target], F)
    else:
        # J7's native pads are F.Cu-only SMD lands. Fan out on F.Cu first,
        # then transition to the ordered B.Cu pair corridor.
        source_via = (column, source[1])
        path(board, net, [source, source_via], F)
        via(board, net, source_via)
        target_via = (target_column, target[1])
        path(board, net, [source_via, (column, target[1]), target_via], B)
        via(board, net, target_via)
        path(board, net, [target_via, target], F)

board.BuildListOfNets()
board.Save(str(OUT))
print(OUT)
