"""V128: translate the saved isolated U11/U12 support island onto V127."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb'
ORACLE = R / 'PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED.kicad_pcb'
OUT = R / 'PHASE24_STORAGE_USB3_SUPPORT_TRANSLATED_V128.kicad_pcb'
SUPPORT = {'USB_TXP1', 'USB_TXN1', 'JMS_USB3_TXP', 'JMS_USB3_TXN',
           'USB_RXP1', 'USB_RXN1'}
DX, DY = -10.0, -15.0


def mm(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


b = pcbnew.LoadBoard(str(BASE))
o = pcbnew.LoadBoard(str(ORACLE))
for ref, pos in {'C86': (180.0, 150.0), 'C87': (180.0, 155.0)}.items():
    f = b.FindFootprintByReference(ref)
    if f is None: raise RuntimeError('missing ' + ref)
    f.SetPosition(V(*pos))

for item in list(b.GetTracks()):
    if item.GetNetname().rsplit('/', 1)[-1] in SUPPORT:
        b.RemoveNative(item)

for item in o.GetTracks():
    leaf = item.GetNetname().rsplit('/', 1)[-1]
    if leaf not in SUPPORT:
        continue
    net = b.FindNet(leaf) or b.FindNet('/STORAGE/' + leaf)
    if net is None: raise RuntimeError('missing target net ' + leaf)
    if isinstance(item, pcbnew.PCB_VIA):
        q = pcbnew.PCB_VIA(b)
        x, y = mm(item.GetPosition())
        q.SetPosition(V(x + DX, y + DY))
        q.SetWidth(item.GetWidth()); q.SetDrill(item.GetDrill())
        q.SetLayerPair(item.TopLayer(), item.BottomLayer())
        q.SetNet(net); b.Add(q)
    else:
        q = pcbnew.PCB_TRACK(b)
        x1, y1 = mm(item.GetStart()); x2, y2 = mm(item.GetEnd())
        q.SetStart(V(x1 + DX, y1 + DY)); q.SetEnd(V(x2 + DX, y2 + DY))
        q.SetLayer(item.GetLayer()); q.SetWidth(item.GetWidth())
        q.SetNet(net); b.Add(q)

b.BuildListOfNets(); b.BuildConnectivity()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT)); print(OUT)
