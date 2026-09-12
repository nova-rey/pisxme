"""Audit the accumulated native JMS583 support joins and negative control."""
from pathlib import Path
import argparse,pcbnew
ap=argparse.ArgumentParser();ap.add_argument('pcb');ap.add_argument('--negative-output');a=ap.parse_args();b=pcbnew.LoadBoard(a.pcb)
PAIRS=[('JMS_REXT','U11','39','R80','1'),('JMS_RESET_N','U11','15','R81','1'),('JMS_AVDD33','U11','19','C80','1'),('JMS_VCCO','U11','6','C81','1'),('JMS_VCCK','U11','2','C82','1')]
b.BuildConnectivity();c=b.GetConnectivity()
for net,ra,pa,rb,pb in PAIRS:
 x=b.FindFootprintByReference(ra).FindPadByNumber(pa);y=b.FindFootprintByReference(rb).FindPadByNumber(pb)
 if x.GetNetname()!=net or y.GetNetname()!=net or y not in c.GetConnectedItems(x):raise SystemExit('FAIL '+net)
for t in list(b.GetTracks()):
 if t.GetNetname() in {x[0] for x in PAIRS}:b.RemoveNative(t)
b.BuildConnectivity()
if any(b.FindFootprintByReference(rb).FindPadByNumber(pb) in b.GetConnectivity().GetConnectedItems(b.FindFootprintByReference(ra).FindPadByNumber(pa)) for _,ra,pa,rb,pb in PAIRS):raise SystemExit('FAIL negative control')
if a.negative_output:b.Save(a.negative_output)
print('PASS accumulated JMS support joins; PASS trace-removal negative control')
