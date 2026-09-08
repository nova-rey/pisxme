"""Native LXO endpoint audit and trace-removal negative control."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;PCB=R/'PHASE24_JMS583_LXO_PROBE.kicad_pcb';NEG=R/'PHASE24_JMS583_LXO_NEGATIVE.kicad_pcb'
def connected(b):
    b.BuildConnectivity();c=b.GetConnectivity();return b.FindFootprintByReference('L10').FindPadByNumber('1') in c.GetConnectedItems(b.FindFootprintByReference('U11').FindPadByNumber('64'))
b=pcbnew.LoadBoard(str(PCB))
if not connected(b):raise SystemExit('FAIL LXO native connectivity')
n=b.FindNet('LXO')
for item in list(b.GetTracks()):
    if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
if connected(b):raise SystemExit('FAIL LXO trace-removal negative control')
b.Save(str(NEG));print('PASS LXO native connectivity; PASS trace-removal negative control')
