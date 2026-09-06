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
W = pcbnew.FromMM(0.15)

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

def main():
    b = pcbnew.LoadBoard(str(BASE))
    keep = {"J7", "U11", "U12", "C86", "C87"}
    for f in list(b.GetFootprints()):
        if f.GetReference() not in keep: b.RemoveNative(f)
    for t in list(b.GetTracks()): b.RemoveNative(t)
    for z in list(b.Zones()): b.RemoveNative(z)

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

    # The selector output uses explicit JMS583 USB names; TX traverses the
    # authoritative AC capacitors, RX is the selected lane without AC caps.
    for name, u11n, c, u12n in [
        ("USB_TXP1", "21", "C86", "25"),
        ("USB_TXN1", "22", "C87", "24"),
    ]:
        n1 = net(b, name); own(pad(b, "U11", u11n), n1); own(pad(b, c, "1"), n1)
        n2name = "JMS_USB3_TXP" if c == "C86" else "JMS_USB3_TXN"
        n2 = net(b, n2name); own(pad(b, c, "2"), n2); own(pad(b, "U12", u12n), n2)
        y = 135.0 if c == "C86" else 138.0
        path(b, n1, [pos(pad(b, "U11", u11n)), V(155, y), pos(pad(b, c, "1"))], B)
        path(b, n2, [pos(pad(b, c, "2")), V(160, y), pos(pad(b, "U12", u12n))], B)
    for name, u11n, u12n in [("USB_RXP1", "26", "23"), ("USB_RXN1", "27", "22")]:
        n = net(b, name); own(pad(b, "U11", u11n), n); own(pad(b, "U12", u12n), n)
        y = 145.0 if u11n == "26" else 148.0
        path(b, n, [pos(pad(b, "U11", u11n)), V(158, y), pos(pad(b, "U12", u12n))], B)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
