"""Native VBUS divider endpoint audit and negative control."""
from pathlib import Path
import os,pcbnew
R=Path(__file__).resolve().parent
PCB=Path(os.environ.get('PISXME_VBUS_AUDIT_PCB',R/'PHASE24_JMS583_VBUS_DIVIDER_PROBE.kicad_pcb'));NEG=Path(os.environ.get('PISXME_VBUS_AUDIT_NEG',R/'PHASE24_JMS583_VBUS_DIVIDER_NEGATIVE.kicad_pcb'))
def connected(b,a,z):
    b.BuildConnectivity();ca=b.GetConnectivity().GetConnectedItems(a);cz=b.GetConnectivity().GetConnectedItems(z)
    return z in ca or any(x in cz for x in ca if isinstance(x,pcbnew.ZONE))
b=pcbnew.LoadBoard(str(PCB));u=b.FindFootprintByReference('U11');r82=b.FindFootprintByReference('R82');r83=b.FindFootprintByReference('R83')
checks=[
 (u.FindPadByNumber('16'),r82.FindPadByNumber('1')),
 (u.FindPadByNumber('10'),r82.FindPadByNumber('2')),
 (r82.FindPadByNumber('2'),r83.FindPadByNumber('1')),
]
if not all(connected(b,a,z) for a,z in checks):
    print('DEBUG', [connected(b,a,z) for a,z in checks])
    raise SystemExit('FAIL VBUS divider native connectivity')
codes={b.FindNet('VBUS').GetNetCode(),b.FindNet('JMS_VBUS_SENSE').GetNetCode()}
for item in list(b.GetTracks()):
    if item.GetNetCode() in codes: b.RemoveNative(item)
for zone in list(b.Zones()):
    if zone.GetNetCode() in codes: b.RemoveNative(zone)
if any(connected(b,a,z) for a,z in checks): raise SystemExit('FAIL VBUS divider trace-removal negative control')
b.Save(str(NEG));print('PASS VBUS divider native connectivity; PASS trace-removal negative control')
