"""Disposable U5 physical power-field stitch experiment.

This adds only same-net F.Cu copper between exposed U5 power pads.  It is
deliberately not a schematic or topology change: the experiment tests whether
the saved PCB's existing U5 pad field can be made physically connected while
preserving the declared layer contract.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"
OUT = ROOT / "PHASE24_U5_INPUT_POWER_STITCH.kicad_pcb"


def point(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


board = pcbnew.LoadBoard(str(BASE))
fc = pcbnew.F_Cu


def net(name):
    item = board.FindNet(name)
    if item is None:
        raise RuntimeError(f"missing net: {name}")
    return item


def stitch(name, segments):
    n = net(name)
    for (x1, y1), (x2, y2) in segments:
        track = pcbnew.PCB_TRACK(board)
        track.SetLayer(fc)
        track.SetNet(n)
        track.SetWidth(pcbnew.FromMM(0.20))
        track.SetStart(point(x1, y1))
        track.SetEnd(point(x2, y2))
        board.Add(track)


# U5 exposed 12V_PROTECTED field: pad 1 -> pad 16 -> pad 14.  Pad 15 is
# explicitly NC, so the final leg doglegs outside the package before entering
# pad 14 rather than passing through its solder-mask aperture.
stitch("12V_PROTECTED", [
    ((232.75, 103.00), (237.25, 103.00)),
    ((237.25, 103.00), (236.20, 103.00)),
    ((236.20, 103.00), (236.20, 104.25)),
    ((236.20, 104.25), (237.25, 104.25)),
])

# U5 exposed POWER_GND field: the central thermal row and the two side pads.
stitch("POWER_GND", [
    ((235.00, 103.875), (235.00, 106.125)),
    ((232.75, 105.75), (235.00, 105.75)),
    ((235.00, 105.75), (237.25, 105.75)),
])

pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
