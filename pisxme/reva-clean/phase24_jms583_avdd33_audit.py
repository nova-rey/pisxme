"""Native AVDD33 endpoint audit with a trace-removal negative control."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
PCB=R/'PHASE24_JMS583_AVDD33_PROBE.kicad_pcb'; NEG=R/'PHASE24_JMS583_AVDD33_NEGATIVE.kicad_pcb'
def connected(b):
    b.BuildConnectivity(); c=b.GetConnectivity()
    return b.FindFootprintByReference('C80').FindPadByNumber('1') in c.GetConnectedItems(b.FindFootprintByReference('U11').FindPadByNumber('19'))
b=pcbnew.LoadBoard(str(PCB))
if not connected(b): raise SystemExit('FAIL AVDD33 native connectivity')
n=b.FindNet('JMS_AVDD33')
for item in list(b.GetTracks()):
    if item.GetNetCode()==n.GetNetCode(): b.RemoveNative(item)
if connected(b): raise SystemExit('FAIL AVDD33 trace-removal negative control')
b.Save(str(NEG)); print('PASS AVDD33 native connectivity; PASS trace-removal negative control')
