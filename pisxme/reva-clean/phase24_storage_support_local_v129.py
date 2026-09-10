"""V129 disposable local U11-to-U12 support escape from native pads."""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = Path(os.environ.get('PISXME_STORAGE_SUPPORT_BASE', str(R / 'PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb')))
OUT = Path(os.environ.get('PISXME_STORAGE_SUPPORT_OUT', str(R / 'PHASE24_STORAGE_SUPPORT_LOCAL_V130.kicad_pcb')))
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.13208)


def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p):
    p = p.GetPosition() if hasattr(p, 'GetPosition') else p
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def P(b, ref, number): return b.FindFootprintByReference(ref).FindPadByNumber(str(number))


def track(b, net, a, z, layer):
    if a == z: return
    q = pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z))
    q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); b.Add(q)


def via(b, net, p):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(net); b.Add(q)


b = pcbnew.LoadBoard(str(BASE))
if os.environ.get('PISXME_MOVE_U13') == '1':
    u13 = b.FindFootprintByReference('U13')
    if u13 is None: raise RuntimeError('missing U13')
    u13.SetPosition(V(200.0, 135.0))
jobs = (
    ('USB_RXP1', '26', '23', (137, 137), (160, 139.5)),
    ('USB_RXN1', '27', '22', (137, 140), (161, 141)),
)
for name, _up, _vp, _sv, _tv in jobs:
    for t in list(b.GetTracks()):
        if t.GetNetname().rsplit('/', 1)[-1] == name: b.RemoveNative(t)
for name, up, vp, sv, tv in jobs:
    net = b.FindNet(name) or b.FindNet('/STORAGE/' + name)
    if net is None: raise RuntimeError('missing ' + name)
    src, dst = xy(P(b, 'U11', up)), xy(P(b, 'U12', vp))
    # Pair-separated pad escapes; the via centers remain outside the pads.
    track(b, net, src, (sv[0], src[1]), F)
    track(b, net, (sv[0], src[1]), sv, F)
    via(b, net, sv)
    track(b, net, sv, tv, B)
    via(b, net, tv)
    # Enter the U12 right-edge pad from outside its right-side pad column.
    track(b, net, tv, (157.6, tv[1]), F)
    track(b, net, (157.6, tv[1]), (157.6, dst[1]), F)
    track(b, net, (157.6, dst[1]), dst, F)
for ref, pos in {'C86': (149.0, 130.0), 'C87': (149.0, 145.0)}.items():
    b.FindFootprintByReference(ref).SetPosition(V(*pos))
for name, u11pad, cap, u12pad, sv, tv in (
        ('USB_TXP1', '21', 'C86.1', None, (143, 130), None),
        ('USB_TXN1', '22', 'C87.1', None, (143, 145), None)):
    net = b.FindNet(name) or b.FindNet('/STORAGE/' + name)
    c = cap.split('.')
    source, target = xy(P(b, 'U11', u11pad)), xy(P(b, c[0], c[1]))
    track(b, net, source, (142.5, source[1]), F)
    track(b, net, (142.5, source[1]), sv, F)
    track(b, net, sv, target, F)
for name, cap, u12pad, points in (
        ('JMS_USB3_TXP', 'C86.2', '25', ((150, 130), (160, 130))),
        ('JMS_USB3_TXN', 'C87.2', '24', ((150, 145), (161, 145)))):
    net = b.FindNet(name) or b.FindNet('/STORAGE/' + name)
    c = cap.split('.')
    source, target = xy(P(b, c[0], c[1])), xy(P(b, 'U12', u12pad))
    track(b, net, source, points[0], F)
    track(b, net, points[0], points[1], F)
    track(b, net, points[1], (points[1][0], target[1]), F)
    track(b, net, (points[1][0], target[1]), target, F)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
