"""Promote the validated USB3 fixture copper into a disposable macro copy.

Only U7's orientation and the four CM5-to-U7 USB3 nets are changed.  Fixture
tracks are snapshotted as scalar native geometry before the target board is
loaded, avoiding KiCad 10 SWIG cross-board proxy invalidation.
"""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = Path(os.environ.get("P24_PROMOTE_BASE", str(R / "PHASE24_MACRO_FRESH_STORAGE_LOCAL_J3_EDGE.kicad_pcb")))
FIX = Path(os.environ.get("P24_PROMOTE_FIXTURE", str(R / "PHASE24_USB3_CM5IO_SOURCE_ESCAPE_U7_ROT0_CLEANPASS.kicad_pcb")))
OUT = Path(os.environ.get("P24_PROMOTE_OUT", str(R / "PHASE24_STORAGE_LOCAL_J3_EDGE_USB3_CLEANPASS.kicad_pcb")))
USB3 = (
    "CM5_USB3_RX_N", "CM5_USB3_RX_P", "CM5_USB3_TX_N", "CM5_USB3_TX_P",
    "USB_TXP1", "USB_TXN1", "JMS_USB3_TXP", "JMS_USB3_TXN",
    "USB_RXP1", "USB_RXN1",
)

def vec(p): return pcbnew.VECTOR2I(p.x, p.y)

fixture = pcbnew.LoadBoard(str(FIX))
if fixture is None: raise RuntimeError("fixture load failed")
fix_u7 = fixture.FindFootprintByReference("U7")
fix_u7_pos = vec(fix_u7.GetPosition())
fix_u7_rot = fix_u7.GetOrientationDegrees()
snapshots = []
for item in list(fixture.GetTracks()):
    if not any(n in item.GetNetname() for n in USB3): continue
    # Preserve the saved fixture net name; target resolution below handles
    # either the child hierarchy spelling or the canonical root spelling.
    name = item.GetNetname()
    if isinstance(item, pcbnew.PCB_VIA):
        snapshots.append(("via", name, vec(item.GetPosition()), item.GetWidth(item.TopLayer()), item.GetDrill(), item.TopLayer(), item.BottomLayer()))
    else:
        snapshots.append(("track", name, vec(item.GetStart()), vec(item.GetEnd()), item.GetLayer(), item.GetWidth()))

board = pcbnew.LoadBoard(str(BASE))
if board is None: raise RuntimeError("target load failed")
u7 = board.FindFootprintByReference("U7")
u7.SetPosition(fix_u7_pos)
u7.SetOrientationDegrees(fix_u7_rot)
target_nets = {str(key): value for key, value in board.GetNetInfo().NetsByName().items()}
for item in list(board.GetTracks()):
    if any(n in item.GetNetname() for n in USB3): board.Remove(item)

target_net_codes = {}
target_net_objects = {}
for rec in snapshots:
    name = rec[1]
    target = target_nets.get(name)
    if target is None and name.startswith('/CORE_CM5/'):
        target = target_nets.get(name.removeprefix('/CORE_CM5/'))
    if target is None and not name.startswith('/'):
        target = target_nets.get('/CORE_CM5/' + name)
    if target is None:
        raise RuntimeError(f"missing target net {name}")
    target_net_codes[name] = target.GetNetCode()
    target_net_objects[name] = target

for rec in snapshots:
    name = rec[1]
    net_code = target_net_codes[name]
    if rec[0] == "via":
        _, _, pos, width, drill, top, bottom = rec
        q = pcbnew.PCB_VIA(board); q.SetPosition(pos); q.SetWidth(width); q.SetDrill(drill); q.SetLayerPair(top, bottom)
    else:
        _, _, start, end, layer, width = rec
        q = pcbnew.PCB_TRACK(board); q.SetStart(start); q.SetEnd(end); q.SetLayer(layer); q.SetWidth(width)
    q.SetNet(target_net_objects[name]); q.SetNetCode(net_code); board.Add(q)

board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
