"""Native U11-to-C83 AVDDL audit and trace-removal negative control."""
import argparse,pcbnew
ap=argparse.ArgumentParser();ap.add_argument('pcb');ap.add_argument('--negative-output');a=ap.parse_args();b=pcbnew.LoadBoard(a.pcb);u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C83')
if not u or not c or u.FindPadByNumber('20').GetNetname()!='JMS_AVDDL' or c.FindPadByNumber('1').GetNetname()!='JMS_AVDDL':raise SystemExit('FAIL authority')
b.BuildConnectivity()
if c.FindPadByNumber('1') not in b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('20')):raise SystemExit('FAIL AVDDL connectivity')
for t in list(b.GetTracks()):
 if t.GetNetname()=='JMS_AVDDL':b.RemoveNative(t)
b.BuildConnectivity()
if c.FindPadByNumber('1') in b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('20')):raise SystemExit('FAIL negative control')
if a.negative_output:b.Save(a.negative_output)
print('PASS U11 AVDDL connectivity; PASS trace-removal negative control')
