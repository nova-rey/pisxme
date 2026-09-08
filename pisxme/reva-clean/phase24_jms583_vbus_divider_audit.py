"""Native VBUS divider endpoint audit and negative control."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
PCB=R/'PHASE24_JMS583_VBUS_DIVIDER_PROBE.kicad_pcb';NEG=R/'PHASE24_JMS583_VBUS_DIVIDER_NEGATIVE.kicad_pcb'
def connected(b,a,z):
    b.BuildConnectivity();return z in b.GetConnectivity().GetConnectedItems(a)
b=pcbnew.LoadBoard(str(PCB));u=b.FindFootprintByReference('U11');r82=b.FindFootprintByReference('R82');r83=b.FindFootprintByReference('R83')
checks=[(u.FindPadByNumber('16'),r82.FindPadByNumber('1')),(r82.FindPadByNumber('2'),r83.FindPadByNumber('1'))]
if not all(connected(b,a,z) for a,z in checks): raise SystemExit('FAIL VBUS divider native connectivity')
codes={b.FindNet('VBUS').GetNetCode(),b.FindNet('JMS_VBUS_SENSE').GetNetCode()}
for item in list(b.GetTracks()):
    if item.GetNetCode() in codes: b.RemoveNative(item)
if any(connected(b,a,z) for a,z in checks): raise SystemExit('FAIL VBUS divider trace-removal negative control')
b.Save(str(NEG));print('PASS VBUS divider native connectivity; PASS trace-removal negative control')
