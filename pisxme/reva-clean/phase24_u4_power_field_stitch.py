"""Disposable obstacle-aware U4 exposed-pad field stitch."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"
OUT = ROOT / "PHASE24_U4_POWER_FIELD_STITCH.kicad_pcb"
board = pcbnew.LoadBoard(str(BASE))


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def add(net_name, a, b):
    n = board.FindNet(net_name)
    if n is None:
        raise RuntimeError(net_name)
    t = pcbnew.PCB_TRACK(board)
    t.SetLayer(pcbnew.F_Cu)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(0.20))
    t.SetStart(p(*a))
    t.SetEnd(p(*b))
    board.Add(t)


ox, oy = 225.0, 105.0
# Approach pad 14 from the left at y=104.25; the x=223.5 dogleg stays clear
# of the existing PG_BRIDGE_3V3 segment near x=226..227.25,y=104.75.
add("12V_PROTECTED", (ox - 2.25, oy - 2.0), (ox + 2.25, oy - 2.0))
add("12V_PROTECTED", (ox + 2.25, oy - 2.0), (ox - 1.5, oy - 2.0))
add("12V_PROTECTED", (ox - 1.5, oy - 2.0), (ox - 1.5, oy - 0.75))
add("12V_PROTECTED", (ox - 1.5, oy - 0.75), (ox + 2.25, oy - 0.75))
add("POWER_GND", (ox, oy - 1.125), (ox, oy + 1.125))
add("POWER_GND", (ox - 2.25, oy + 0.75), (ox, oy + 0.75))
add("POWER_GND", (ox, oy + 0.75), (ox + 2.25, oy + 0.75))

pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
