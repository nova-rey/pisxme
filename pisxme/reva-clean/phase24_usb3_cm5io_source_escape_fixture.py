"""Disposable USB3 fixture using the native CM5IO source-side escape.

The CM5IO source launch is copied by the measured carrier-frame transform;
the first native CM5IO via terminates the copied escape.  The remainder is
deliberately authored as separated ordinary F.Cu/B.Cu corridors to test
whether the launch, rather than the macro placement, is the limiting method.
No expected connectivity edges are synthesized.
"""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_MACRO_FRESH_STORAGE_LOCAL_J3_EDGE.kicad_pcb"
ORACLE = R / "authority-inventory/cm5io-rev2/CM5IO.kicad_pcb"
OUT = Path(os.environ.get("P24_USB3_OUT", str(R / "PHASE24_USB3_CM5IO_SOURCE_ESCAPE_FIXTURE.kicad_pcb")))
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.147)

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def pad(board, ref, number):
    p = board.FindFootprintByReference(ref).FindPadByNumber(str(number))
    if p is None: raise RuntimeError(f"missing {ref}.{number}")
    return p.GetPosition()
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def track(board, net_code, a, z, layer):
    if a == z: return
    q = pcbnew.PCB_TRACK(board); q.SetStart(a); q.SetEnd(z); q.SetLayer(layer)
    q.SetWidth(W); q.SetNetCode(net_code); board.Add(q)
def via(board, net_code, p):
    q = pcbnew.PCB_VIA(board); q.SetPosition(p); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNetCode(net_code); board.Add(q)
def polyline(board, net_code, points, layer):
    for a, z in zip(points, points[1:]): track(board, net_code, a, z, layer)

# Official Module1 is rotated relative to PiSXMe J7.  The full mirrored
# carrier-frame transform is derived from all four corresponding native USB3
# pad centers and the side of the connector body from which the CM5IO launch
# escapes: x' = 230.50-x, y' = 203.5-y.  It preserves source-side shape while
# placing the escape on the corresponding free side of the target connector.
def cm5io_to_pisxme(p):
    x, y = xy(p)
    return V(230.50 - x, 203.5 - y)

def first_via_path(board, oracle, netname, padno):
    p = oracle.FindFootprintByReference("Module1").FindPadByNumber(padno)
    def key(q): return (q.x, q.y)
    start = key(p.GetPosition())
    items = []
    via_positions = set()
    for t in list(oracle.GetTracks()):
        if t.GetNetname() != netname: continue
        if isinstance(t, pcbnew.PCB_VIA):
            pos = key(t.GetPosition()); via_positions.add(pos)
            items.append(("via", pos))
        else:
            items.append(("track", key(t.GetStart()), key(t.GetEnd()), t.GetLayer(), t.GetWidth()))
    frontier = {start}; seen = set(); result = []; reached = None
    while frontier:
        nxt = set()
        for i, rec in enumerate(items):
            if i in seen or rec[0] == "via": continue
            _, a, z, layer, width = rec
            if a not in frontier and z not in frontier: continue
            seen.add(i); result.append((a, z, layer, width))
            other = z if a in frontier else a
            if other in via_positions:
                reached = other
            else:
                nxt.add(other)
        frontier = nxt
        if reached is not None: break
    if reached is None:
        raise RuntimeError(f"no first via found for {netname}")
    return result, reached

o = pcbnew.LoadBoard(str(ORACLE))
if o is None: raise RuntimeError("native oracle load failed")
names = {
    "CM5_USB3_RX_N": ("/CM5_HighSpeed/USB3-0-RX_N", "128", "42"),
    "CM5_USB3_RX_P": ("/CM5_HighSpeed/USB3-0-RX_P", "130", "43"),
    "CM5_USB3_TX_N": ("/CM5_HighSpeed/USB3-0-TX_N", "140", "45"),
    "CM5_USB3_TX_P": ("/CM5_HighSpeed/USB3-0-TX_P", "142", "46"),
}
# Snapshot all oracle geometry before mutating the target board; KiCad 10's
# SWIG collections can invalidate native proxies across board mutations.
oracle_paths = {name: first_via_path(None, o, oracle_name, jpad)
                for name, (oracle_name, jpad, _upad) in names.items()}
b = pcbnew.LoadBoard(str(BASE))
if b is None: raise RuntimeError("native target load failed")
u7 = b.FindFootprintByReference("U7")
u7.SetOrientationDegrees(float(os.environ.get("P24_U7_ROT", "180")))
if "P24_U7_X" in os.environ and "P24_U7_Y" in os.environ:
    u7.SetPosition(V(float(os.environ["P24_U7_X"]), float(os.environ["P24_U7_Y"])))
net_codes = {name: b.FindNet("/CORE_CM5/" + name).GetNetCode() for name in names}
u7_pads = {name: pad(b, "U7", upad) for name, (_oracle_name, _jpad, upad) in names.items()}
for item in list(b.GetFootprints()):
    if item.GetReference() not in ("J7", "U7"): b.RemoveNative(item)
for item in list(b.GetTracks()): b.Remove(item)
for zone in list(b.Zones()): b.RemoveNative(zone)
print("cleared target", flush=True)

# Pair-separated endpoint vias. RX stays on B.Cu; TX stays on F.Cu between
# the CM5IO-derived first vias and these endpoint vias, avoiding an ordering
# crossing while retaining ordinary through-via transitions.
end_vias = {
    # Match the native CM5IO first-via vertical ordering; endpoint dogbones
    # are kept short at the U7 pad field.
    "CM5_USB3_RX_N": V(84.0, 120.5), "CM5_USB3_RX_P": V(84.0, 119.8),
    "CM5_USB3_TX_N": V(84.0, 121.5), "CM5_USB3_TX_P": V(84.0, 122.2),
}
if int(float(os.environ.get("P24_U7_ROT", "180"))) == 0:
    # At 0 degrees the native U7 pad order matches the CM5IO-derived source
    # order, so endpoint vias can sit directly beside their corresponding pads.
    end_vias = {
        "CM5_USB3_RX_N": V(93.5, pcbnew.ToMM(u7_pads["CM5_USB3_RX_N"].y)),
        "CM5_USB3_RX_P": V(95.5, pcbnew.ToMM(u7_pads["CM5_USB3_RX_P"].y)),
        "CM5_USB3_TX_N": V(90.0, pcbnew.ToMM(u7_pads["CM5_USB3_TX_N"].y)),
        "CM5_USB3_TX_P": V(95.5, pcbnew.ToMM(u7_pads["CM5_USB3_TX_P"].y)),
    }
    if os.environ.get("P24_LOCAL_CORRIDOR") == "1":
        # Keep the endpoint vias well outside the 0.5 mm annular copper
        # overlap while preserving the native U7-at-0-degree ordering.
        end_vias = {
            "CM5_USB3_RX_N": V(pcbnew.ToMM(u7_pads["CM5_USB3_RX_N"].x) - 1.5, pcbnew.ToMM(u7_pads["CM5_USB3_RX_N"].y)),
            "CM5_USB3_RX_P": V(pcbnew.ToMM(u7_pads["CM5_USB3_RX_P"].x) + 0.5, pcbnew.ToMM(u7_pads["CM5_USB3_RX_P"].y)),
            "CM5_USB3_TX_N": V(pcbnew.ToMM(u7_pads["CM5_USB3_TX_N"].x) - 1.5, pcbnew.ToMM(u7_pads["CM5_USB3_TX_N"].y)),
            "CM5_USB3_TX_P": V(pcbnew.ToMM(u7_pads["CM5_USB3_TX_P"].x) + 0.5, pcbnew.ToMM(u7_pads["CM5_USB3_TX_P"].y)),
        }
for target_name, (oracle_name, jpad, upad) in names.items():
    net_code = net_codes[target_name]
    copied, first = oracle_paths[target_name]
    for a, z, layer, _width in copied:
        track(b, net_code, cm5io_to_pisxme(pcbnew.VECTOR2I(a[0], a[1])), cm5io_to_pisxme(pcbnew.VECTOR2I(z[0], z[1])), layer)
    src_via = cm5io_to_pisxme(pcbnew.VECTOR2I(first[0], first[1]))
    txp_fcu = target_name.endswith("TX_P") and os.environ.get("P24_TXP_FCU") == "1"
    if not txp_fcu:
        via(b, net_code, src_via)
    ev = end_vias[target_name]
    if not txp_fcu:
        via(b, net_code, ev)
    if os.environ.get("P24_LOCAL_CORRIDOR") == "1":
        # The moved-endpoint experiment deliberately uses a direct B.Cu
        # corridor; the native source-side escape still retains its exact
        # CM5IO layer geometry and ordinary through-via at the source.
        if target_name.startswith("CM5_USB3_TX"):
            outer_x = 96.0 if target_name.endswith("TX_N") else 98.0
            top_y = 78.0 if target_name.endswith("TX_N") else 78.5
            local_layer = F if txp_fcu else B
            polyline(b, net_code, [src_via, V(pcbnew.ToMM(src_via.x), top_y), V(outer_x, top_y), V(outer_x, pcbnew.ToMM(ev.y)), ev], local_layer)
        else:
            track(b, net_code, src_via, ev, B)
    elif target_name.startswith("CM5_USB3_RX"):
        track(b, net_code, src_via, ev, B)
    else:
        # Keep TX on B.Cu, first step above the J7 NPTH obstruction, then use
        # distinct outer x-channels before descending outside the RX corridor.
        outer_x = 100.0 if target_name.endswith("TX_N") else 102.0
        outer = V(outer_x, pcbnew.ToMM(src_via.y))
        top_y = 78.0 if target_name.endswith("TX_N") else 78.5
        top_at_via = V(pcbnew.ToMM(src_via.x), top_y)
        top = V(outer_x, top_y)
        route_layer = F if ((target_name.endswith("TX_P") and os.environ.get("P24_TXP_FCU") == "1") or (target_name.endswith("TX_N") and os.environ.get("P24_TXN_FCU") == "1")) else B
        if target_name.endswith("TX_N") and os.environ.get("P24_TXN_LOCAL") == "1":
            mid_y = 122.5
            polyline(b, net_code, [src_via, top_at_via, top, V(outer_x, mid_y), V(90.0, mid_y), ev], route_layer)
        else:
            lower = V(outer_x, pcbnew.ToMM(ev.y))
            polyline(b, net_code, [src_via, top_at_via, top, lower, ev], route_layer)
    track(b, net_code, ev, u7_pads[target_name], F)

b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
