"""Native VDDREG zone connectivity and zone-removal negative control."""
from pathlib import Path
import os,pcbnew
R=Path(__file__).resolve().parent;PCB=Path(os.environ.get('PISXME_VDDREG_ZONE_PCB',R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VDDREG_local_zone.kicad_pcb'));NEG=Path(os.environ.get('PISXME_VDDREG_ZONE_NEG',R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VDDREG_local_zone-negative.kicad_pcb'))
def ok(b):
 b.BuildConnectivity();u=b.FindFootprintByReference('U11');l=b.FindFootprintByReference('L10');cu=b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('1'));cl=b.GetConnectivity().GetConnectedItems(l.FindPadByNumber('2'));return l.FindPadByNumber('2') in cu or any(a in cl for a in cu if isinstance(a,pcbnew.ZONE))
b=pcbnew.LoadBoard(str(PCB))
if not ok(b):
 b.BuildConnectivity();u=b.FindFootprintByReference('U11');l=b.FindFootprintByReference('L10')
 print('DEBUG',len(b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('1'))),len(b.GetConnectivity().GetConnectedItems(l.FindPadByNumber('2'))))
 raise SystemExit('FAIL VDDREG zone native connectivity')
n=b.FindNet('JMS_VDDREG_5V')
for q in list(b.GetTracks()):
 if q.GetNetCode()==n.GetNetCode():b.RemoveNative(q)
for z in list(b.Zones()):
 if z.GetNetCode()==n.GetNetCode():b.RemoveNative(z)
if ok(b):raise SystemExit('FAIL VDDREG zone-removal negative control')
b.Save(str(NEG));print('PASS VDDREG zone native connectivity; PASS zone-removal negative control')
