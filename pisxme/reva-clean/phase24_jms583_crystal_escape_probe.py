"""Disposable native-pad crystal escape probe for the Path-A storage basis."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb"
OUT = R / "PHASE24_JMS583_CRYSTAL_ESCAPE_PROBE.kicad_pcb"

def mm(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p):
    q = p.GetPosition()
    return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)
def add_track(b, net, a, z):
    if a == z: return
    t = pcbnew.PCB_TRACK(b)
    t.SetStart(mm(*a)); t.SetEnd(mm(*z)); t.SetLayer(pcbnew.F_Cu)
    t.SetWidth(pcbnew.FromMM(0.15)); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    b.Add(t)
def add_via(b, net, p):
    v = pcbnew.PCB_VIA(b)
    v.SetPosition(mm(*p)); v.SetWidth(pcbnew.FromMM(0.50))
    v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    v.SetNet(net); v.SetNetCode(net.GetNetCode()); b.Add(v)
def add_path(b, net, points, layer):
    for a, z in zip(points, points[1:]):
        if a == z: continue
        t = pcbnew.PCB_TRACK(b)
        t.SetStart(mm(*a)); t.SetEnd(mm(*z)); t.SetLayer(layer)
        t.SetWidth(pcbnew.FromMM(0.15)); t.SetNet(net); t.SetNetCode(net.GetNetCode())
        b.Add(t)

b = pcbnew.LoadBoard(str(BASE))
u11 = b.FindFootprintByReference("U11")
y10 = b.FindFootprintByReference("Y10")
if u11 is None or y10 is None:
    raise RuntimeError("missing U11/Y10")
y10.SetPosition(mm(150.0, 125.0))
# Disposable land-pattern sensitivity only.  The current fixture's 0.22 mm
# pitch-direction pads inherently leave 0.18 mm between 0.40 mm-pitch pads;
# test the 0.20 mm candidate without changing the production footprint.
for pad in u11.Pads():
    pad.SetSize(mm(0.70, 0.20))
for name, upad, ypad, f_bends, b_bends in (
    ("XIN", "50", "1", ((137.4, 129.0), (134.0, 129.0)), ((147.0, 129.0), (147.0, 122.0))),
    ("XOUT", "51", "2", ((137.8, 128.0), (140.0, 128.0)), ((146.0, 128.0), (146.0, 123.0))),
):
    net = b.FindNet(name)
    if net is None: raise RuntimeError("missing " + name)
    for item in list(b.GetTracks()):
        if item.GetNetCode() == net.GetNetCode(): b.RemoveNative(item)
    src = xy(u11.FindPadByNumber(upad)); dst = xy(y10.FindPadByNumber(ypad))
    via = f_bends[-1]
    add_path(b, net, [src, *f_bends], pcbnew.F_Cu)
    add_via(b, net, via)
    add_path(b, net, [via, *b_bends], pcbnew.B_Cu)
    add_via(b, net, b_bends[-1])
    add_path(b, net, [b_bends[-1], dst], pcbnew.F_Cu)
b.BuildListOfNets()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
