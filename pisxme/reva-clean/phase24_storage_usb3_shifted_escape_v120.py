"""V120 disposable CM5IO-style shifted USB3 escape to native U12."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_STORAGE_COPPER_SCRUBBED_V116.kicad_pcb'
OUT = R / 'PHASE24_STORAGE_USB3_SHIFTED_ESCAPE_V121.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.13208)
JOBS = (
    ('CM5_USB3_RX_N', '128', '16', (72, 103.9), (145, 100)),
    ('CM5_USB3_RX_P', '130', '15', (75, 105.2), (147, 104)),
    ('CM5_USB3_TX_N', '140', '12', (77, 108), (149, 108)),
    ('CM5_USB3_TX_P', '142', '11', (70.8, 112), (151, 112)),
)


def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)


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
for item in list(b.GetFootprints()):
    if item.GetReference() not in ('J7', 'U12'):
        b.RemoveNative(item)
for item in list(b.GetTracks()):
    b.RemoveNative(item)
for zone in list(b.Zones()):
    b.RemoveNative(zone)
names = {x[0] for x in JOBS}

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

b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
