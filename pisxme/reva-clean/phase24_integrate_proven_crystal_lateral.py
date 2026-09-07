#!/usr/bin/env python3
"""Disposable crystal transplant into the combined lateral support candidate."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_INTEGRATED_V2.kicad_pcb'
DONOR=HERE/'PHASE24_RTL9210B_CRYSTAL_V11.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V3.kicad_pcb'
NAMES={'XTAL_IN','XTAL_OUT'}
def blocks(text,names):
 out=[];i=0
 while i<len(text):
  if text.startswith('\t(segment',i) or text.startswith('\t(via',i):
   d=0;j=i
   while j<len(text):
    if text[j]=='(':d+=1
    elif text[j]==')':
     d-=1
     if d==0:
      z=text[i:j+1]
      if any(f'(net "{n}")' in z for n in names):out.append((i,j+1,z))
      i=j;break
    j+=1
  i+=1
 return out
def main():
 base=BASE.read_text();donor=DONOR.read_text()
 for a,z,_ in reversed(blocks(base,NAMES)):base=base[:a]+base[z:]
 ins='\n'.join(z for _,_,z in blocks(donor,NAMES))+'\n'
 base=re.sub(r'(?m)^(\s*\(gr_rect\b)',ins+r'\1',base,count=1)
 OUT.write_text(base);print(OUT)
if __name__=='__main__':main()
