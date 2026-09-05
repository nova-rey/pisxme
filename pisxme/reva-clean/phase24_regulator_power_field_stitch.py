"""Disposable same-net exposed-pad field repair for U3/U4/U5.

The experiment uses the repeated TPSM63606 footprint geometry already saved in
the PCB.  It adds no schematic edges and deliberately leaves each regulator's
topology unchanged.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"
OUT = ROOT / "PHASE24_REGULATOR_POWER_FIELD_STITCH_U3_U5.kicad_pcb"
board = pcbnew.LoadBoard(str(BASE))


def pt(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def add_track(name, a, b):
    n = board.FindNet(name)
    if n is None:
        raise RuntimeError(f"missing net {name}")
    t = pcbnew.PCB_TRACK(board)
    t.SetLayer(pcbnew.F_Cu)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(0.20))
    t.SetStart(pt(*a))
    t.SetEnd(pt(*b))
    board.Add(t)


for ox, oy in ((60.0, 165.0), (235.0, 105.0)):
    # pad 1 -> pad 16; pad 14 is entered from the left to avoid NC pad 15.
    add_track("12V_PROTECTED", (ox - 2.25, oy - 2.0), (ox + 2.25, oy - 2.0))
    add_track("12V_PROTECTED", (ox + 2.25, oy - 2.0), (ox + 1.20, oy - 2.0))
    add_track("12V_PROTECTED", (ox + 1.20, oy - 2.0), (ox + 1.20, oy - 0.75))
    add_track("12V_PROTECTED", (ox + 1.20, oy - 0.75), (ox + 2.25, oy - 0.75))
    # central thermal row and the two side POWER_GND pads.
    add_track("POWER_GND", (ox, oy - 1.125), (ox, oy + 1.125))
    add_track("POWER_GND", (ox - 2.25, oy + 0.75), (ox, oy + 0.75))
    add_track("POWER_GND", (ox, oy + 0.75), (ox + 2.25, oy + 0.75))

pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
