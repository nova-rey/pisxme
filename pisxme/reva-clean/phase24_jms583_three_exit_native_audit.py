"""Native saved-object audit for the transplanted XIN/XOUT/XAVDDH exits."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
PCB=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_THREE_EXITS.kicad_pcb'
NEG=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_THREE_EXITS_NEGATIVE.kicad_pcb'
PAIRS=(('U11','50','Y10','1'),('U11','51','Y10','2'),('U11','52','C84','1'))
def connected(b,a,ap,z,zp):
    b.BuildConnectivity(); c=b.GetConnectivity()
    return b.FindFootprintByReference(z).FindPadByNumber(zp) in c.GetConnectedItems(b.FindFootprintByReference(a).FindPadByNumber(ap))
b=pcbnew.LoadBoard(str(PCB))
if not all(connected(b,*x) for x in PAIRS): raise SystemExit('FAIL three-exit connectivity')
for item in list(b.GetTracks()):
    if item.GetNetname()=='XIN': b.RemoveNative(item)
if all(connected(b,*x) for x in PAIRS): raise SystemExit('FAIL XIN negative control')
b.Save(str(NEG));print('PASS XIN/XOUT/XAVDDH native connectivity; PASS XIN removal negative control')
