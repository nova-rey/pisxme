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
# Use the board's ordinary 0.20-mm signal rule for this route-development
# fixture; the earlier 0.1321-mm trial was below the saved minimum-width rule
# and therefore could not be a valid DRC candidate.
WIDTH = pcbnew.FromMM(0.20)

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
    t.SetLayer(layer); t.SetWidth(WIDTH); t.SetNet(net); t.SetNetCode(net.GetNetCode()); board.Add(t)
def via(board, net, p):
    v = pcbnew.PCB_VIA(board); v.SetPosition(V(*p))
    v.SetWidth(pcbnew.FromMM(0.5)); v.SetDrill(pcbnew.FromMM(0.3))
    v.SetLayerPair(F, B); v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)
def path(board, net, points, layer):
    for a, z in zip(points, points[1:]): track(board, net, a, z, layer)

board = pcbnew.LoadBoard(str(BASE))
J3_ROT = int(os.environ.get("PISXME_J3_ROT", "90"))
J3_X = os.environ.get("PISXME_J3_X")
J3_Y = os.environ.get("PISXME_J3_Y")
if J3_ROT != 90 or (J3_X is not None and J3_Y is not None):
    j3 = board.FindFootprintByReference("J3")
    if j3 is None: raise RuntimeError("missing J3")
    j3.SetOrientationDegrees(J3_ROT)
    if J3_X is not None and J3_Y is not None:
        j3.SetPosition(V(float(J3_X), float(J3_Y)))
    elif J3_ROT == 0:
        j3.SetPosition(V(138.0, 95.0))

# Native capacitor positions: N is above P at the bridge and socket ends,
# and TX/RX occupy distinct physical corridors. All caps retain their
# manufacturer footprint orientation; pad 2 is bridge-side, pad 1 socket-side.
CAPS = {
    "TX_N": ("C31", (110.5, 124.0)),
    "TX_P": ("C30", (110.5, 112.0)),
    "RX_N": ("C33", (110.5, 128.0)),
    "RX_P": ("C32", (110.5, 116.0)),
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

# Remove only SATA copper, retaining the already-tested USB3 corridor.  The
# socket-side names are the canonical source names, not the superseded
# SATA_M2_* aliases used by an earlier disposable author.
for item in list(board.GetTracks()):
    if ("BRIDGE_SATA_" in item.GetNetname()
            or "SATA_M2_" in item.GetNetname()
            or "M2_SATA_" in item.GetNetname()):
        board.RemoveNative(item)

# Bridge-side escapes.  Starts are taken from the native U7 pads so this
# disposable author cannot silently drift when the verified footprint moves.
# All four members escape to separated ordinary vias, then use distinct B.Cu
# corridors to the coupling row; this avoids pretending a 0.4-mm QFN pad
# pitch can support four same-layer diagonal fanouts.
u7pads = {key: xy(pad(board, "U7", pin)) for key, pin in {
    "TX_N": "56", "TX_P": "57", "RX_N": "59", "RX_P": "60"}.items()}
bridge = {
    "TX_N": ("56", B, [u7pads["TX_N"], (96.2,129.0), (97.4,130.0),
                         (100.0,130.0), (100.0,124.0), (109.0,124.0)]),
    "TX_P": ("57", B, [u7pads["TX_P"], (95.8,130.5), (94.6,132.0),
                         (102.0,132.0), (102.0,112.0), (109.0,112.0)]),
    "RX_N": ("59", F, [u7pads["RX_N"], (95.0,131.5), (92.0,134.0),
                         (104.0,134.0), (104.0,128.0), (109.0,128.0)]),
    "RX_P": ("60", F, [u7pads["RX_P"], (94.6,132.5), (91.0,136.0),
                         (108.0,136.0), (108.0,116.0), (109.0,116.0)]),
}
for key, (u7pin, layer, pts) in bridge.items():
    n = find_net(board, "/STORAGE/BRIDGE_SATA_" + key)
    cap_pad = xy(pad(board, CAPS[key][0], "2"))
    if layer == F:
        path(board, n, pts[:-1] + [cap_pad], F)
    else:
        source_via, cap_via = pts[2], pts[-1]
        path(board, n, pts[:3], F); via(board, n, source_via)
        path(board, n, [source_via] + pts[3:], B); via(board, n, cap_via)
        path(board, n, [cap_via, cap_pad], F)

# Socket-side launches. TX transitions above the connector, traverses B.Cu
# under its body, and returns at vias outside the signal-pad field. RX uses
# F.Cu side-entry channels away from the TX launch vias.
socket = {
    "TX_N": ("C31", (112.0,124.0), B, [(112.0,124.0),(126.75,126.275)]),
    "TX_P": ("C30", (112.0,112.0), B, [(112.0,112.0),(126.5,118.725)]),
    "RX_N": ("C33", (112.0,128.0), B, [(112.0,128.0),(127.25,126.275)]),
    "RX_P": ("C32", (112.0,116.0), B, [(112.0,116.0),(126.75,118.725)]),
}
socket_nets = {
    "TX_P": "M2_SATA_A_P_PCIE_TXP0",
    "TX_N": "M2_SATA_A_N_PCIE_TXN0",
    "RX_P": "M2_SATA_B_N_PCIE_RXP0",
    "RX_N": "M2_SATA_B_P_PCIE_RXN0",
}
# M-key Socket 3 authority: SATA A is contacts 49/47 and SATA B is
# contacts 43/41.  The SATA B polarity is intentionally crossed by the
# reviewed CM5IO-derived mapping and must not be inferred from pad order.
socket_pads = {"TX_N": "47", "TX_P": "49", "RX_N": "41", "RX_P": "43"}
if J3_ROT == 90:
    # Rotating the socket makes the signal contacts a vertical, monotonic
    # launch.  Derive its actual post-transform positions and use separate
    # ordinary-via lanes; do not use the historical guessed coordinates.
    j3pads = {key: xy(pad(board, "J3", number)) for key, number in socket_pads.items()}
    socket = {
        "TX_N": ("C31", (114.0,124.0), B, [(114.0,124.0),(123.0,124.0),
                                               (123.0,j3pads["TX_N"][1])]),
        "TX_P": ("C30", (114.0,112.0), B, [(114.0,112.0),(121.0,112.0),
                                               (121.0,j3pads["TX_P"][1])]),
        "RX_N": ("C33", (114.0,128.0), F, [(130.0,128.0),
                                               (130.0,j3pads["RX_N"][1])]),
        "RX_P": ("C32", (114.0,116.0), F, [(129.0,116.0),
                                               (129.0,j3pads["RX_P"][1])]),
    }
    final_dogbones = {key: [(pts[-1][0], pts[-1][1]), j3pads[key]]
                      for key, (_, _, _, pts) in socket.items()}
final_dogbones = locals().get("final_dogbones", {})
if J3_ROT == 0:
    # In the native 0-degree footprint the two members of each row are
    # adjacent F.Cu lands.  Stagger their approach Y coordinates so the
    # final dogbones do not cross or share a via clearance envelope.
    socket = {
        "TX_N": ("C31", (114.0,124.0), B, [(114.0,124.0),(125.0,105.0)]),
        "TX_P": ("C30", (114.0,112.0), B, [(114.0,112.0),(126.0,87.0)]),
        "RX_N": ("C33", (114.0,128.0), B, [(114.0,128.0),(126.0,110.0)]),
        "RX_P": ("C32", (114.0,116.0), B, [(114.0,116.0),(116.0,116.0),
                                               (116.0,114.0),(118.0,114.0),
                                               (118.0,116.0),(127.0,93.0)]),
    }
    # Keep the final approaches monotonic with the native contact x-order.
    # The vias are outside the connector pad field; each short F.Cu dogbone
    # approaches one pad from the right without entering a neighboring land.
    final_dogbones = {
        "RX_N": [(143.0,86.5),(138.75,89.725)],
        "RX_P": [(143.0,88.0),(139.25,89.725)],
        "TX_N": [(143.0,91.5),(140.25,89.725)],
        "TX_P": [(143.0,93.0),(140.75,89.725)],
    }
for key, (cap, start, layer, pts) in socket.items():
    n = find_net(board, socket_nets[key])
    cap_pad = xy(pad(board, cap, "1"))
    source_via = pts[0]
    target_via = pts[-1]
    # The connector body has a dense F.Cu-only no-net field.  Transition
    # immediately beside the coupling capacitor, stay on B.Cu through the
    # field, then return only for the final signal-pad dogbone.
    cap_via = (cap_pad[0] + 1.5, cap_pad[1])
    if layer == F:
        path(board, n, [cap_pad] + pts + [xy(pad(board, "J3", socket_pads[key]))], F)
    else:
        path(board, n, [cap_pad, cap_via], F); via(board, n, cap_via)
        path(board, n, [cap_via, source_via], B)
        path(board, n, pts, B); via(board, n, target_via)
        end_path = final_dogbones.get(key, [target_via])
        if end_path[0] != target_via:
            path(board, n, [target_via, end_path[0]], B)
        path(board, n, end_path, F)

board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
