"""Native XAVDDH audit for the local fine-escape candidate."""
from pathlib import Path
import argparse,pcbnew
ap=argparse.ArgumentParser();ap.add_argument('pcb');ap.add_argument('--negative-output');a=ap.parse_args();b=pcbnew.LoadBoard(a.pcb);u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C84')
if not u or not c or u.FindPadByNumber('52').GetNetname()!='JMS_XAVDDH' or c.FindPadByNumber('1').GetNetname()!='JMS_XAVDDH':raise SystemExit('FAIL authority')
b.BuildConnectivity();
if c.FindPadByNumber('1') not in b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('52')):raise SystemExit('FAIL connectivity')
for t in list(b.GetTracks()):
 if t.GetNetname()=='JMS_XAVDDH':b.RemoveNative(t)
b.BuildConnectivity();
if c.FindPadByNumber('1') in b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('52')):raise SystemExit('FAIL negative control')
if a.negative_output:b.Save(a.negative_output)
print('PASS XAVDDH connectivity; PASS trace-removal negative control')
