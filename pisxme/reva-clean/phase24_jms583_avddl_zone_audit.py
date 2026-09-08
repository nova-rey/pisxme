"""Native AVDDL zone connectivity and zone-removal negative control."""
from pathlib import Path
import os,pcbnew
R=Path(__file__).resolve().parent;PCB=Path(os.environ.get('PISXME_AVDDL_ZONE_PCB',R/'PHASE24_DUAL_MODE_STORAGE_FULL7_AVDDL_local_zone.kicad_pcb'));NEG=Path(os.environ.get('PISXME_AVDDL_ZONE_NEG',R/'PHASE24_DUAL_MODE_STORAGE_FULL7_AVDDL_local_zone-negative.kicad_pcb'))
def ok(b):
 b.BuildConnectivity();u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C83');a=b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('20'));d=b.GetConnectivity().GetConnectedItems(c.FindPadByNumber('1'));return c.FindPadByNumber('1') in a or any(x in d for x in a if isinstance(x,pcbnew.ZONE))
b=pcbnew.LoadBoard(str(PCB))
if not ok(b):raise SystemExit('FAIL AVDDL zone native connectivity')
n=b.FindNet('JMS_AVDDL')
for q in list(b.GetTracks()):
 if q.GetNetCode()==n.GetNetCode():b.RemoveNative(q)
for z in list(b.Zones()):
 if z.GetNetCode()==n.GetNetCode():b.RemoveNative(z)
if ok(b):raise SystemExit('FAIL AVDDL zone-removal negative control')
b.Save(str(NEG));print('PASS AVDDL zone native connectivity; PASS zone-removal negative control')
