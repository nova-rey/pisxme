"""V120 disposable CM5IO-style shifted USB3 escape to native U12."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_STORAGE_COPPER_SCRUBBED_V116.kicad_pcb'
OUT = R / 'PHASE24_STORAGE_USB3_SHIFTED_ESCAPE_V124.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.13208)
JOBS = (
    ('CM5_USB3_RX_N', '128', '16', (72, 103.9), (145, 137.8)),
    ('CM5_USB3_RX_P', '130', '15', (75, 105.2), (147, 137.4)),
    ('CM5_USB3_TX_N', '140', '12', (77, 108), (149, 136.2)),
    ('CM5_USB3_TX_P', '142', '11', (70.8, 112), (151, 135.8)),
)


def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p):
    p = p.GetPosition() if hasattr(p, 'GetPosition') else p
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)


def segment(board, net, layer, points):
    for a, z in zip(points, points[1:]):
        if a == z: continue
        t = pcbnew.PCB_TRACK(board)
        t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
        t.SetWidth(W); t.SetNet(net); board.Add(t)


def via(board, net, point):
    q = pcbnew.PCB_VIA(board)
    q.SetPosition(V(*point)); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B)
    q.SetNet(net); board.Add(q)


b = pcbnew.LoadBoard(str(BASE))
j7, u12 = b.FindFootprintByReference('J7'), b.FindFootprintByReference('U12')
if j7 is None or u12 is None: raise RuntimeError('missing J7/U12')
names = {x[0] for x in JOBS}
for item in list(b.GetTracks()):
    if item.GetNetname().rsplit('/', 1)[-1] in names:
        b.RemoveNative(item)
perst = 'CM5_PERST'
# Local single-ended PERST duck: preserve its fixed endpoints while moving
# only the vertical trunk segment to B.Cu through the U12 final-mile window.
for t in list(b.GetTracks()):
    if t.GetNetname().rsplit('/', 1)[-1] == perst and t.GetLayer() == F:
        a, z = xy(t.GetStart()), xy(t.GetEnd())
        if (abs(a[0] - 152.54) < .01 and abs(z[0] - 152.54) < .01
                and {round(a[1], 2), round(z[1], 2)} == {88.73, 150.0}):
            b.RemoveNative(t)
            n = b.FindNet('/CORE_CM5/' + perst) or b.FindNet(perst)
            segment(b, n, F, [(152.54, 88.73), (152.54, 134.0)])
            via(b, n, (152.54, 134.0))
            segment(b, n, B, [(152.54, 134.0), (152.54, 139.5)])
            via(b, n, (152.54, 139.5))
            segment(b, n, F, [(152.54, 139.5), (152.54, 150.0)])
            break

for name, jp, up, source_via, target_via in JOBS:
    net = b.FindNet('/CORE_CM5/' + name) or b.FindNet(name)
    if net is None: raise RuntimeError('missing ' + name)
    source, target = xy(j7.FindPadByNumber(jp)), xy(u12.FindPadByNumber(up))
    if name == 'CM5_USB3_RX_P':
        launch = (71.2, source[1])
        segment(b, net, F, [source, launch, (launch[0], source_via[1]), source_via])
    elif name == 'CM5_USB3_TX_P':
        launch = (70.8, source[1])
        segment(b, net, F, [source, launch, source_via])
    else:
        segment(b, net, F, [source, (source_via[0], source[1]), source_via])
    via(b, net, source_via)
    segment(b, net, B, [source_via, target_via])
    via(b, net, target_via)
    segment(b, net, F, [target_via, (target_via[0], target[1]), target])

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
