"""Native connectivity and saved-board negative controls for V1466."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
PCB = H / "PHASE24_RTL9210B_U166_JOIN_RXP_EAST_UP_V1466.kicad_pcb"

def pad(board, ref, number):
    fp = board.FindFootprintByReference(ref)
    assert fp is not None, ref
    result = fp.FindPadByNumber(number)
    assert result is not None, (ref, number)
    return result

def connected(board, a, z):
    board.BuildConnectivity()
    return pad(board, *z) in board.GetConnectivity().GetConnectedItems(pad(board, *a))

board = pcbnew.LoadBoard(str(PCB))
assert connected(board, ("U1", "66"), ("U1", "69")), "U1.66 GND exposed-pad join"
assert connected(board, ("U1", "64"), ("J1", "43")), "U1.64 RXP to J1.43"
for source, target in (("65", "41"), ("67", "47"), ("68", "49")):
    assert connected(board, ("U1", source), ("J1", target)), f"U1.{source} to J1.{target}"

# Remove the saved direct GND edge join.  The audit must fail because its
# edges come only from KiCad's native loaded pads/tracks/vias/zones.
negative_gnd = pcbnew.LoadBoard(str(PCB))
victim = next(item for item in negative_gnd.GetTracks()
               if item.GetNetname() == "GND"
               and hasattr(item, "GetStart")
               and tuple(round(float(v) / 1e6, 3) for v in item.GetStart()) == (94.05, 72.4)
               and tuple(round(float(v) / 1e6, 3) for v in item.GetEnd()) == (95.6, 72.4))
negative_gnd.RemoveNative(victim)
assert not connected(negative_gnd, ("U1", "66"), ("U1", "69"))
negative_gnd.Save(str(H / "PHASE24_RTL9210B_U166_JOIN_RXP_EAST_UP_V1466-negative-gnd.kicad_pcb"))

# Remove the saved RXP source segment.  This must break U1.64-to-J1.43 while
# leaving the rest of the board untouched.
negative_rxp = pcbnew.LoadBoard(str(PCB))
victim = next(item for item in negative_rxp.GetTracks()
              if item.GetNetname() == "LANE0_RXP"
              and hasattr(item, "GetStart")
              and tuple(round(float(v) / 1e6, 3) for v in item.GetStart()) == (94.05, 71.6)
              and tuple(round(float(v) / 1e6, 3) for v in item.GetEnd()) == (95.0, 71.6))
negative_rxp.RemoveNative(victim)
assert not connected(negative_rxp, ("U1", "64"), ("J1", "43"))
negative_rxp.Save(str(H / "PHASE24_RTL9210B_U166_JOIN_RXP_EAST_UP_V1466-negative-rxp.kicad_pcb"))

print("PASS V1466 native U1.66-to-U1.69 GND and U1.64-to-J1.43 RXP")
print("PASS V1466 saved-board GND and RXP trace-removal negative controls")
