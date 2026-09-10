"""V133: shift TX support-cap corridors below the PERST/TP5 window."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb'
OUT = R / 'PHASE24_STORAGE_TX_SUPPORT_SHIFTED_V133.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.13208)


def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p):
    p = p.GetPosition() if hasattr(p, 'GetPosition') else p
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def pad(b, ref, n): return b.FindFootprintByReference(ref).FindPadByNumber(str(n))


def seg(b, n, a, z, layer):
    if a == z: return
    q = pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z))
    q.SetLayer(layer); q.SetWidth(W); q.SetNet(n); b.Add(q)


def via(b, n, p):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(n); b.Add(q)


b = pcbnew.LoadBoard(str(BASE))
for ref, pos in {'C86': (180, 160), 'C87': (180, 165)}.items():
    f = b.FindFootprintByReference(ref)
    if f is None: raise RuntimeError('missing ' + ref)
    f.SetPosition(V(*pos))
for name in ('USB_TXP1', 'USB_TXN1', 'JMS_USB3_TXP', 'JMS_USB3_TXN'):
    for t in list(b.GetTracks()):
        if t.GetNetname().rsplit('/', 1)[-1] == name: b.RemoveNative(t)

# U11 -> coupling capacitor, on F.Cu with separated y corridors.
for name, u11n, capref, y in (
        ('USB_TXP1', '21', 'C86.1', 160),
        ('USB_TXN1', '22', 'C87.1', 165)):
    n = b.FindNet(name) or b.FindNet('/STORAGE/' + name)
    c = capref.split('.')
    source, target = xy(pad(b, 'U11', u11n)), xy(pad(b, c[0], c[1]))
    x = source[0] + (0.8 if name == 'USB_TXP1' else 1.8)
    seg(b, n, source, (x, source[1]), F)
    seg(b, n, (x, source[1]), (x, y), F)
    seg(b, n, (x, y), target, F)

# Coupling capacitor -> U12, with ordinary through-vias and a B.Cu return
# corridor. The target vias are deliberately separated from the dense U12
# pad column and final F.Cu dogbones enter only their own right-edge rows.
for name, capref, u12n, source_via, target_via in (
        ('JMS_USB3_TXP', 'C86.2', '25', (162, 137), (182, 160)),
        ('JMS_USB3_TXN', 'C87.2', '24', (164, 137.4), (184, 165))):
    n = b.FindNet(name) or b.FindNet('/STORAGE/' + name)
    c = capref.split('.')
    source, target = xy(pad(b, c[0], c[1])), xy(pad(b, 'U12', u12n))
    seg(b, n, source, (source_via[0], source[1]), F)
    seg(b, n, (source_via[0], source[1]), source_via, F)
    via(b, n, source_via)
    seg(b, n, source_via, target_via, B)
    via(b, n, target_via)
    seg(b, n, target_via, (157.6, target_via[1]), F)
    seg(b, n, (157.6, target_via[1]), (157.6, target[1]), F)
    seg(b, n, (157.6, target[1]), target, F)

b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.BuildConnectivity(); b.Save(str(OUT)); print(OUT)
