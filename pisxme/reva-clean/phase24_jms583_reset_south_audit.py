"""Native connectivity audit and negative control for the reset escape probe."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
PCB=R/'PHASE24_JMS583_RESET_SOUTH_PROBE.kicad_pcb'
NEG=R/'PHASE24_JMS583_RESET_SOUTH_PROBE_NEGATIVE.kicad_pcb'
def connected(b):
    b.BuildConnectivity(); c=b.GetConnectivity()
    a=b.FindFootprintByReference('U11').FindPadByNumber('15')
    z=b.FindFootprintByReference('R81').FindPadByNumber('1')
    return z in c.GetConnectedItems(a)
b=pcbnew.LoadBoard(str(PCB))
if not connected(b): raise SystemExit('FAIL reset native connectivity')
n=b.FindNet('JMS_RESET_N')
for item in list(b.GetTracks()):
    if item.GetNetCode()==n.GetNetCode(): b.RemoveNative(item)
if connected(b): raise SystemExit('FAIL reset trace-removal negative control')
b.Save(str(NEG))
print('PASS reset native connectivity; PASS trace-removal negative control')
