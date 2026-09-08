"""Native connectivity audit for the seven-net JMS583 support cohort.

Edges are derived only from KiCad's saved pads/tracks/vias/zones.  The
negative control removes the authored tracks and must fail every assertion.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
PCB = R / "PHASE24_JMS583_SUPPORT_COHORT_PROBE.kicad_pcb"
NEG = R / "PHASE24_JMS583_SUPPORT_COHORT_V7_NEGATIVE.kicad_pcb"

PAIRS = [
    ("JMS_RESET_N", "15", "R81", "1"),
    ("JMS_AVDD33", "19", "C80", "1"),
    ("JMS_AVDDL", "20", "C83", "1"),
    ("JMS_VCCO", "6", "C81", "1"),
    ("JMS_VCCK", "2", "C82", "1"),
    ("JMS_VDDREG_5V", "1", "L10", "2"),
    ("LXO", "64", "L10", "1"),
    ("JMS_XAVDDH", "52", "C84", "1"),
]


def connected(board, source, destination):
    board.BuildConnectivity()
    return destination in board.GetConnectivity().GetConnectedItems(source)


board = pcbnew.LoadBoard(str(PCB))
u11 = board.FindFootprintByReference("U11")
ep = u11.FindPadByNumber("65")
if ep is None or ep.GetNetname() != "POWER_GND":
    raise SystemExit("FAIL JMS583 exposed-pad POWER_GND authority")
checks = [
    (u11.FindPadByNumber(pin), board.FindFootprintByReference(ref).FindPadByNumber(pad))
    for _net, pin, ref, pad in PAIRS
]
r81 = board.FindFootprintByReference("R81")
c85 = board.FindFootprintByReference("C85")
checks.append((r81.FindPadByNumber("1"), c85.FindPadByNumber("1")))
if not all(connected(board, src, dst) for src, dst in checks):
    raise SystemExit("FAIL eight-net JMS583 support cohort connectivity")

codes = {board.FindNet(net).GetNetCode() for net, *_ in PAIRS}
for item in list(board.GetTracks()):
    if item.GetNetCode() in codes:
        board.RemoveNative(item)
if any(connected(board, src, dst) for src, dst in checks):
    raise SystemExit("FAIL eight-net JMS583 support cohort negative control")

board.Save(str(NEG))
print("PASS eight-net support cohort connectivity; PASS trace-removal negative control")
