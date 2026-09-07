"""Disposable U1 180-degree rotation, preserving the exposed-pad center."""
from pathlib import Path
import re
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_RELOCATION_U2_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_ROTATE_U1_V1.kicad_pcb'
SCRUB=HERE/'.phase24_rotate_u1_scrubbed.kicad_pcb'
NETS={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','RESET_N','PERST_N','SPICS','SPISO','SPISO3','SPICLK','SPISI'}
def main():
 text=BASE.read_text(); spans=[]
 for m in re.finditer(r"\n\s+\((segment|via)\b",text):
  st=m.start()+1;d=0
  for i in range(st,len(text)):
   if text[i]=='(':d+=1
   elif text[i]==')':
    d-=1
    if d==0:
     block=text[st:i+1];pts=[(float(x),float(y)) for x,y in re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)',block)]
     if any(n in block for n in NETS) and any(90<=x<=120 and 58<=y<=82 for x,y in pts):spans.append((st,i+1))
     break
  
 for a,z in reversed(spans):text=text[:a]+text[z:]
 SCRUB.write_text(text);b=pcbnew.LoadBoard(str(SCRUB))
 u=next(x for x in b.GetFootprints() if str(x.GetReference())=='U1');ep=u.FindPadByNumber('69').GetPosition()
 u.SetOrientationDegrees(180);q=u.FindPadByNumber('69').GetPosition()
 u.SetPosition(pcbnew.VECTOR2I(u.GetPosition().x+ep.x-q.x,u.GetPosition().y+ep.y-q.y))
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
