"""Build an isolated native USB3 source/selector/JMS583 fixture.

This deliberately starts from the saved placement but retains only the
physical objects needed for the USB3 discriminator.  No expected graph edges
are injected: every endpoint is an actual saved pad and every connection is
native PCB copper.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_DUAL_MODE_STORAGE_PLACEMENT.kicad_pcb"
OUT = R / "PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
# Match the saved board's approved minimum differential-pair width; the
# earlier 0.15-mm trial is retained only as rejected evidence.
W = pcbnew.FromMM(0.20)

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def pos(p): return p.GetPosition()
def fp(b, ref):
    f = next((x for x in b.GetFootprints() if x.GetReference() == ref), None)
    if f is None: raise RuntimeError("missing footprint " + ref)
    return f
def pad(b, ref, number):
    p = next((x for x in fp(b, ref).Pads() if str(x.GetNumber()) == str(number)), None)
    if p is None: raise RuntimeError(f"missing {ref}.{number}")
    return p
def net(b, name):
    n = b.FindNet(name)
    if n is None: raise RuntimeError("missing net " + name)
    return n
def own(p, n):
    p.SetNet(n); p.SetNetCode(n.GetNetCode())
def seg(b, n, a, z, layer):
    if a == z: return
    t = pcbnew.PCB_TRACK(b); t.SetStart(a); t.SetEnd(z); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(n); b.Add(t)
def via(b, n, x, y):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(x, y)); q.SetWidth(pcbnew.FromMM(.55))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(n); b.Add(q)
def path(b, n, points, layer):
    for a, z in zip(points, points[1:]): seg(b, n, a, z, layer)

def escape_via(b, n, p, x, y):
    """Escape an SMD endpoint on F.Cu before entering a B.Cu lane."""
    a = pos(p)
    path(b, n, [a, V(x, pcbnew.ToMM(a.y)), V(x, y)], F)
    via(b, n, x, y)

def main():
    b = pcbnew.LoadBoard(str(BASE))
    keep = {"J7", "U11", "U12", "C86", "C87"}
    for f in list(b.GetFootprints()):
        if f.GetReference() not in keep: b.RemoveNative(f)
    for t in list(b.GetTracks()): b.RemoveNative(t)
    for z in list(b.Zones()): b.RemoveNative(z)

    # Keep the disposable TX coupling parts in the local bridge neighborhood;
    # their historical acreage coordinates are not a routing constraint.
    fp(b, "C86").SetPosition(V(190, 165))
    fp(b, "C87").SetPosition(V(190, 170))

    # Source authority and U12 source side.
    source = [
        ("/CORE_CM5/CM5_USB3_RX_N", "128", "16"),
        ("/CORE_CM5/CM5_USB3_RX_P", "130", "15"),
        ("/CORE_CM5/CM5_USB3_TX_N", "140", "12"),
        ("/CORE_CM5/CM5_USB3_TX_P", "142", "11"),
    ]
    # Escape in the actual CM5 pad order (RX_N, RX_P, TX_N, TX_P), then use a
    # monotonic B.Cu corridor to the corresponding U12 bottom-edge pads.
    source_vias = {"128": (74.0, 100.0), "130": (78.0, 102.0),
                   "140": (82.0, 104.0), "142": (86.0, 106.0)}
    # RUA0042A pins 11/12/15/16 are on the left long edge in the documented
    # 17/4/17/4 perimeter. Leave the package outward (-X) and spread the
    # through-vias well outside the 0.4-mm signal pitch.
    target_vias = {"128": (156.0, 160.0), "130": (158.0, 156.0),
                   "140": (160.0, 152.0), "142": (162.0, 148.0)}
    for name, j7n, u12n in source:
        n = net(b, name); a = pos(pad(b, "J7", j7n)); z = pos(pad(b, "U12", u12n))
        own(pad(b, "U12", u12n), n)
        sx, sy = source_vias[j7n]; tx, ty = target_vias[j7n]
        path(b, n, [a, V(sx, sy)], F); via(b, n, sx, sy)
        path(b, n, [V(sx, sy), V(tx, ty)], B); via(b, n, tx, ty)
        # U12 pins 11/12/15/16 are on the package bottom edge.  The final
        # F.Cu segment is a short outward dogbone from a full-pitch-spaced
        # via, never a horizontal approach through the pad row.
        # Stay outside the long-edge pad row until the target Y, then enter
        # horizontally; a diagonal from the via cuts through its neighbor.
        path(b, n, [V(tx, ty), V(tx, pcbnew.ToMM(z.y)), z], F)

    # The actual JMS583 QFN64 USB pads are all on its bottom edge.  Keep the
    # complete selector continuation on a separate F.Cu local island for this
    # placement discriminator; the CM5 source fanout above is B.Cu.
    for src_name, u11n, cref, dst_name, u12n, y1, y2 in [
        ("USB_TXP1", "21", "C86", "JMS_USB3_TXP", "25", 165.0, 152.0),
        ("USB_TXN1", "22", "C87", "JMS_USB3_TXN", "24", 170.0, 152.4),
    ]:
        n1 = net(b, src_name); p11 = pad(b, "U11", u11n); c1 = pad(b, cref, "1")
        own(p11, n1); own(c1, n1)
        path(b, n1, [pos(p11), V(pos(p11).x and pcbnew.ToMM(pos(p11).x), y1), V(180, y1), pos(c1)], F)
        n2 = net(b, dst_name); c2 = pad(b, cref, "2"); p12 = pad(b, "U12", u12n)
        own(c2, n2); own(p12, n2)
        # Keep both bridge-side TX legs on the reserved B.Cu corridor.  Only
        # their SMD endpoint escapes remain on F.Cu, so the RX dogbones cannot
        # cross a TX vertical segment at the U12 edge.
        cvia = (192.0, 165.0) if cref == "C86" else (194.0, 170.0)
        xout = 215.0 if cref == "C86" else 220.0
        escape_via(b, n2, c2, *cvia); escape_via(b, n2, p12, xout, y2)
        path(b, n2, [V(*cvia), V(xout, pcbnew.ToMM(pos(c2).y)), V(xout, y2)], B)
    for name, u11n, u12n, y1, y2, xout in [
        ("USB_RXP1", "26", "23", 175.0, 152.8, 225.0),
        ("USB_RXN1", "27", "22", 180.0, 153.2, 230.0),
    ]:
        n = net(b, name); p11 = pad(b, "U11", u11n); p12 = pad(b, "U12", u12n)
        own(p11, n); own(p12, n)
        # RX uses the reserved B.Cu corridor.  The two F.Cu dogbones are
        # outside the SMD pad rows and terminate in ordinary through-vias.
        # The adjacent QFN64 RX pads share a bottom-edge row.  Give RXP a
        # lateral 0.6-mm escape so its via is not parallel/clearance-bound
        # to the RXN pad escape.
        xv = 150.0 if u11n == "26" else 149.0
        # RXN drops on F.Cu to the lower lane height; this keeps its B.Cu
        # launch from crossing the RXP return vertical at x=235.
        yv = 170.0 if u11n == "26" else 200.0
        tx = 235.0 if u11n == "26" else 240.0
        ty = 190.0 if u11n == "26" else 200.0
        if u11n == "26":
            # RXP is the third-from-left bottom-edge pad.  Exit downward
            # before moving laterally; a horizontal first move would cross
            # the adjacent QFN64 pads.
            a = pos(p11)
            path(b, n, [a, V(pcbnew.ToMM(a.x), 158.0), V(xv, yv)], F)
            via(b, n, xv, yv)
        else:
            escape_via(b, n, p11, xv, yv)
        escape_via(b, n, p12, tx, y2)
        lane_x = 140.0 if u11n == "26" else 250.0
        path(b, n, [V(xv, yv), V(lane_x, yv), V(lane_x, ty),
                    V(tx, ty), V(tx, y2)], B)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
