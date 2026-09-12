"""Create the disposable full-board F.Cu POWER_GND plane probe.

This is an experiment only. It never edits the retained input board.
"""
from pathlib import Path
import pcbnew

root = Path(__file__).resolve().parent
base = root / "PHASE24_JMS583_FINE_QFN_ESCAPE.kicad_pcb"
out = root / "PHASE24_FCU_POWER_GND_PLANE_PROBE.kicad_pcb"
board = pcbnew.LoadBoard(str(base))
net = board.FindNet("POWER_GND")
if net is None:
    raise SystemExit("POWER_GND net not found")
zone = pcbnew.ZONE(board)
zone.SetLayer(pcbnew.F_Cu)
zone.SetNet(net)
zone.SetNetCode(net.GetNetCode())
zone.SetMinThickness(pcbnew.FromMM(0.20))
zone.SetLocalClearance(pcbnew.FromMM(0.20))
zone.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL)
zone.SetZoneName("REV_A_TOP_POWER_GND_RETURN_FULL")
poly = pcbnew.VECTOR_VECTOR2I()
for x, y in ((1, 1), (299, 1), (299, 179), (1, 179)):
    poly.append(pcbnew.VECTOR2I_MM(x, y))
zone.AddPolygon(poly)
board.Add(zone)
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
pcbnew.SaveBoard(str(out), board)
print(out)
