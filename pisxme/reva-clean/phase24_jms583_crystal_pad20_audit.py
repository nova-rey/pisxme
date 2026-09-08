"""Native crystal endpoint audit and trace-removal negative controls."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
PCB=R/'PHASE24_JMS583_CRYSTAL_ESCAPE_PROBE.kicad_pcb'
NEG=R/'PHASE24_JMS583_CRYSTAL_PAD20_NEGATIVE.kicad_pcb'
def endpoints(b):
    b.BuildConnectivity(); c=b.GetConnectivity(); u=b.FindFootprintByReference('U11'); y=b.FindFootprintByReference('Y10')
    return (y.FindPadByNumber('1') in c.GetConnectedItems(u.FindPadByNumber('50')) and
            y.FindPadByNumber('2') in c.GetConnectedItems(u.FindPadByNumber('51')))
b=pcbnew.LoadBoard(str(PCB))
if not endpoints(b): raise SystemExit('FAIL crystal native connectivity')
codes={b.FindNet('XIN').GetNetCode(),b.FindNet('XOUT').GetNetCode()}
for item in list(b.GetTracks()):
    if item.GetNetCode() in codes: b.RemoveNative(item)
if endpoints(b): raise SystemExit('FAIL crystal trace-removal negative control')
b.Save(str(NEG))
print('PASS XIN/XOUT native connectivity; PASS trace-removal negative control')
