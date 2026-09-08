"""Native endpoint and negative-control audit for the REXT V8 escape."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
PCB=R/'PHASE24_JMS583_SUPPORT_COHORT_REXT_V8.kicad_pcb'
NEG=R/'PHASE24_JMS583_SUPPORT_COHORT_REXT_V8_NEGATIVE.kicad_pcb'
b=pcbnew.LoadBoard(str(PCB)); u=b.FindFootprintByReference('U11'); r=b.FindFootprintByReference('R80')
if not u or not r: raise SystemExit('FAIL missing REXT endpoints')
src=u.FindPadByNumber('39'); dst=r.FindPadByNumber('1'); b.BuildConnectivity()
if dst not in b.GetConnectivity().GetConnectedItems(src): raise SystemExit('FAIL JMS_REXT native connectivity')
n=b.FindNet('JMS_REXT');
for item in list(b.GetTracks()):
    if item.GetNetCode()==n.GetNetCode(): b.RemoveNative(item)
b.BuildConnectivity()
if dst in b.GetConnectivity().GetConnectedItems(src): raise SystemExit('FAIL JMS_REXT trace-removal negative control')
b.Save(str(NEG)); print('PASS JMS_REXT V8 connectivity; PASS trace-removal negative control')
