"""Disposable native SATA pair corridors for the selected storage island.

The capacitor row is deliberately ordered to preserve pair endpoint order at
both the TI bridge and the M.2 socket. RX and TX remain separate permitted
signal layers; every layer transition is an ordinary through-via outside a
component pad. Existing USB3 copper from the validated pair-corridor basis is
retained so coexistence is tested, while old SATA copper is removed.
"""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / os.environ.get("PISXME_SATA_PAIR_BASE", "PHASE24_SELECTED_MACRO_SWAP_STORAGE_USB3_PAIR_CORRIDOR_V3.kicad_pcb")
OUT = ROOT / os.environ.get("PISXME_SATA_PAIR_OUT", "PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_PAIR_CORRIDOR.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu
WIDTH = pcbnew.FromMM(0.1321)

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p):
    q = p.GetPosition()
    return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)
def find_net(board, name):
    for candidate in (name, "/STORAGE/" + name):
        n = board.FindNet(candidate)
        if n is not None: return n
    raise RuntimeError(f"missing native net {name}")
def pad(board, ref, number):
    p = board.FindFootprintByReference(ref).FindPadByNumber(str(number))
    if p is None: raise RuntimeError(f"missing {ref}.{number}")
    return p
def track(board, net, a, z, layer):
    t = pcbnew.PCB_TRACK(board); t.SetStart(V(*a)); t.SetEnd(V(*z))
    t.SetLayer(layer); t.SetWidth(WIDTH); t.SetNet(net); board.Add(t)
def via(board, net, p):
    v = pcbnew.PCB_VIA(board); v.SetPosition(V(*p))
    v.SetWidth(pcbnew.FromMM(0.5)); v.SetDrill(pcbnew.FromMM(0.3))
    v.SetLayerPair(F, B); v.SetNet(net); board.Add(v)
def path(board, net, points, layer):
    for a, z in zip(points, points[1:]): track(board, net, a, z, layer)

board = pcbnew.LoadBoard(str(BASE))

# Native capacitor positions: N is above P at the bridge and socket ends,
# and TX/RX occupy distinct physical corridors. All caps retain their
# manufacturer footprint orientation; pad 2 is bridge-side, pad 1 socket-side.
CAPS = {
    "TX_N": ("C31", (150.5, 130.0)),
    "TX_P": ("C30", (126.5, 130.0)),
    "RX_N": ("C33", (152.5, 125.0)),
    "RX_P": ("C32", (128.5, 125.0)),
}
for ref, (x, y) in CAPS.values():
    f = board.FindFootprintByReference(ref)
    if f is None: raise RuntimeError(f"missing {ref}")
    f.SetPosition(V(x, y)); f.SetOrientationDegrees(180)

# Keep clock, divider, and bridge-rail support as real obstacles but outside
# the high-speed corridor. This is a placement choice for the disposable
# island, not removal or net substitution.
for ref in ("Y1", "R23", "C42", "C43", "C16", "C17", "C19", "R24", "R32", "R33"):
    f = board.FindFootprintByReference(ref)
    if f is not None:
        p = xy(f)
        f.SetPosition(V(p[0] + 90.0, p[1] + 50.0))

# Remove only SATA copper, retaining the already-tested USB3 corridor.
for item in list(board.GetTracks()):
    if "BRIDGE_SATA_" in item.GetNetname() or "SATA_M2_" in item.GetNetname():
        board.RemoveNative(item)

# Bridge-side escapes. TX stays on F.Cu. RX starts on F.Cu at the SMD bridge
# lands, transitions to B.Cu at separated points, then reaches the cap pads.
bridge = {
    "TX_N": ("56", F, [(97.0,119.5),(97.0,105.0),(150.0,105.0),(150.0,130.0)]),
    "TX_P": ("57", F, [(96.5,119.5),(96.5,124.0),(126.0,124.0),(126.0,130.0)]),
    "RX_N": ("59", B, [(95.5,119.5),(95.5,115.0),(152.0,115.0),(152.0,125.0)]),
    "RX_P": ("60", B, [(95.0,119.5),(93.0,121.0),(128.0,135.0),(128.0,125.0)]),
}
for key, (u7pin, layer, pts) in bridge.items():
    n = find_net(board, "/STORAGE/BRIDGE_SATA_" + key)
    if layer == F:
        path(board, n, pts, F)
    else:
        start, source_via, cap_via = pts[0], pts[1], pts[-1]
        cap_pad = xy(pad(board, CAPS[key][0], "2"))
        path(board, n, [start, source_via], F); via(board, n, source_via)
        path(board, n, [source_via] + pts[2:], B); via(board, n, cap_via)
        path(board, n, [cap_via, cap_pad], F)

# Socket-side launches. TX transitions above the connector, traverses B.Cu
# under its body, and returns at vias outside the signal-pad field. RX uses
# F.Cu side-entry channels away from the TX launch vias.
socket = {
    "TX_N": ("C31", (155.0,130.0), B, [(155.0,130.0),(143.5,133.0)]),
    "TX_P": ("C30", (132.0,130.0), B, [(132.0,130.0),(130.5,133.25)]),
    "RX_N": ("C33", (155.0,125.0), B, [(155.0,125.0),(145.5,132.5)]),
    "RX_P": ("C32", (134.0,125.0), B, [(134.0,125.0),(131.5,132.75)]),
}
socket_pads = {"TX_N": "2", "TX_P": "1", "RX_N": "4", "RX_P": "3"}
for key, (cap, start, layer, pts) in socket.items():
    n = find_net(board, "/STORAGE/SATA_M2_" + key)
    cap_pad = xy(pad(board, cap, "1"))
    source_via = pts[0]
    target_via = pts[-1]
    # The connector body has a dense F.Cu-only no-net field.  Transition
    # immediately beside the coupling capacitor, stay on B.Cu through the
    # field, then return only for the final signal-pad dogbone.
    cap_via = (cap_pad[0] + 1.5, cap_pad[1])
    path(board, n, [cap_pad, cap_via], F); via(board, n, cap_via)
    path(board, n, [cap_via, source_via], B)
    via(board, n, source_via)
    path(board, n, pts, B); via(board, n, target_via)
    path(board, n, [target_via, xy(pad(board, "J3", socket_pads[key]))], F)

board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
