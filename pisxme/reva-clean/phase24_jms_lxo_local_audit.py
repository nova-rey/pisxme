"""Native LXO endpoint and trace-removal negative-control audit."""
import argparse,pcbnew
ap=argparse.ArgumentParser();ap.add_argument('pcb');ap.add_argument('--negative-output');a=ap.parse_args();b=pcbnew.LoadBoard(a.pcb);u=b.FindFootprintByReference('U11');l=b.FindFootprintByReference('L10')
if not u or not l or u.FindPadByNumber('64').GetNetname()!='LXO' or l.FindPadByNumber('1').GetNetname()!='LXO':raise SystemExit('FAIL authority')
b.BuildConnectivity()
if l.FindPadByNumber('1') not in b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('64')):raise SystemExit('FAIL LXO connectivity')
for t in list(b.GetTracks()):
 if t.GetNetname()=='LXO':b.RemoveNative(t)
b.BuildConnectivity()
if l.FindPadByNumber('1') in b.GetConnectivity().GetConnectedItems(u.FindPadByNumber('64')):raise SystemExit('FAIL negative control')
if a.negative_output:b.Save(a.negative_output)
print('PASS LXO connectivity; PASS trace-removal negative control')
