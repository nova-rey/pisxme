#!/usr/bin/env python3
"""Native saved-board rail endpoint audit and serialized negative control."""
from pathlib import Path
import re
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_RAIL_ONLY_LATERAL_V1.kicad_pcb'
EPS={'RTL_3V3':('34',('C3','1')),'RTL_1V1':('36',('C4','1')),'RTL_5V':('33',('C5','1'))}
def fp(b,r):return next(f for f in b.GetFootprints() if f.GetReference()==r)
def audit(b):
 b.BuildConnectivity();c=b.GetConnectivity()
 for net,(up,other) in EPS.items():
  p=fp(b,'U1').FindPadByNumber(up);got={(x.GetParentFootprint().GetReference(),x.GetNumber()) for x in c.GetConnectedItems(p) if isinstance(x,pcbnew.PAD)}
  if other not in got:raise AssertionError(f'{net}: {other} disconnected')
 print('PASS native rail endpoints: U1 to C3/C4/C5')
def negative():
 text=PCB.read_text();cuts=[];i=0
 while i<len(text):
  if text.startswith('\t(segment',i) or text.startswith('\t(via',i):
   d=0;j=i
   while j<len(text):
    if text[j]=='(':d+=1
    elif text[j]==')':
     d-=1
     if d==0:
      z=text[i:j+1]
      if '(net "RTL_3V3")' in z:cuts.append((i,j+1))
      i=j;break
    j+=1
  i+=1
 for a,z in reversed(cuts):text=text[:a]+text[z:]
 probe=ROOT/'.phase24_rail_only_negative.kicad_pcb';probe.write_text(text)
 try:audit(pcbnew.LoadBoard(str(probe)))
 except AssertionError:print('PASS negative control: removed RTL_3V3 copper fails')
 else:raise AssertionError('negative control unexpectedly passed')
if __name__=='__main__':audit(pcbnew.LoadBoard(str(PCB)));negative()
