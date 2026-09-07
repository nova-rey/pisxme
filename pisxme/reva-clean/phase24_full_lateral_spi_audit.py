#!/usr/bin/env python3
"""Saved-board SPI endpoint audit for the full-support transplant."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_FULL_LATERAL_SPI_INTEGRATED_V1.kicad_pcb'
EPS={'SPICS':('24','1'),'SPISO':('23','2'),'SPISI':('18','5'),'SPICLK':('19','6'),'SPISO3':('22','7')}
def fp(b,r): return next(f for f in b.GetFootprints() if f.GetReference()==r)
def audit(b):
 b.BuildConnectivity(); c=b.GetConnectivity()
 for net,(a,z) in EPS.items():
  p=fp(b,'U1').FindPadByNumber(a); got={(x.GetParentFootprint().GetReference(),x.GetNumber()) for x in c.GetConnectedItems(p) if isinstance(x,pcbnew.PAD)}
  got.add(('U1',a))
  if ('U2',z) not in got: raise AssertionError(f'{net}: U2.{z} disconnected')
 print('PASS native full-support SPI endpoints: 5 nets')
if __name__=='__main__': audit(pcbnew.LoadBoard(str(PCB)))
