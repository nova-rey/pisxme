#!/usr/bin/env python3
"""Saved-board native connectivity audit for the SPI-only lateral proof."""
from pathlib import Path
import re
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_SPI_ONLY_LATERAL_V1.kicad_pcb'
EXPECTED={
 'SPICS':[('U1','24'),('U2','1')], 'SPISO':[('U1','23'),('U2','2')],
 'SPISI':[('U1','18'),('U2','5')], 'SPICLK':[('U1','19'),('U2','6')],
 'SPISO3':[('U1','22'),('U2','7')]}
def pad(b,r,n): return next(f for f in b.GetFootprints() if f.GetReference()==r).FindPadByNumber(n)
def peers(b,p):
 out=set();
 for x in b.GetConnectivity().GetConnectedItems(p):
  if isinstance(x,pcbnew.PAD): out.add((x.GetParentFootprint().GetReference(),x.GetNumber()))
 out.add((p.GetParentFootprint().GetReference(),p.GetNumber())); return out
def audit(b):
 b.BuildConnectivity()
 for net,eps in EXPECTED.items():
  got=peers(b,pad(b,*eps[0]))
  for ep in eps:
   if ep not in got: raise AssertionError(f'{net}: {ep} not connected')
 print('PASS native SPI-only lateral U1-U2 endpoint connectivity')
def negative():
 text=PCB.read_text(); cuts=[]; i=0
 while i<len(text):
  if text.startswith('\t(segment',i) or text.startswith('\t(via',i):
   d=0;j=i
   while j<len(text):
    if text[j]=='(':d+=1
    elif text[j]==')':
     d-=1
     if d==0:
      z=text[i:j+1]
      if '(net "SPICS")' in z: cuts.append((i,j+1))
      i=j;break
    j+=1
  i+=1
 if not cuts: raise AssertionError('no SPICS copper for negative control')
 for a,z in reversed(cuts):text=text[:a]+text[z:]
 probe=ROOT/'.phase24_spi_only_negative.kicad_pcb'; probe.write_text(text)
 b=pcbnew.LoadBoard(str(probe))
 try: audit(b)
 except AssertionError: print('PASS negative control: removed SPICS copper fails')
 else: raise AssertionError('negative control unexpectedly passed')
if __name__=='__main__': b=pcbnew.LoadBoard(str(PCB)); audit(b); negative()
