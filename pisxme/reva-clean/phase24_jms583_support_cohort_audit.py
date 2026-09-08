"""Native audit for the four-net JMS583 support cohort."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;PCB=R/'PHASE24_JMS583_SUPPORT_COHORT_PROBE.kicad_pcb';NEG=R/'PHASE24_JMS583_SUPPORT_COHORT_NEGATIVE.kicad_pcb'
def ok(b,a,z):
    b.BuildConnectivity();return z in b.GetConnectivity().GetConnectedItems(a)
b=pcbnew.LoadBoard(str(PCB));u=b.FindFootprintByReference('U11')
pairs=[('15','R81','1'),('19','C80','1'),('6','C81','1'),('2','C82','1')]
checks=[(u.FindPadByNumber(a),b.FindFootprintByReference(r).FindPadByNumber(p)) for a,r,p in pairs]
if not all(ok(b,a,z) for a,z in checks):raise SystemExit('FAIL support cohort native connectivity')
codes={b.FindNet(x).GetNetCode() for x in ('JMS_RESET_N','JMS_AVDD33','JMS_VCCO','JMS_VCCK')}
for item in list(b.GetTracks()):
    if item.GetNetCode() in codes:b.RemoveNative(item)
if any(ok(b,a,z) for a,z in checks):raise SystemExit('FAIL support cohort trace-removal negative control')
b.Save(str(NEG));print('PASS four-net support cohort connectivity; PASS trace-removal negative control')
