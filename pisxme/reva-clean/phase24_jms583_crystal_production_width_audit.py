"""Audit the production-width JMS583 crystal escape and its negative control."""
from pathlib import Path
import pcbnew
R = Path(__file__).resolve().parent
PCB = R / "PHASE24_JMS583_CRYSTAL_PRODUCTION_WIDTH_PROBE.kicad_pcb"
NEG = R / "PHASE24_JMS583_CRYSTAL_PRODUCTION_WIDTH_NEGATIVE.kicad_pcb"
def joined(b):
    b.BuildConnectivity(); c = b.GetConnectivity()
    u = b.FindFootprintByReference("U11"); y = b.FindFootprintByReference("Y10")
    return all(y.FindPadByNumber(yp) in c.GetConnectedItems(u.FindPadByNumber(up))
               for up, yp in (("50", "1"), ("51", "2")))
b = pcbnew.LoadBoard(str(PCB))
if not joined(b): raise SystemExit("FAIL production-width XIN/XOUT connectivity")
for item in list(b.GetTracks()):
    if item.GetNetname() in ("XIN", "XOUT"): b.RemoveNative(item)
if joined(b): raise SystemExit("FAIL production-width crystal negative control")
b.Save(str(NEG)); print("PASS production-width XIN/XOUT; PASS trace-removal negative control")
