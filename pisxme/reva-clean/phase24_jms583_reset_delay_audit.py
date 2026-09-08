"""Native reset branch audit and trace-removal negative control."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;PCB=R/'PHASE24_JMS583_RESET_DELAY_PROBE.kicad_pcb';NEG=R/'PHASE24_JMS583_RESET_DELAY_NEGATIVE.kicad_pcb'
def ok(b,a,z):
    b.BuildConnectivity();return z in b.GetConnectivity().GetConnectedItems(a)
b=pcbnew.LoadBoard(str(PCB));u=b.FindFootprintByReference('U11');r=b.FindFootprintByReference('R81');c=b.FindFootprintByReference('C85')
pairs=[(u.FindPadByNumber('15'),r.FindPadByNumber('1')),(r.FindPadByNumber('1'),c.FindPadByNumber('1'))]
if not all(ok(b,a,z) for a,z in pairs):raise SystemExit('FAIL reset-delay native connectivity')
n=b.FindNet('JMS_RESET_N')
for item in list(b.GetTracks()):
    if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
if any(ok(b,a,z) for a,z in pairs):raise SystemExit('FAIL reset-delay trace-removal negative control')
b.Save(str(NEG));print('PASS reset-delay native connectivity; PASS trace-removal negative control')
