"""Disposable TI-U7 USB3 escape with a monotonic, separated target field."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
IN = R / "PHASE24_USB3_LOCAL_TI_MINIMAL.kicad_pcb"
OUT = R / "PHASE24_USB3_LOCAL_TI_RX_SPLIT_V2.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.15)
LANES = (("CM5_USB3_RX_N", "128", "42"), ("CM5_USB3_RX_P", "130", "43"),
         ("CM5_USB3_TX_N", "140", "45"), ("CM5_USB3_TX_P", "142", "46"))

def V(p): return pcbnew.VECTOR2I_MM(*p)
def pos(p):
    q = p.GetPosition()
    return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)
def net(board, name):
    for candidate in (name, "/CORE_CM5/" + name, "/STORAGE/" + name):
        found = board.FindNet(candidate)
        if found: return found
    raise RuntimeError(name)
def track(board, n, a, z, layer):
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(V(a)); item.SetEnd(V(z)); item.SetLayer(layer)
    item.SetWidth(W); item.SetNet(n); board.Add(item)
def via(board, n, p):
    item = pcbnew.PCB_VIA(board)
    item.SetPosition(V(p)); item.SetWidth(pcbnew.FromMM(.5))
    item.SetDrill(pcbnew.FromMM(.3)); item.SetLayerPair(F, B)
    item.SetNet(n); board.Add(item)
def path(board, n, points, layer):
    for a, z in zip(points, points[1:]): track(board, n, a, z, layer)

board = pcbnew.LoadBoard(str(IN))
j7, u7 = board.FindFootprintByReference("J7"), board.FindFootprintByReference("U7")
terms = [(name, pos(j7.FindPadByNumber(jp)), pos(u7.FindPadByNumber(up)), net(board, name))
         for name, jp, up in LANES]
source_transitions = ((74.0, 102.2), (76.0, 105.2), (78.0, 108.2), (80.0, 111.2))
target_transitions = ((80.0, 105.6), (80.0, 106.5), (80.0, 107.4), (80.0, 108.3))
for i, (_, source, destination, n) in enumerate(terms):
    sv, tv = source_transitions[i], target_transitions[i]
    path(board, n, [source, sv], B)
    via(board, n, sv)
    path(board, n, [sv, tv], B)
    via(board, n, tv)
    # Align the TX dogbones to the native U7 pad rows before the final
    # approach; a direct diagonal grazes the adjacent ground/support pads.
    if i >= 2:
        aligned = (83.0, destination[1])
        path(board, n, [tv, aligned, destination], F)
    else:
        path(board, n, [tv, destination], F)
board.BuildListOfNets()
board.Save(str(OUT))
print(OUT)
