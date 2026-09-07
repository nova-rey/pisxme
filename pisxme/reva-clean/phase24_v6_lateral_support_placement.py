#!/usr/bin/env python3
"""Disposable Path-B placement: move bridge/decoupling laterally only."""
from pathlib import Path
import re
import pcbnew
from phase24_relocate_rtl9210b_support_branch import v
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_V6_LATERAL_SUPPORT_PLACEMENT_V2.kicad_pcb'
NETS={'RTL_3V3','RTL_1V1','RTL_5V','SPICS','SPISO','SPISI','SPICLK','SPISO3'}
def scrub(src):
 text=src.read_text(); cuts=[]; i=0
 while i<len(text):
  if text.startswith('\t(segment',i) or text.startswith('\t(via',i):
   d=0; j=i
   while j<len(text):
    if text[j]=='(': d+=1
    elif text[j]==')':
     d-=1
     if d==0:
      z=text[i:j+1]; pts=[(float(x),float(y)) for x,y in re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)',z)]
      if any(f'(net "{n}")' in z for n in NETS) and any(x>=89 and 40<=y<=75 for x,y in pts): cuts.append((i,j+1))
      i=j; break
    j+=1
  i+=1
 for a,z in reversed(cuts): text=text[:a]+text[z:]
 (HERE/'.phase24_v6_lateral_scrub.kicad_pcb').write_text(text)
def main():
 scrub(BASE); b=pcbnew.LoadBoard(str(HERE/'.phase24_v6_lateral_scrub.kicad_pcb'))
 for ref in {'U2','C3','C4','C5'}:
  f=next(x for x in b.GetFootprints() if x.GetReference()==ref); f.SetPos(f.GetPosition()+v(20,0))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
