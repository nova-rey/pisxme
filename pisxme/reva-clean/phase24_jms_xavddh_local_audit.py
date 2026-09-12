"""Native JMS_XAVDDH audit with a saved-copper negative control."""
from pathlib import Path
import argparse
import pcbnew

ap=argparse.ArgumentParser(); ap.add_argument('pcb'); ap.add_argument('--negative-output',default=None); a=ap.parse_args()
b=pcbnew.LoadBoard(a.pcb); u=b.FindFootprintByReference('U11'); c=b.FindFootprintByReference('C84')
if not u or not c or u.FindPadByNumber('52').GetNetname()!='JMS_XAVDDH' or c.FindPadByNumber('1').GetNetname()!='JMS_XAVDDH': raise SystemExit('FAIL endpoint authority')
b.BuildConnectivity();
if c.FindPadByNumber('1') not in b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('52')): raise SystemExit('FAIL JMS_XAVDDH connectivity')
for item in list(b.GetTracks()):
    if item.GetNetname()=='JMS_XAVDDH': b.RemoveNative(item)
b.BuildConnectivity()
if c.FindPadByNumber('1') in b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('52')): raise SystemExit('FAIL trace-removal negative control')
if a.negative_output: b.Save(a.negative_output)
print('PASS JMS_XAVDDH connectivity; PASS trace-removal negative control')
