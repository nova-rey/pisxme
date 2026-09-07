"""Add the previously audited lateral SPI geometry to staged V4."""
from pathlib import Path
import re
BASE=Path("PHASE24_RTL9210B_1V1_CRYSTAL_RSET_STAGED_V4.kicad_pcb")
DONOR=Path("PHASE24_RTL9210B_SPI_ONLY_LATERAL_V1.kicad_pcb")
OUT=Path("PHASE24_RTL9210B_V4_WITH_SPI_V1.kicad_pcb")
NETS={"SPICS","SPISO","SPISI","SPICLK","SPISO3"}
def blocks(text):
 out=[];i=0
 while i<len(text):
  if text.startswith("(segment",i) or text.startswith("(via",i) or text.startswith("  (segment",i) or text.startswith("  (via",i):
   d=0;j=i
   while j<len(text):
    if text[j]=='(':d+=1
    elif text[j]==')':
     d-=1
     if d==0:
      z=text[i:j+1]
      if any(f'(net "{n}")' in z for n in NETS):out.append(z)
      i=j;break
    j+=1
  i+=1
 return out
def main():
 base=BASE.read_text();add='\n'.join(blocks(DONOR.read_text()))+'\n'
 base=re.sub(r'(?m)^(\s*\(gr_rect\b)',add+r'\1',base,count=1)
 OUT.write_text(base);print(f'{OUT} ({len(blocks(DONOR.read_text()))} objects)')
if __name__=='__main__':main()
