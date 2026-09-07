#!/usr/bin/env python3
"""Native endpoint audit for the combined lateral SPI/rail transplant."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_INTEGRATED_V2.kicad_pcb'
SPI={'SPICS':('24',[('U2','1')]),'SPISO':('23',[('U2','2')]),'SPISI':('18',[('U2','5')]),'SPICLK':('19',[('U2','6')]),'SPISO3':('22',[('U2','7')])}
RAILS={'RTL_3V3':('34',[('C3','1'),('U2','3'),('U2','8')]),'RTL_1V1':('36',[('C4','1')]),'RTL_5V':('33',[('C5','1')])}
def fp(b,r):return next(f for f in b.GetFootprints() if f.GetReference()==r)
def main():
 b=pcbnew.LoadBoard(str(PCB));b.BuildConnectivity();c=b.GetConnectivity()
 for net,(up,eps) in {**SPI,**RAILS}.items():
  p=fp(b,'U1').FindPadByNumber(up);got={(x.GetParentFootprint().GetReference(),x.GetNumber()) for x in c.GetConnectedItems(p) if isinstance(x,pcbnew.PAD)}
  for ep in eps:
   if ep not in got:raise AssertionError(f'{net}: {ep} disconnected')
 print('PASS native combined lateral SPI and rail endpoints')
if __name__=='__main__':main()
