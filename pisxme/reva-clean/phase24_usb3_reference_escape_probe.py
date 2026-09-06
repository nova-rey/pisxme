"""Disposable USB3 escape probe for the selected storage macro placement.

The route is generated from native J7/U7 pad positions.  It uses one
coherent B.Cu corridor with ordinary through-vias at the two ends, leaving
the PCIe F.Cu launch corridor available.  This is route-development evidence
only; no expected graph edges are authored.
"""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_USB3_ESCAPE_BASE", str(R / "PHASE24_MACRO_FRESH_STORAGE_LOCAL_J3_EDGE.kicad_pcb")))
OUT = Path(os.environ.get("PISXME_USB3_ESCAPE_OUT", str(R / "PHASE24_STORAGE_USB3_REFERENCE_ESCAPE.kicad_pcb")))
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.13208)

def point(p):
    return pcbnew.VECTOR2I(p.x, p.y)

def V(x, y):
    return pcbnew.VECTOR2I_MM(x, y)

def xy(board, ref, pad):
    p = board.FindFootprintByReference(ref).FindPadByNumber(str(pad))
    if p is None:
        raise RuntimeError(f"missing {ref}.{pad}")
    return p.GetPosition()

def track(board, net, a, z, layer):
    if a == z:
        return
    q = pcbnew.PCB_TRACK(board); q.SetStart(a); q.SetEnd(z)
    q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); board.Add(q)

def via(board, net, p):
    q = pcbnew.PCB_VIA(board); q.SetPosition(p)
    # Keep the ordinary through-via drill while reducing annular copper enough
    # to clear the selected board's plane-zone boundary.
    q.SetWidth(pcbnew.FromMM(0.45)); q.SetDrill(pcbnew.FromMM(0.30))
    q.SetLayerPair(F, B); q.SetNet(net); board.Add(q)

b = pcbnew.LoadBoard(str(BASE))
if b is None:
    raise RuntimeError("native board load failed")

names = ("CM5_USB3_RX_N", "CM5_USB3_RX_P", "CM5_USB3_TX_N", "CM5_USB3_TX_P")
native_ends = {}
for name, (jpad, upad, _jvia, _bend, _uvia) in {
    "CM5_USB3_RX_N": ("128", "42", None, None, None),
    "CM5_USB3_RX_P": ("130", "43", None, None, None),
    "CM5_USB3_TX_N": ("140", "45", None, None, None),
    "CM5_USB3_TX_P": ("142", "46", None, None, None),
}.items():
    native_ends[name] = (xy(b, "J7", jpad), xy(b, "U7", upad))
for item in [b.Tracks()[i] for i in range(b.Tracks().size())]:
    if any(name in str(item.GetNetname()) for name in names):
        b.Remove(item)

# Keep the pair lanes separated in a left-side B.Cu corridor.  The J7 escape
# first follows the official CM5IO launch side before turning into that
# corridor; putting the initial vias on the opposite side of the dense pad
# field creates real shorts to adjacent J7 pads.
routes = {
    "CM5_USB3_RX_N": ("128", "42", V(72.0, 103.9), None, V(64.0, 116.5), V(82.5, 119.0)),
    "CM5_USB3_RX_P": ("130", "43", V(72.0, 104.8), None, V(63.0, 118.0), V(81.5, 120.5)),
    "CM5_USB3_TX_N": ("140", "45", V(72.0, 108.0), V(72.0, 112.0), V(62.0, 119.0), V(82.5, 122.0)),
    "CM5_USB3_TX_P": ("142", "46", V(71.0, 109.0), V(71.0, 114.0), V(61.0, 121.0), V(81.5, 123.5)),
}
for name, (jpad, upad, jvia, mid, bend, uvia) in routes.items():
    net = b.FindNet("/CORE_CM5/" + name)
    if net is None:
        raise RuntimeError(f"missing net {name}")
    jp, up = native_ends[name]
    launch = V(71.2, pcbnew.ToMM(jp.y))
    if name.endswith("RX_P"):
        launch = V(71.2, 104.8)
    elif name.endswith("TX_N"):
        launch = V(71.2, 106.3)
    elif name.endswith("TX_P"):
        launch = V(71.2, 106.7)
    track(b, net, jp, launch, F); track(b, net, launch, jvia, F); via(b, net, jvia)
    if mid is not None:
        track(b, net, jvia, mid, B); track(b, net, mid, bend, B)
    else:
        track(b, net, jvia, bend, B)
    track(b, net, bend, uvia, B)
    via(b, net, uvia); track(b, net, uvia, up, F)

b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
