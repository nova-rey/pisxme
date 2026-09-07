#!/usr/bin/env python3
"""Native audit for the complete lateral RTL_3V3 support branch."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_RAIL_ONLY_LATERAL_U2_V2.kicad_pcb'
def fp(b,r):return next(f for f in b.GetFootprints() if f.GetReference()==r)
def main():
 b=pcbnew.LoadBoard(str(PCB));b.BuildConnectivity();c=b.GetConnectivity()
 p=fp(b,'U1').FindPadByNumber('34');got={(x.GetParentFootprint().GetReference(),x.GetNumber()) for x in c.GetConnectedItems(p) if isinstance(x,pcbnew.PAD)}
 for ep in [('C3','1'),('U2','3'),('U2','8')]:
  if ep not in got:raise AssertionError(f'RTL_3V3: {ep} disconnected')
 print('PASS native complete RTL_3V3 branch: U1.34/C3.1/U2.3/U2.8')
if __name__=='__main__':main()
