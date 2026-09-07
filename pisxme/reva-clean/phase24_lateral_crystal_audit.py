#!/usr/bin/env python3
"""Native crystal endpoint audit for the combined lateral candidate."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V3.kicad_pcb'
EPS={'XTAL_IN':[('U1','53'),('Y1','1'),('C1','1')],'XTAL_OUT':[('U1','54'),('Y1','2'),('C2','1')]}
def fp(b,r):return next(f for f in b.GetFootprints() if f.GetReference()==r)
def main():
 b=pcbnew.LoadBoard(str(PCB));b.BuildConnectivity();c=b.GetConnectivity()
 for net,eps in EPS.items():
  p=fp(b,'U1').FindPadByNumber(eps[0][1]);got={(x.GetParentFootprint().GetReference(),x.GetNumber()) for x in c.GetConnectedItems(p) if isinstance(x,pcbnew.PAD)}
  if any(ep not in got for ep in eps):raise AssertionError(f'{net}: endpoint missing')
 print('PASS native lateral crystal endpoints: XTAL_IN/XTAL_OUT')
if __name__=='__main__':main()
