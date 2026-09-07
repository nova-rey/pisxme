#!/usr/bin/env python3
"""Disposable full-support transplant of proven lateral SPI and rail copper."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_PLACEMENT_V1.kicad_pcb'
SPI_DONOR=HERE/'PHASE24_RTL9210B_SPI_ONLY_LATERAL_V1.kicad_pcb'
RAIL_DONOR=HERE/'PHASE24_RTL9210B_RAIL_ONLY_LATERAL_U2_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_INTEGRATED_V2.kicad_pcb'
SPI={'SPICS','SPISO','SPISI','SPICLK','SPISO3'}
RAILS={'RTL_3V3','RTL_1V1','RTL_5V'}
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
def remove(text,names):
 cuts=blocks(text,names)
 for a,z,_ in reversed(cuts):text=text[:a]+text[z:]
 return text
def main():
 base=remove(BASE.read_text(),SPI|RAILS)
 add='\n'.join(z for _,_,z in blocks(SPI_DONOR.read_text(),SPI))+'\n'
 add+='\n'.join(z for _,_,z in blocks(RAIL_DONOR.read_text(),RAILS))+'\n'
 base=re.sub(r'(?m)^(\s*\(gr_rect\b)',add+r'\1',base,count=1)
 OUT.write_text(base);print(OUT)
if __name__=='__main__':main()
