"""Disposable placement-only check using corrected U2 local pad coordinates."""
from pathlib import Path
import re
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U2_CORRECTED_LEFT_ROT90_PLACEMENT_V1.kicad_pcb'
SCRUB=HERE/'.phase24_u2_corrected_left_rot90_scrubbed.kicad_pcb'
def find_block(text,name):
 m=re.search(r'\n\s*\(footprint "'+re.escape(name)+r'"',text); assert m
 st=m.start()+1;d=0
 for i in range(st,len(text)):
  if text[i]=='(':d+=1
  elif text[i]==')':
   d-=1
   if d==0:return st,i+1,text[st:i+1]
def main():
 text=BASE.read_text();st,en,fb=find_block(text,'BRINGUP_W25Q128_SPI_FLASH');first=True
 def cv(m):
  nonlocal first
  x,y=float(m.group(1)),float(m.group(2));tail=m.group(3)
  if first:first=False;return '(at 86 76 90)'
  return '(at %.4f %.4f%s)'%(x-95,y-58,tail)
 fb=re.sub(r'\(at\s+([-\d.]+)\s+([-\d.]+)((?:\s+[-\d.]+)?)\)',cv,fb)
 text=text[:st]+fb+text[en:];SCRUB.write_text(text)
 b=pcbnew.LoadBoard(str(SCRUB));b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
