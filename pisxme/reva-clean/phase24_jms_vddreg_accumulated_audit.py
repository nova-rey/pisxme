"""Audit both VDDREG branches and their trace-removal negative control."""
import argparse,pcbnew
ap=argparse.ArgumentParser();ap.add_argument('pcb');ap.add_argument('--negative-output');a=ap.parse_args();b=pcbnew.LoadBoard(a.pcb);l=b.FindFootprintByReference('L10')
if not l:raise SystemExit('FAIL missing L10')
b.BuildConnectivity();c=b.GetConnectivity()
for ref in ('U11','U12'):
 x=b.FindFootprintByReference(ref).FindPadByNumber('1')
 if x.GetNetname()!='JMS_VDDREG_5V' or l.FindPadByNumber('2') not in c.GetConnectedItems(x):raise SystemExit('FAIL '+ref+' VDDREG')
for t in list(b.GetTracks()):
 if t.GetNetname()=='JMS_VDDREG_5V':b.RemoveNative(t)
b.BuildConnectivity()
if any(l.FindPadByNumber('2') in b.GetConnectivity().GetConnectedItems(b.FindFootprintByReference(ref).FindPadByNumber('1')) for ref in ('U11','U12')):raise SystemExit('FAIL negative control')
if a.negative_output:b.Save(a.negative_output)
print('PASS U11/U12 VDDREG connectivity; PASS trace-removal negative control')
