"""Disposable Path-A storage-rail repair: connect J3 power pads on In2.

This deliberately uses the saved V79 native board and only adds pad-derived
F.Cu dogbones, ordinary through vias, and a narrow In2 STORAGE_3V3 pocket.
No signal-layer collector is authored through the SATA launch field.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_STORAGE_V79_HARMLESS_ADD.kicad_pcb"
OUT = ROOT / "PHASE24_STORAGE_M2_POWER_IN2_ZONE_V1562.kicad_pcb"
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
track(pt(232.0, via_y), pt(232.0, 149.05), pcbnew.In2_Cu, 0.60)

# A remote source column reaches the U14.5 source on In2, so no F.Cu power
# collector traverses the M.2 signal launch field.
via(232.0, via_y)
via(232.0, 149.05)
track(pt(232.0, 149.05), pt(232.0, via_y), pcbnew.F_Cu, 0.60)
track(pt(232.0, 149.05), pt(211.1, 149.05), pcbnew.F_Cu, 0.60)

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
pcbnew.SaveBoard(str(OUT), b)
print(OUT)
