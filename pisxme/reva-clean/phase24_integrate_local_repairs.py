"""Compose the currently accepted local Phase 24 copper repairs.

This is a disposable integration candidate. All additions are explicit
same-net PCB geometry; no schematic connectivity is generated here.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_PGND_CLUSTER.kicad_pcb"
OUT = ROOT / "PHASE24_LOCAL_REPAIRS_COMPOSED.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def add(name, layer, a, z, width=0.20):
    n = b.FindNet(name)
    if n is None:
        raise RuntimeError(name)
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(layer)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(width))
    t.SetStart(p(*a))
    t.SetEnd(p(*z))
    b.Add(t)


def field(name, ox, oy, ground_right=True):
    # exposed 12V field, with NC pad 15 bypassed on the outside
    add("12V_PROTECTED", pcbnew.F_Cu, (ox - 2.25, oy - 2.0), (ox + 2.25, oy - 2.0))
    side = ox + 1.20 if ground_right else ox - 1.50
    add("12V_PROTECTED", pcbnew.F_Cu, (ox + 2.25, oy - 2.0), (side, oy - 2.0))
    add("12V_PROTECTED", pcbnew.F_Cu, (side, oy - 2.0), (side, oy - 0.75))
    add("12V_PROTECTED", pcbnew.F_Cu, (side, oy - 0.75), (ox + 2.25, oy - 0.75))
    # POWER_GND is intentionally omitted here: its accepted perimeter
    # geometry is evaluated in a separate candidate so the 12V escape cannot
    # silently cross the return field.


# U3/U5 field repairs and the proven U4 protected-12V perimeter escape.
field("12V_PROTECTED", 60.0, 165.0, True)
field("12V_PROTECTED", 235.0, 105.0, True)
ox, oy = 225.0, 105.0
for a, z in [
    ((ox - 2.25, oy - 2.0), (ox - 3.50, oy - 2.0)),
    ((ox - 3.50, oy - 2.0), (ox - 3.50, oy - 4.50)),
    ((ox - 3.50, oy - 4.50), (ox + 5.50, oy - 4.50)),
    ((ox + 5.50, oy - 4.50), (ox + 5.50, oy - 2.0)),
    ((ox + 5.50, oy - 2.0), (ox + 2.25, oy - 2.0)),
    ((ox + 5.50, oy - 2.0), (ox + 5.50, oy - 0.75)),
    ((ox + 5.50, oy - 0.75), (ox + 2.25, oy - 0.75)),
]:
    add("12V_PROTECTED", pcbnew.F_Cu, a, z)

# Bridge 1V1/3V3 pad-field escapes around the intervening ground pad 6.
for name, ox, oy in (("/REGULATORS/BRIDGE_1V1", 235.0, 105.0),
                     ("/REGULATORS/BRIDGE_3V3", 225.0, 105.0)):
    add(name, pcbnew.F_Cu, (ox - 2.25, oy + 0.25), (ox - 3.50, oy + 0.25))
    add(name, pcbnew.F_Cu, (ox - 3.50, oy + 0.25), (ox - 3.50, oy + 2.0))
    add(name, pcbnew.F_Cu, (ox - 3.50, oy + 2.0), (ox - 2.25, oy + 2.0))
    add(name, pcbnew.F_Cu, (ox - 2.25, oy + 2.0), (ox + 2.25, oy + 2.0))

# Keep both fuse sides separate while joining each four-pad field.
for name, xs in (("/POWER_INPUT/12V_IN_A", (233.6, 237.1)),
                 ("/POWER_INPUT/FUSED_12V_A", (242.9, 246.4)),
                 ("/POWER_INPUT/12V_IN_B", (43.6, 47.1)),
                 ("/POWER_INPUT/FUSED_12V_B", (52.9, 56.4))):
    x1, x2 = xs
    y1, y2 = (38.75, 41.25) if x1 > 200 else (118.75, 121.25)
    add(name, pcbnew.F_Cu, (x1, y1), (x1, y2))
    add(name, pcbnew.F_Cu, (x2, y1), (x2, y2))
    add(name, pcbnew.F_Cu, (x1, y1), (x2, y1))

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
