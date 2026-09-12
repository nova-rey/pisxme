"""Disposablely graft the validated U12/U11 USB3 support field into M-key board.

Only native saved track/via geometry is copied. J7 source links remain separate
and are audited independently; no connectivity edges are synthesized.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_STORAGE_MKEY_USB3_ACTUAL_PAD_PROBE_20260912.kicad_pcb"
FIX = ROOT / "PHASE24_STORAGE_SUPPORT_U12_COAUTHOR_TX_RX_FAR_V150.kicad_pcb"
OUT = ROOT / "PHASE24_STORAGE_MKEY_USB3_SUPPORT_V150_GRAFT_20260912.kicad_pcb"
NETS = {"USB_TXP1", "USB_TXN1", "JMS_USB3_TXP", "JMS_USB3_TXN", "USB_RXP1", "USB_RXN1"}


def resolve(board, name):
    names = [str(n) for n in board.GetNetsByName()
             if str(n) == name or str(n).endswith("/" + name)]
    if len(names) != 1:
        raise RuntimeError(f"expected one net for {name}, got {names}")
    return board.GetNetsByName()[names[0]]


board = pcbnew.LoadBoard(str(BASE))
fixture = pcbnew.LoadBoard(str(FIX))
if board is None or fixture is None:
    raise SystemExit("cannot load base or fixture")

for item in list(board.GetTracks()):
    if item.GetNetname() in NETS:
        board.RemoveNative(item)

count = 0
for source in fixture.GetTracks():
    name = source.GetNetname()
    if name not in NETS:
        continue
    net = resolve(board, name)
    if isinstance(source, pcbnew.PCB_VIA):
        item = pcbnew.PCB_VIA(board)
        item.SetPosition(pcbnew.VECTOR2I(source.GetPosition()))
        item.SetWidth(source.GetWidth(source.TopLayer()))
        item.SetDrill(source.GetDrill())
        item.SetLayerPair(source.TopLayer(), source.BottomLayer())
    else:
        item = pcbnew.PCB_TRACK(board)
        item.SetStart(pcbnew.VECTOR2I(source.GetStart()))
        item.SetEnd(pcbnew.VECTOR2I(source.GetEnd()))
        item.SetLayer(source.GetLayer())
        item.SetWidth(source.GetWidth())
    item.SetNetCode(net.GetNetCode())
    board.Add(item)
    count += 1

board.BuildListOfNets()
board.Save(str(OUT))
print(f"copied {count} native support track/via objects to {OUT}")
