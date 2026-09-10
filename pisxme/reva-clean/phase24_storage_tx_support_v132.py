"""V132: selective TX support-leg transplant with a PERST corridor duck."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb'
ORACLE = R / 'PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED.kicad_pcb'
OUT = R / 'PHASE24_STORAGE_TX_SUPPORT_SELECTIVE_V132.kicad_pcb'
DX, DY = -10.0, -15.0
F, B = pcbnew.F_Cu, pcbnew.B_Cu
KEEP = {'USB_TXP1', 'USB_TXN1', 'JMS_USB3_TXP', 'JMS_USB3_TXN'}


def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def mm(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def leaf(n): return n.rsplit('/', 1)[-1]


def segment(b, n, a, z, layer, width):
    if a == z: return
    q = pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z))
    q.SetLayer(layer); q.SetWidth(width); q.SetNet(n); b.Add(q)


b = pcbnew.LoadBoard(str(BASE)); o = pcbnew.LoadBoard(str(ORACLE))
for ref, pos in {'C86': (180, 150), 'C87': (180, 155)}.items():
    f = b.FindFootprintByReference(ref)
    if f is None: raise RuntimeError('missing ' + ref)
    f.SetPosition(V(*pos))
for t in list(b.GetTracks()):
    if leaf(t.GetNetname()) in KEEP: b.RemoveNative(t)

# Move only the local support geometries from the known support fixture.  The
# source fixture was authored at U11=(150,150), U12=(165,150); V127 is
# U11=(140,135), U12=(155,135), hence the fixed translation.
for t in o.GetTracks():
    if leaf(t.GetNetname()) not in KEEP: continue
    n = b.FindNet(leaf(t.GetNetname())) or b.FindNet('/STORAGE/' + leaf(t.GetNetname()))
    if n is None: raise RuntimeError('missing ' + leaf(t.GetNetname()))
    if isinstance(t, pcbnew.PCB_VIA):
        q = pcbnew.PCB_VIA(b); x, y = mm(t.GetPosition())
        q.SetPosition(V(x + DX, y + DY)); q.SetWidth(t.GetWidth(t.TopLayer()))
        q.SetDrill(t.GetDrill()); q.SetLayerPair(t.TopLayer(), t.BottomLayer())
        q.SetNet(n); b.Add(q)
    else:
        q = pcbnew.PCB_TRACK(b); x1, y1 = mm(t.GetStart()); x2, y2 = mm(t.GetEnd())
        q.SetStart(V(x1 + DX, y1 + DY)); q.SetEnd(V(x2 + DX, y2 + DY))
        q.SetLayer(t.GetLayer()); q.SetWidth(t.GetWidth()); q.SetNet(n); b.Add(q)

# Move PERST's y=150 horizontal trunk to B.Cu, preserving its endpoints and
# leaving the validated PCIe/CM5 architecture otherwise unchanged.
for t in list(b.GetTracks()):
    if leaf(t.GetNetname()) != 'CM5_PERST' or t.GetLayer() != F: continue
    a, z = mm(t.GetStart()), mm(t.GetEnd())
    if {round(a[0], 2), round(z[0], 2)} == {64.0, 152.54} and abs(a[1] - 150) < .02 and abs(z[1] - 150) < .02:
        b.RemoveNative(t); n = b.FindNet('/CORE_CM5/CM5_PERST') or b.FindNet('CM5_PERST')
        segment(b, n, (64, 150), (64, 147), F, t.GetWidth())
        v1 = pcbnew.PCB_VIA(b); v1.SetPosition(V(64, 147)); v1.SetWidth(pcbnew.FromMM(.50)); v1.SetDrill(pcbnew.FromMM(.30)); v1.SetLayerPair(F, B); v1.SetNet(n); b.Add(v1)
        segment(b, n, (64, 147), (152.54, 147), B, t.GetWidth())
        v2 = pcbnew.PCB_VIA(b); v2.SetPosition(V(152.54, 147)); v2.SetWidth(pcbnew.FromMM(.50)); v2.SetDrill(pcbnew.FromMM(.30)); v2.SetLayerPair(F, B); v2.SetNet(n); b.Add(v2)
        segment(b, n, (152.54, 147), (152.54, 150), F, t.GetWidth())
        break

b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.BuildConnectivity()
b.Save(str(OUT)); print(OUT)
