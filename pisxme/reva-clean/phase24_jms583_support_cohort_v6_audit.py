"""Native audit for the six-net JMS583 support-field cohort."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;PCB=R/'PHASE24_JMS583_SUPPORT_COHORT_PROBE.kicad_pcb';NEG=R/'PHASE24_JMS583_SUPPORT_COHORT_V6_NEGATIVE.kicad_pcb'
def ok(b,a,z):b.BuildConnectivity();return z in b.GetConnectivity().GetConnectedItems(a)
b=pcbnew.LoadBoard(str(PCB));u=b.FindFootprintByReference('U11')
pairs=[('JMS_RESET_N','15','R81','1'),('JMS_AVDD33','19','C80','1'),('JMS_VCCO','6','C81','1'),('JMS_VCCK','2','C82','1'),('JMS_VDDREG_5V','1','L10','2'),('LXO','64','L10','1')]
checks=[(u.FindPadByNumber(a),b.FindFootprintByReference(r).FindPadByNumber(p)) for _,a,r,p in pairs]
if not all(ok(b,a,z) for a,z in checks):raise SystemExit('FAIL six-net support cohort connectivity')
codes={b.FindNet(n).GetNetCode() for n,_,_,_ in pairs}
for item in list(b.GetTracks()):
    if item.GetNetCode() in codes:b.RemoveNative(item)
if any(ok(b,a,z) for a,z in checks):raise SystemExit('FAIL six-net support cohort negative control')
b.Save(str(NEG));print('PASS six-net support cohort connectivity; PASS trace-removal negative control')
