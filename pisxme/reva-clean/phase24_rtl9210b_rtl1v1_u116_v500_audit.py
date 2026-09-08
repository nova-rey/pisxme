"""Native connectivity audit and trace-removal negative control for V500."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
PCB = H / "PHASE24_RTL9210B_RTL1V1_U116_V500.kicad_pcb"

def connected(board, ref, pad):
    board.BuildConnectivity()
    fp = board.FindFootprintByReference(ref)
    p = fp.FindPadByNumber(pad)
    return p.GetNetname(), board.GetConnectivity().GetConnectedItems(p)

board = pcbnew.LoadBoard(str(PCB))
for ref, pad in (("U1", "16"), ("C4", "1")):
    net, items = connected(board, ref, pad)
    assert net == "RTL_1V1", (ref, pad, net)
    assert items, (ref, pad, "no native connected items")
assert connected(board, "U1", "16")[1]
print("PASS native V500 U1.16 -> C4.1 RTL_1V1")

# Negative control: remove one necessary V500 trace and require disconnection.
neg = pcbnew.LoadBoard(str(PCB))
neg.BuildConnectivity()
removed = False
for item in list(neg.GetTracks()):
    if item.GetNetname() == "RTL_1V1" and not isinstance(item, pcbnew.PCB_VIA):
        neg.Remove(item); removed = True; break
assert removed
neg.BuildConnectivity()
u1 = neg.FindFootprintByReference("U1").FindPadByNumber("16")
c4 = neg.FindFootprintByReference("C4").FindPadByNumber("1")
assert not (c4 in neg.GetConnectivity().GetConnectedItems(u1) and
            u1 in neg.GetConnectivity().GetConnectedItems(c4)), "negative control did not fail"
print("PASS V500 trace-removal negative control")
