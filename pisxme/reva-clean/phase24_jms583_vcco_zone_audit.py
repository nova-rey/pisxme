"""Native VCCO zone connectivity audit with a zone-removal negative control."""
from pathlib import Path
import os
import pcbnew
R=Path(__file__).resolve().parent
PCB=Path(os.environ.get('PISXME_VCCO_ZONE_AUDIT_PCB',R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VCCO_local_zone.kicad_pcb'))
NEG=Path(os.environ.get('PISXME_VCCO_ZONE_AUDIT_NEG',R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VCCO_local_zone-negative.kicad_pcb'))
def connected(b):
 b.BuildConnectivity();u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C81');return c.FindPadByNumber('1') in b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('6'))
b=pcbnew.LoadBoard(str(PCB))
if not connected(b):
 b.BuildConnectivity();u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C81')
 print('DEBUG',len(b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('6'))),len(b.GetConnectivity().GetConnectedItems(c.FindPadByNumber('1'))))
 raise SystemExit('FAIL VCCO zone native connectivity')
n=b.FindNet('JMS_VCCO')
for item in list(b.GetTracks()):
 if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
for zone in list(b.Zones()):
 if zone.GetNetCode()==n.GetNetCode():b.RemoveNative(zone)
if connected(b):raise SystemExit('FAIL VCCO zone-removal negative control')
b.Save(str(NEG));print('PASS VCCO zone native connectivity; PASS zone-removal negative control')
