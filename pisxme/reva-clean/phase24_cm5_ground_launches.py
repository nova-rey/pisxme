"""Disposable CM5-ground launch test with a net-isolated local plane island."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_J1_POWER_GROUND_COLUMNS.kicad_pcb"
OUT = ROOT / "PHASE24_CM5_GROUND_LAUNCHES.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("/CORE_CM5/POWER_GND")
if n is None:
    raise RuntimeError("missing CM5 ground net")


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def track(a, z):
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(pcbnew.F_Cu)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(0.20))
    t.SetStart(p(*a))
    t.SetEnd(p(*z))
    b.Add(t)


def via(x, y):
    v = pcbnew.PCB_VIA(b)
    v.SetNet(n)
    v.SetPosition(p(x, y))
    v.SetWidth(pcbnew.FromMM(0.50))
    v.SetDrill(pcbnew.FromMM(0.25))
    b.Add(v)


j7 = next(fp for fp in b.GetFootprints() if fp.GetReference() == "J7")
# Move outward from each of the four connector pad columns. The vias are not
# in-pad and the local island remains a distinct net until schematic authority
# explicitly resolves CM5 ground versus global POWER_GND.
for pad in j7.Pads():
    if pad.GetNetCode() != n.GetNetCode():
        continue
    x = float(pad.GetPosition().x) / 1_000_000.0
    y = float(pad.GetPosition().y) / 1_000_000.0
    dx = -3.00 if x < 50.0 else 3.00
    vx = x + dx
    via(vx, y)
    track((x, y), (vx, y))

# Dedicated CM5-ground plane island on In1; global POWER_GND remains a
# separate net and is cleared by KiCad's normal zone rules.
z = pcbnew.ZONE(b)
z.SetLayer(pcbnew.In1_Cu)
z.SetNet(n)
z.SetNetCode(n.GetNetCode())
z.SetIsRuleArea(False)
z.SetMinThickness(pcbnew.FromMM(0.20))
z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL)
z.SetZoneName("REV_A_CM5_POWER_GND_ISLAND")
poly = pcbnew.VECTOR_VECTOR2I()
for xy in ((30, 97), (73, 97), (73, 120), (30, 120)):
    poly.append(p(*xy))
z.AddPolygon(poly)
b.Add(z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
