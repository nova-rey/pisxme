"""Create the disposable F.Cu-ground candidate with normal-width returns."""
from pathlib import Path
import pcbnew

root = Path(__file__).resolve().parent
base = root / "PHASE24_FCU_POWER_GND_PLANE_PROBE.kicad_pcb"
out = root / "PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb"
board = pcbnew.LoadBoard(str(base))
net = board.FindNet("POWER_GND")
changed = 0
for track in board.GetTracks():
    if (isinstance(track, pcbnew.PCB_TRACK)
            and not isinstance(track, pcbnew.PCB_VIA)
            and track.GetNetCode() == net.GetNetCode()
            and track.GetWidth() < pcbnew.FromMM(0.20)):
        track.SetWidth(pcbnew.FromMM(0.20))
        changed += 1
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
pcbnew.SaveBoard(str(out), board)
print(f"widened {changed} POWER_GND tracks")
