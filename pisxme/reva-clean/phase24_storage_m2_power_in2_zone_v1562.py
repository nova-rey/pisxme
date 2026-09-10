"""Disposable Path-A storage-rail repair: connect J3 power pads on In2.

This deliberately uses the saved V79 native board and only adds pad-derived
F.Cu dogbones, ordinary through vias, and a narrow In2 STORAGE_3V3 pocket.
No signal-layer collector is authored through the SATA launch field.
"""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / os.environ.get("PISXME_POWER_BASE", "PHASE24_STORAGE_V79_HARMLESS_ADD.kicad_pcb")
OUT = ROOT / os.environ.get("PISXME_POWER_OUT", "PHASE24_STORAGE_M2_POWER_IN2_ZONE_V1562.kicad_pcb")
b = pcbnew.LoadBoard(str(BASE))
net = b.FindNet("STORAGE_3V3")
assert net, "STORAGE_3V3 net missing"

def mm(v):
    return pcbnew.FromMM(v)

def pt(x, y):
    return pcbnew.VECTOR2I(mm(x), mm(y))

def track(a, z, layer, width=0.30):
    t = pcbnew.PCB_TRACK(b)
    t.SetStart(a); t.SetEnd(z); t.SetLayer(layer)
    t.SetWidth(mm(width)); t.SetNetCode(net.GetNetCode())
    b.Add(t)

def via(x, y):
    v = pcbnew.PCB_VIA(b)
    p = pt(x, y); v.SetPosition(p); v.SetWidth(mm(0.80)); v.SetDrill(mm(0.40))
    v.SetNetCode(net.GetNetCode()); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    b.Add(v)

# J3's nine native STORAGE_3V3 pads are the source of these exact launches.
xs = [211.0, 211.5, 213.5, 214.0, 214.5, 215.0, 228.0, 228.5, 229.0]
pad_y = 167.275
via_y = 174.0
for x in xs:
    track(pt(x, pad_y), pt(x, via_y), pcbnew.F_Cu)

# Cluster the tightly spaced socket contacts onto two ordinary vias rather
# than violating the board's minimum drilled-hole spacing with one via/pad.
via(213.0, via_y)
via(228.5, via_y)
for x in xs[:6]:
    track(pt(x, via_y), pt(213.0, via_y), pcbnew.F_Cu)
for x in xs[6:]:
    track(pt(x, via_y), pt(228.5, via_y), pcbnew.F_Cu)

# An explicit In2 power spine joins the ordinary through-vias.  This is a
# designated low-voltage power-layer route, not an ordinary signal route.
for x in (213.0, 228.5):
    track(pt(x, via_y), pt(232.0, via_y), pcbnew.In2_Cu, 0.60)
track(pt(232.0, via_y), pt(232.0, 146.0), pcbnew.In2_Cu, 0.60)

# A remote source column reaches the U14.5 source on In2, so no F.Cu power
# collector traverses the M.2 signal launch field.
via(232.0, 146.0)
track(pt(232.0, 146.0), pt(211.1, 146.0), pcbnew.F_Cu, 0.60)
track(pt(211.1, 146.0), pt(211.1, 149.05), pcbnew.F_Cu, 0.60)

# Optional source-owned support-pad attachment for the integrated trial.  It
# is disabled by default so the original V1562 fixture remains reproducible.
if os.environ.get("PISXME_ATTACH_STORAGE_SUPPORT") == "1":
    support = {
        "U12": [(153.5, 136.6, 151.5, 136.6),
                (154.8, 139.5, 154.8, 142.0),
                (156.5, 135.0, 159.0, 135.0)],
        "U13": [(178.5, 133.4, 176.0, 133.4),
                (178.5, 136.6, 176.0, 136.6),
                (179.8, 139.5, 179.8, 142.0),
                (181.5, 135.0, 184.0, 135.0)],
        "R81": [(125.5, 145.0, 125.5, 147.0)],
    }
    if os.environ.get("PISXME_SUPPORT_VARIANT") == "u12_separated":
        support = {
            "U12": [(153.5, 136.6, 147.5, 136.6),
                    (154.8, 139.5, 157.0, 142.0),
                    (156.5, 135.0, 161.5, 134.0)],
        }
    if os.environ.get("PISXME_SUPPORT_VARIANT") == "u12_pad13_monotonic":
        support = {"U12": [(153.5, 136.6, 153.5, 133.5)]}
    if os.environ.get("PISXME_SUPPORT_VARIANT") == "r81_only":
        # Escape diagonally into the open pocket above R81.  The prior
        # horizontal escape crossed the adjacent C85/JMS_RESET_N launch.
        support = {"R81": [(125.5, 145.0, 126.5, 144.2)]}
    if os.environ.get("PISXME_SUPPORT_VARIANT") == "u12_pad13_far":
        # A distinct source-field class: leave the QFN edge immediately,
        # then place the ordinary via outside the pad/via field.
        support = {"U12": [(153.5, 136.6, 149.0, 136.6)]}
    spine = pt(188.0, 146.0)
    if os.environ.get("PISXME_SUPPORT_VARIANT") == "u12_pad13_monotonic":
        spine = pt(232.0, 133.5)
        track(pt(232.0, 133.5), pt(232.0, 146.0), pcbnew.In2_Cu, 0.60)
    if os.environ.get("PISXME_SUPPORT_VARIANT") == "r81_only":
        spine = pt(150.0, 138.5)
        track(pt(150.0, 138.5), pt(150.0, 145.0), pcbnew.In2_Cu, 0.60)
        track(pt(150.0, 145.0), pt(232.0, 145.0), pcbnew.In2_Cu, 0.60)
        track(pt(232.0, 145.0), pt(232.0, 146.0), pcbnew.In2_Cu, 0.60)
    if os.environ.get("PISXME_SUPPORT_VARIANT") == "u12_pad13_far":
        spine = pt(150.0, 138.5)
    track(pt(232.0, 146.0), spine, pcbnew.In2_Cu, 0.60)
    for entries in support.values():
        for px, py, vx, vy in entries:
            local_width = 0.10 if os.environ.get("PISXME_SUPPORT_VARIANT") == "u12_pad13_far" else 0.30
            track(pt(px, py), pt(vx, vy), pcbnew.F_Cu, local_width)
            via(vx, vy)
            if os.environ.get("PISXME_SUPPORT_VARIANT") == "r81_only":
                # Clear reset on F.Cu, then clear the known USB via field.
                track(pt(vx, vy), pt(132.0, 138.5), pcbnew.In2_Cu, 0.60)
                track(pt(132.0, 138.5), pt(150.0, 138.5), pcbnew.In2_Cu, 0.60)
                track(pt(150.0, 138.5), spine, pcbnew.In2_Cu, 0.60)
            else:
                track(pt(vx, vy), spine, pcbnew.In2_Cu, 0.60)

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
pcbnew.SaveBoard(str(OUT), b)
print(OUT)
