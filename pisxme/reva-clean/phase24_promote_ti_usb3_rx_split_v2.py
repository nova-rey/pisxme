"""Apply the validated disposable TI-U7 escape geometry to the selected macro."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_REVIEW.kicad_pcb"
OUT = R / "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_USB3_RX_SPLIT_V2.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.15)
LANES = (("CM5_USB3_RX_N", "128", "42"), ("CM5_USB3_RX_P", "130", "43"),
         ("CM5_USB3_TX_N", "140", "45"), ("CM5_USB3_TX_P", "142", "46"))

def V(p): return pcbnew.VECTOR2I_MM(*p)
def pos(p):
    q = p.GetPosition()
    return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)
def path(board, n, points, layer):
    for a, z in zip(points, points[1:]):
        t = pcbnew.PCB_TRACK(board); t.SetStart(V(a)); t.SetEnd(V(z))
        t.SetLayer(layer); t.SetWidth(W); t.SetNet(n); board.Add(t)
def via(board, n, p):
    v = pcbnew.PCB_VIA(board); v.SetPosition(V(p)); v.SetWidth(pcbnew.FromMM(.5))
    v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F, B); v.SetNet(n); board.Add(v)

board = pcbnew.LoadBoard(str(BASE))
j7 = board.FindFootprintByReference("J7")
u7 = board.FindFootprintByReference("U7")
for item in list(board.GetTracks()):
    if any(name in item.GetNetname() for name, _, _ in LANES): board.Remove(item)
source_transitions = ((74.0, 102.2), (76.0, 105.2), (78.0, 108.2), (80.0, 111.2))
target_transitions = ((88.0, 124.6), (88.0, 125.5), (88.0, 126.4), (88.0, 127.3))
for i, (name, jp, up) in enumerate(LANES):
    n = board.FindNet(name) or board.FindNet("/CORE_CM5/" + name)
    if n is None: raise RuntimeError(name)
    source = pos(j7.FindPadByNumber(jp)); destination = pos(u7.FindPadByNumber(up))
    sv, tv = source_transitions[i], target_transitions[i]
    path(board, n, [source, sv], B); via(board, n, sv); path(board, n, [sv, tv], B)
    via(board, n, tv)
    if i >= 2: path(board, n, [tv, (91.0, destination[1]), destination], F)
    else: path(board, n, [tv, destination], F)
board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
