"""Disposable JMS583 support author co-located north of the USB3 field.

All endpoints are read from the saved native board.  This is an experiment;
it intentionally does not alter schematic ownership or infer connectivity.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_DUAL_MODE_STORAGE_USB3_LOCAL_FROM_FULL7.kicad_pcb"
OUT = R / "PHASE24_DUAL_MODE_STORAGE_USB3_SUPPORT_NORTH.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def fp(b, ref): return b.FindFootprintByReference(ref)
def pad(b, ref, number): return fp(b, ref).FindPadByNumber(str(number))
def pos(b, ref, number): return xy(pad(b, ref, number).GetPosition())
def track(b, net, a, z, layer=F, width=.20):
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z));
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net)
    t.SetNetCode(net.GetNetCode()); b.Add(t)
def via(b, net, q):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F, B); v.SetNet(net)
    v.SetNetCode(net.GetNetCode()); b.Add(v)
def clear_net(b, name):
    n = b.FindNet(name)
    for item in list(b.GetTracks()):
        if item.GetNetCode() == n.GetNetCode(): b.RemoveNative(item)
    return n
def path(b, name, ref, number, points, layer=F):
    n = b.FindNet(name); pts = [pos(b, ref, number)] + points
    for a, z in zip(pts, pts[1:]): track(b, n, a, z, layer)
def ground_return(b, ref, number, q):
    n = b.FindNet('POWER_GND'); p = pos(b, ref, number)
    via(b, n, q); track(b, n, p, q)

b = pcbnew.LoadBoard(str(BASE))
# Keep every support body in the open north acreage, away from C86/C87 and
# the bridge-side USB3 escape.  Positions are explicit and mechanically sane
# for this disposable comparison.
placements = {
    'C80': (126.5, 114.5), 'C81': (130.0, 114.5),
    'C82': (133.5, 114.5), 'C83': (137.0, 114.5),
    'C84': (119.5, 117.0), 'C85': (126.5, 117.0),
    'R81': (123.0, 117.0), 'R83': (133.5, 117.0),
    'L10': (136.0, 125.0), 'Y10': (145.0, 125.0),
}
for ref, q in placements.items(): fp(b, ref).SetPosition(P(*q))

support = ('JMS_RESET_N', 'JMS_AVDD33', 'JMS_AVDDL', 'JMS_VCCO',
           'JMS_VCCK', 'JMS_VDDREG_5V', 'LXO', 'JMS_XAVDDH', 'JMS_REXT')
for name in support: clear_net(b, name)

# Separate F.Cu corridors are assigned by source edge; the analog AVDDL and
# XAVDDH paths use ordinary through-vias and B.Cu corridors.
path(b, 'JMS_VDDREG_5V', 'U11', 1, [(136.35, 129.0), (137.15, 125.0)])
path(b, 'LXO', 'U11', 64, [(145.0, 129.0), (145.0, 123.0), (134.85, 123.0), (134.85, 125.0)])
path(b, 'JMS_VCCK', 'U11', 2, [(132.0, 132.4), (132.0, 112.5), (133.5, 112.5), (133.5, 114.5)])
path(b, 'JMS_VCCO', 'U11', 6, [(134.0, 134.0), (134.0, 111.0), (130.0, 111.0), (130.0, 114.5)])
path(b, 'JMS_AVDD33', 'U11', 19, [(144.0, 138.6), (144.0, 109.5), (126.5, 109.5), (126.5, 114.5)])
path(b, 'JMS_RESET_N', 'U11', 15, [(135.0, 137.6), (135.0, 107.5), (123.0, 107.5), (123.0, 117.0)])
path(b, 'JMS_RESET_N', 'R81', 1, [(126.5, 117.0)])
path(b, 'JMS_RESET_N', 'C85', 1, [])

def via_path(name, ref, number, first, middle, last):
    n = b.FindNet(name); s = pos(b, ref, number)
    track(b, n, s, first, F); via(b, n, first)
    prev = first
    for q in middle: track(b, n, prev, q, B); prev = q
    via(b, n, last); track(b, n, prev, last, B); track(b, n, last, pos(b, ref, number), F)

# Native pad-to-pad B.Cu corridors with explicit transitions.
for name, ref, number, first, middle, last, dest in [
    ('JMS_AVDDL', 'U11', 20, (141.8, 140.0), [(141.8, 106.5), (137.0, 106.5)], (137.0, 112.5), 'C83'),
    ('JMS_XAVDDH', 'U11', 52, (138.2, 130.0), [(117.5, 130.0), (117.5, 117.0)], (119.5, 117.0), 'C84'),
]:
    n = b.FindNet(name); s = pos(b, ref, number); d = pos(b, dest, 1)
    track(b, n, s, first, F); via(b, n, first); prev = first
    for q in middle: track(b, n, prev, q, B); prev = q
    via(b, n, last); track(b, n, prev, last, B); track(b, n, last, d, F)

# RSET remains local in the U11/U12 gap.
path(b, 'JMS_REXT', 'U11', 39, [(145.0, 135.6), (147.5, 130.0)])

for ref, number, q in [('C80','2',(125.5,114.5)), ('C81','2',(129.0,114.5)),
                       ('C82','2',(132.5,114.5)), ('C83','2',(136.0,114.5)),
                       ('C84','2',(118.5,117.0)), ('C85','2',(125.5,117.0)),
                       ('R83','2',(134.5,116.0))]:
    ground_return(b, ref, number, q)
for ref, number in [('Y10','3'), ('Y10','4')]:
    p = pos(b, ref, number); ground_return(b, ref, number, (p[0], p[1] + 1.0))
ground_return(b, 'U11', '63', (142.6, 130.0))

b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
