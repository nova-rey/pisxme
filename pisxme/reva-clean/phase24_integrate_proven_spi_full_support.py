#!/usr/bin/env python3
"""Disposable transplant of the proven SPI geometry into full support placement."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_PLACEMENT_V1.kicad_pcb'
DONOR=HERE/'PHASE24_RTL9210B_SPI_ONLY_LATERAL_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_FULL_LATERAL_SPI_INTEGRATED_V1.kicad_pcb'
SPI={'SPICS','SPISO','SPISI','SPICLK','SPISO3'}
def blocks(text):
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
      if any(f'(net "{n}")' in z for n in SPI):out.append((i,j+1,z))
      i=j;break
    j+=1
  i+=1
 return out
def main():
 base=BASE.read_text(); donor=DONOR.read_text()
 cuts=blocks(base)
 for a,z,_ in reversed(cuts):base=base[:a]+base[z:]
 inserts='\n'.join(z for _,_,z in blocks(donor))+'\n'
 base=re.sub(r'(?m)^(\s*\(gr_rect\b)',inserts+r'\1',base,count=1)
 OUT.write_text(base);print(OUT)
if __name__=='__main__':main()
