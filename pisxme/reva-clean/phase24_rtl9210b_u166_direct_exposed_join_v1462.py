"""V1462: test the native package-edge U1.66-to-exposed-pad GND join.

This is a disposable, read-only-of-the-parent experiment.  It uses actual
loaded pad coordinates and a native PCB_TRACK; it does not synthesize graph
connectivity or alter the accepted parent.
"""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_U166_DIRECT_EXPOSED_JOIN_V1462.kicad_pcb"
F_CU = pcbnew.F_Cu
W = pcbnew.FromMM(0.20)

board = pcbnew.LoadBoard(str(BASE))
gnd = board.FindNet("GND")
assert gnd is not None

# Native-loaded facts: U1.66 is at (94.05,72.40), and the bottom edge of the
# 4.8 mm exposed pad U1.69 is y=72.40 with its left edge at x=95.60.
track = pcbnew.PCB_TRACK(board)
track.SetStart(pcbnew.VECTOR2I_MM(94.05, 72.40))
track.SetEnd(pcbnew.VECTOR2I_MM(95.60, 72.40))
track.SetLayer(F_CU)
track.SetWidth(W)
track.SetNet(gnd)
track.SetNetCode(gnd.GetNetCode())
board.Add(track)

board.BuildListOfNets()
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
