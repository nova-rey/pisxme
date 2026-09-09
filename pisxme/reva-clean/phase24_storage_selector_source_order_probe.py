"""Disposable SATA source-field probe with an order-preserving capacitor row."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_STORAGE_VCCK_LOCAL_V1.kicad_pcb"
OUT = ROOT / "PHASE24_STORAGE_SATA_SOURCE_ORDER_V1.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def V(x, y):
    # Use one-micron integer quantization for every shared via/track vertex.
    # VECTOR2I_MM's floating conversion can otherwise leave a one-nanometre
    # gap in saved native connectivity at a via transition.
    return pcbnew.VECTOR2I(int(round(float(x) * 1_000_000)),
                           int(round(float(y) * 1_000_000)))
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def pad(b, r, n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def pxy(b, r, n): return xy(pad(b, r, n).GetPosition())
def net(b, name):
    for candidate in ("/STORAGE/" + name, name):
        n = b.FindNet(candidate)
        if n: return n
    raise RuntimeError(name)
def seg(b, n, a, z, layer):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def path(b, n, pts, layer):
    for a, z in zip(pts, pts[1:]): seg(b, n, a, z, layer)
def via(b, n, at):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*at)); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(n)
    q.SetNetCode(n.GetNetCode()); b.Add(q)

b = pcbnew.LoadBoard(str(BASE))
sata_tokens = ("BRIDGE_SATA_", "TUSB_SATA_")
for t in list(b.GetTracks()):
    if any(token in t.GetNetname() for token in sata_tokens): b.RemoveNative(t)

# Place the F-only coupling pads in the same lateral order as U7's native
# bottom-edge SATA pads.  This is a disposable placement experiment only.
placements = {"C32": (104.0, 119.0), "C33": (105.6, 119.0),
              "C30": (107.2, 119.0), "C31": (108.8, 119.0)}
for ref, (x, y) in placements.items():
    f = b.FindFootprintByReference(ref); f.SetPosition(V(x, y)); f.SetOrientationDegrees(0)

channels = {
    "C32": ("BRIDGE_SATA_RX_P", "TUSB_SATA_RXP", "U7", "60", "U13", "36"),
    "C33": ("BRIDGE_SATA_RX_N", "TUSB_SATA_RXN", "U7", "59", "U13", "35"),
    "C30": ("BRIDGE_SATA_TX_P", "TUSB_SATA_TXP", "U7", "57", "U13", "38"),
    "C31": ("BRIDGE_SATA_TX_N", "TUSB_SATA_TXN", "U7", "56", "U13", "37"),
}
# Leave a full-pitch corridor between each source via and its neighbor, then
# take the four B.Cu lanes monotonically to the reordered cap row.
source_vias = {"C32": (94.6, 130.2), "C33": (95.0, 131.2),
               "C30": (95.8, 130.2), "C31": (96.2, 131.2)}
for ref, (bridge, capnet, sr, sn, dr, dn) in channels.items():
    n = net(b, bridge)
    s = pxy(b, sr, sn); c2 = pxy(b, ref, "2"); c1 = pxy(b, ref, "1")
    sv = source_vias[ref]
    path(b, n, [s, (s[0], 129.0), sv], F); via(b, n, sv)
    c2v = (c2[0], c2[1] - 0.35)
    path(b, n, [sv, (sv[0], 116.5), c2v], B); via(b, n, c2v)
    path(b, n, [c2v, c2], F)
    # Selected-side route gets its own monotonic B.Cu corridor, then a
    # transition outside U13's pad field and a short F.Cu dogbone.
    target = pxy(b, dr, dn)
    lane = {"C32": 111.0, "C33": 113.0, "C30": 115.0, "C31": 117.0}[ref]
    dv = (lane, 127.0)
    snet = net(b, capnet)
    c1v = (c1[0], c1[1] + 0.35)
    path(b, snet, [c1, c1v], F); via(b, snet, c1v)
    path(b, snet, [c1v, (lane, 119.0), dv], B); via(b, snet, dv)
    path(b, snet, [dv, target], F)

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
