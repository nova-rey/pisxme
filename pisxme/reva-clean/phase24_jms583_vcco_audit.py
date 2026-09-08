"""Native VCCO endpoint audit and trace-removal negative control."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; PCB=R/'PHASE24_JMS583_VCCO_PROBE.kicad_pcb'; NEG=R/'PHASE24_JMS583_VCCO_NEGATIVE.kicad_pcb'
def connected(b):
    b.BuildConnectivity();c=b.GetConnectivity();return b.FindFootprintByReference('C81').FindPadByNumber('1') in c.GetConnectedItems(b.FindFootprintByReference('U11').FindPadByNumber('6'))
b=pcbnew.LoadBoard(str(PCB))
if not connected(b): raise SystemExit('FAIL VCCO native connectivity')
n=b.FindNet('JMS_VCCO')
for item in list(b.GetTracks()):
    if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
if connected(b): raise SystemExit('FAIL VCCO trace-removal negative control')
b.Save(str(NEG));print('PASS VCCO native connectivity; PASS trace-removal negative control')
