"""Promote the best native TI-U7 USB3 control into the selected macro review.

This is a disposable integration experiment.  Track and via geometry is
copied as scalar native data; endpoint connectivity remains whatever the
saved PCB objects and native KiCad DRC establish.
"""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = Path(os.environ.get("P24_TI_PROMOTE_BASE", str(R / "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_REVIEW.kicad_pcb")))
FIX = Path(os.environ.get("P24_TI_PROMOTE_FIXTURE", str(R / "PHASE24_TI_USB3_MIXED_PAIR_ESCAPE.kicad_pcb")))
OUT = Path(os.environ.get("P24_TI_PROMOTE_OUT", str(R / "PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_MIXED_REVIEW.kicad_pcb")))
USB3 = ("CM5_USB3_RX_N", "CM5_USB3_RX_P", "CM5_USB3_TX_N", "CM5_USB3_TX_P")

def native_name(board, short):
    names = [str(name) for name in board.GetNetsByName() if str(name) == short or str(name).endswith("/" + short)]
    if len(names) != 1:
        raise RuntimeError(f"expected one target net for {short}, got {names}")
    return board.GetNetsByName()[names[0]]

fixture = pcbnew.LoadBoard(str(FIX))
board = pcbnew.LoadBoard(str(BASE))
if fixture is None or board is None:
    raise RuntimeError("unable to load fixture or target")

for item in list(board.GetTracks()):
    if any(item.GetNetname().endswith("/" + n) or item.GetNetname() == n for n in USB3):
        board.Remove(item)

records = []
for item in fixture.GetTracks():
    short = next((n for n in USB3 if item.GetNetname() == n or item.GetNetname().endswith("/" + n)), None)
    if short is None:
        continue
    if isinstance(item, pcbnew.PCB_VIA):
        records.append(("via", short, pcbnew.VECTOR2I(item.GetPosition()),
                        item.GetWidth(item.TopLayer()), item.GetDrill(),
                        item.TopLayer(), item.BottomLayer()))
    else:
        records.append(("track", short, pcbnew.VECTOR2I(item.GetStart()),
                        pcbnew.VECTOR2I(item.GetEnd()), item.GetLayer(), item.GetWidth()))

for record in records:
    short = record[1]
    net = native_name(board, short)
    if record[0] == "via":
        _, _, pos, width, drill, top, bottom = record
        item = pcbnew.PCB_VIA(board)
        item.SetPosition(pos)
        item.SetWidth(width)
        item.SetDrill(drill)
        item.SetLayerPair(top, bottom)
    else:
        _, _, start, end, layer, width = record
        item = pcbnew.PCB_TRACK(board)
        item.SetStart(start)
        item.SetEnd(end)
        item.SetLayer(layer)
        item.SetWidth(width)
    item.SetNetCode(net.GetNetCode())
    board.Add(item)

board.BuildListOfNets()
board.Save(str(OUT))
print(f"promoted {len(records)} native USB3 track/via objects into {OUT}")
