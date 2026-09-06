"""Disposable TI-U7 USB3 escape using native pad coordinates.

The expected pair order is assertion-only.  Endpoints and net objects are
read from the saved PCB; this fixture emits ordinary through-vias outside the
TI pad field and keeps all signal copper on F.Cu/B.Cu.
"""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / os.environ.get("PISXME_TI_USB3_BASE", "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI.kicad_pcb")
OUT = R / os.environ.get("PISXME_TI_USB3_OUT", "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_USB3_ORDERED_BCU.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.15)

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def pad(board, ref, number): return board.FindFootprintByReference(ref).FindPadByNumber(str(number))
def net(board, name):
    for candidate in (name, "/CORE_CM5/" + name, "/STORAGE/" + name):
        n = board.FindNet(candidate)
        if n is not None: return n
    raise RuntimeError("missing native net " + name)
def track(board, n, a, z, layer):
    if a == z: return
    t = pcbnew.PCB_TRACK(board); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(n); board.Add(t)
def via(board, n, p):
    v = pcbnew.PCB_VIA(board); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5))
    v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F, B); v.SetNet(n); board.Add(v)
def path(board, n, pts, layer):
    for a, z in zip(pts, pts[1:]): track(board, n, a, z, layer)

b = pcbnew.LoadBoard(str(BASE))
jobs = [("CM5_USB3_RX_N", "128", "42"), ("CM5_USB3_RX_P", "130", "43"),
        ("CM5_USB3_TX_N", "140", "45"), ("CM5_USB3_TX_P", "142", "46")]
for name, jp, _ in jobs:
    pad(b, "J7", jp).SetNet(net(b, name))
terms = [(name, xy(pad(b, "J7", jp)), xy(pad(b, "U7", up))) for name, jp, up in jobs]
for item in list(b.GetTracks()):
    if "CM5_USB3_" in item.GetNetname(): b.RemoveNative(item)

# Ordered source-side vias are outside J7.  Ordered target-side vias are
# outside the TI exposed-pad field (the TI USB3 lands are x=92.2 mm).
for idx, (name, src, dst) in enumerate(terms):
    n = net(b, name)
    sx = 75.0 + idx * 2.0
    tx = 90.0
    sv = (sx, src[1]); tv = (tx, dst[1])
    path(b, n, [src, sv], B); via(b, n, sv)
    # Keep the long shared corridor on F.Cu over the approved In1 reference;
    # B.Cu is used only for the source-side escape from J7.
    path(b, n, [sv, (tx, src[1]), tv], F); via(b, n, tv)
    path(b, n, [tv, dst], F)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
