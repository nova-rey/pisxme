"""Disposable USB3 fixture using the native CM5IO source-side escape.

The CM5IO source launch is copied by the measured carrier-frame transform;
the first native CM5IO via terminates the copied escape.  The remainder is
deliberately authored as separated ordinary F.Cu/B.Cu corridors to test
whether the launch, rather than the macro placement, is the limiting method.
No expected connectivity edges are synthesized.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_MACRO_FRESH_STORAGE_LOCAL_J3_EDGE.kicad_pcb"
ORACLE = R / "authority-inventory/cm5io-rev2/CM5IO.kicad_pcb"
OUT = R / "PHASE24_USB3_CM5IO_SOURCE_ESCAPE_FIXTURE.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.147)

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def pad(board, ref, number):
    p = board.FindFootprintByReference(ref).FindPadByNumber(str(number))
    if p is None: raise RuntimeError(f"missing {ref}.{number}")
    return p.GetPosition()
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def track(board, net, a, z, layer):
    if a == z: return
    q = pcbnew.PCB_TRACK(board); q.SetStart(a); q.SetEnd(z); q.SetLayer(layer)
    q.SetWidth(W); q.SetNet(net); board.Add(q)
def via(board, net, p):
    q = pcbnew.PCB_VIA(board); q.SetPosition(p); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(net); board.Add(q)

# Official Module1 is rotated relative to PiSXMe J7.  This affine frame was
# derived from all four corresponding native USB3 pad centers: x' = x-90.42,
# y' = 203.5-y.  It preserves the exact source-side shape and ordering.
def cm5io_to_pisxme(p):
    x, y = xy(p)
    return V(x - 90.42, 203.5 - y)

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

b = pcbnew.LoadBoard(str(BASE)); print("loaded target", flush=True); o = pcbnew.LoadBoard(str(ORACLE)); print("loaded oracle", flush=True)
if b is None or o is None: raise RuntimeError("native board load failed")
names = {
    "CM5_USB3_RX_N": ("/CM5_HighSpeed/USB3-0-RX_N", "128", "42"),
    "CM5_USB3_RX_P": ("/CM5_HighSpeed/USB3-0-RX_P", "130", "43"),
    "CM5_USB3_TX_N": ("/CM5_HighSpeed/USB3-0-TX_N", "140", "45"),
    "CM5_USB3_TX_P": ("/CM5_HighSpeed/USB3-0-TX_P", "142", "46"),
}
# Snapshot all oracle geometry before mutating the target board; KiCad 10's
# SWIG collections can invalidate native proxies across board mutations.
oracle_paths = {name: first_via_path(b, o, oracle_name, jpad)
                for name, (oracle_name, jpad, _upad) in names.items()}
print("snapshotted oracle", flush=True)
for item in list(b.GetFootprints()):
    if item.GetReference() not in ("J7", "U7"): b.RemoveNative(item)
for item in list(b.GetTracks()): b.Remove(item)
for zone in list(b.Zones()): b.RemoveNative(zone)
print("cleared target", flush=True)

# Pair-separated endpoint vias. RX stays on B.Cu; TX stays on F.Cu between
# the CM5IO-derived first vias and these endpoint vias, avoiding an ordering
# crossing while retaining ordinary through-via transitions.
end_vias = {
    "CM5_USB3_RX_N": V(84.0, 119.8), "CM5_USB3_RX_P": V(84.0, 120.5),
    "CM5_USB3_TX_N": V(84.0, 121.5), "CM5_USB3_TX_P": V(84.0, 122.2),
}
for target_name, (oracle_name, jpad, upad) in names.items():
    print("routing", target_name, flush=True)
    net = b.FindNet("/CORE_CM5/" + target_name)
    if net is None: raise RuntimeError(f"missing target net {target_name}")
    copied, first = oracle_paths[target_name]; print("path", len(copied), flush=True)
    for a, z, _layer, _width in copied:
        print("copy", xy(pcbnew.VECTOR2I(a[0], a[1])), xy(pcbnew.VECTOR2I(z[0], z[1])), flush=True)
        track(b, net, cm5io_to_pisxme(pcbnew.VECTOR2I(a[0], a[1])), cm5io_to_pisxme(pcbnew.VECTOR2I(z[0], z[1])), F)
    print("adding source via", flush=True)
    src_via = cm5io_to_pisxme(pcbnew.VECTOR2I(first[0], first[1])); via(b, net, src_via)
    ev = end_vias[target_name]; via(b, net, ev)
    layer = B if target_name.startswith("CM5_USB3_RX") else F
    track(b, net, src_via, ev, layer)
    track(b, net, ev, pad(b, "U7", upad), F)

b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
