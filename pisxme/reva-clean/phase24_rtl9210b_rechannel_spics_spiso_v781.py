from pathlib import Path
import pcbnew

BASE = Path(__file__).with_name('PHASE24_RTL9210B_SPI_RECHANNEL_SPICS_SPISO_V780.kicad_pcb')
OUT = Path(__file__).with_name('PHASE24_RTL9210B_SPI_RECHANNEL_SPICS_SPISO_V781.kicad_pcb')

F = pcbnew.F_Cu
B = pcbnew.B_Cu

def xy(p): return pcbnew.VECTOR2I_MM(p[0], p[1])
def track(board, net, layer, a, b, width=0.15):
    t = pcbnew.PCB_TRACK(board)
    t.SetNet(net)
    t.SetLayer(layer)
    t.SetStart(xy(a)); t.SetEnd(xy(b)); t.SetWidth(pcbnew.FromMM(width))
    board.Add(t)
def via(board, net, p, diameter=0.6, drill=0.3):
    v = pcbnew.PCB_VIA(board)
    v.SetNet(net); v.SetPosition(xy(p))
    v.SetWidth(pcbnew.FromMM(diameter)); v.SetDrill(pcbnew.FromMM(drill))
    board.Add(v)

b = pcbnew.LoadBoard(str(BASE))
for name in ('SPICS', 'SPISO'):
    net = b.FindNet(name)
    for item in list(b.GetTracks()):
        if item.GetNetname() == name:
            b.RemoveNative(item)

# Source escapes remain on F.Cu; long channels use B.Cu and return above
# the crystal/decoupling support pocket.  Final F.Cu dogbones are intentionally
# short and are independently checked by native DRC.
n = b.FindNet('SPICS')
track(b, n, F, (98.8,66.05), (98.8,64.5))
track(b, n, F, (98.8,64.5), (97.0,60.5))
via(b, n, (97.0,60.5))
track(b, n, B, (97.0,60.5), (97.0,76.0))
via(b, n, (97.0,76.0))
track(b, n, F, (97.0,76.0), (103.0,76.0))
track(b, n, F, (103.0,76.0), (105.0,80.0))

n = b.FindNet('SPISO')
track(b, n, F, (99.2,66.05), (99.2,64.5))
track(b, n, F, (99.2,64.5), (99.0,60.5))
via(b, n, (99.0,60.5))
track(b, n, B, (99.0,60.5), (99.0,74.0))
via(b, n, (99.0,74.0))
track(b, n, F, (99.0,74.0), (103.0,74.0))
track(b, n, F, (103.0,74.0), (105.0,78.8))

b.Save(str(OUT))
print(OUT)
