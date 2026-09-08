"""Native VDDREG endpoint audit and trace-removal negative control."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;PCB=R/'PHASE24_JMS583_VDDREG_PROBE.kicad_pcb';NEG=R/'PHASE24_JMS583_VDDREG_NEGATIVE.kicad_pcb'
def connected(b):
    b.BuildConnectivity();c=b.GetConnectivity();return b.FindFootprintByReference('L10').FindPadByNumber('2') in c.GetConnectedItems(b.FindFootprintByReference('U11').FindPadByNumber('1'))
b=pcbnew.LoadBoard(str(PCB))
if not connected(b):raise SystemExit('FAIL VDDREG native connectivity')
n=b.FindNet('JMS_VDDREG_5V')
for item in list(b.GetTracks()):
    if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
if connected(b):raise SystemExit('FAIL VDDREG trace-removal negative control')
b.Save(str(NEG));print('PASS VDDREG native connectivity; PASS trace-removal negative control')
