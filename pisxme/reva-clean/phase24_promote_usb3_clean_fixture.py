"""Promote the validated USB3 fixture copper into a disposable macro copy.

Only U7's orientation and the four CM5-to-U7 USB3 nets are changed.  Fixture
tracks are snapshotted as scalar native geometry before the target board is
loaded, avoiding KiCad 10 SWIG cross-board proxy invalidation.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_MACRO_FRESH_STORAGE_LOCAL_J3_EDGE.kicad_pcb"
FIX = R / "PHASE24_USB3_CM5IO_SOURCE_ESCAPE_U7_ROT0_CLEANPASS.kicad_pcb"
OUT = R / "PHASE24_STORAGE_LOCAL_J3_EDGE_USB3_CLEANPASS.kicad_pcb"
USB3 = ("CM5_USB3_RX_N", "CM5_USB3_RX_P", "CM5_USB3_TX_N", "CM5_USB3_TX_P")

def vec(p): return pcbnew.VECTOR2I(p.x, p.y)

fixture = pcbnew.LoadBoard(str(FIX))
if fixture is None: raise RuntimeError("fixture load failed")
snapshots = []
for item in list(fixture.GetTracks()):
    if not any(n in item.GetNetname() for n in USB3): continue
    name = item.GetNetname()
    if isinstance(item, pcbnew.PCB_VIA):
        snapshots.append(("via", name, vec(item.GetPosition()), item.GetWidth(item.TopLayer()), item.GetDrill(), item.TopLayer(), item.BottomLayer()))
    else:
        snapshots.append(("track", name, vec(item.GetStart()), vec(item.GetEnd()), item.GetLayer(), item.GetWidth()))

board = pcbnew.LoadBoard(str(BASE))
if board is None: raise RuntimeError("target load failed")
u7 = board.FindFootprintByReference("U7")
u7.SetOrientationDegrees(0)
for item in list(board.GetTracks()):
    if any(n in item.GetNetname() for n in USB3): board.Remove(item)

for rec in snapshots:
    name = rec[1]
    net = board.FindNet(name)
    if net is None: raise RuntimeError(f"missing target net {name}")
    if rec[0] == "via":
        _, _, pos, width, drill, top, bottom = rec
        q = pcbnew.PCB_VIA(board); q.SetPosition(pos); q.SetWidth(width); q.SetDrill(drill); q.SetLayerPair(top, bottom)
    else:
        _, _, start, end, layer, width = rec
        q = pcbnew.PCB_TRACK(board); q.SetStart(start); q.SetEnd(end); q.SetLayer(layer); q.SetWidth(width)
    q.SetNetCode(net.GetNetCode()); board.Add(q)

board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
