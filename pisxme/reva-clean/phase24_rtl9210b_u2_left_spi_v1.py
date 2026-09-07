"""Disposable class: move SPI flash left of the rotated RTL9210B and escape on B.Cu."""
from pathlib import Path
import re
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U2_LEFT_SPI_V1.kicad_pcb'
SCRUB=HERE/'.phase24_u2_left_scrubbed.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
NETS={'SPICS','SPISO','SPISO3','SPICLK','SPISI'}
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def main():
 text=BASE.read_text(); spans=[]
 for m in re.finditer(r"\n\s+\((segment|via)\b",text):
  st=m.start()+1; d=0
  for i in range(st,len(text)):
   if text[i]=='(': d+=1
   elif text[i]==')':
    d-=1
    if d==0:
     block=text[st:i+1]
     pts=[(float(x),float(y)) for x,y in re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)',block)]
     if any(n in block for n in NETS) and any(75<=x<=125 and 55<=y<=82 for x,y in pts): spans.append((st,i+1))
     break
 for a,z in reversed(spans): text=text[:a]+text[z:]
 SCRUB.write_text(text); b=pcbnew.LoadBoard(str(SCRUB))
 u2=next(x for x in b.GetFootprints() if str(x.GetReference())=='U2')
 u2.SetPosition(u2.GetPosition()+pcbnew.VECTOR2I_MM(-28,0))
 lanes=[('SPISI',(94.05,66.8),(93,66.8),90.6),('SPICLK',(94.05,67.2),(91.5,67.2),91.8),('SPISO3',(94.05,68.4),(90,68.4),93.0),('SPISO',(94.05,68.8),(88.5,68.8),87.0),('SPICS',(94.05,69.2),(87,69.2),85.8)]
 for name,src,esc,targetx in lanes:
  n=b.FindNet(name); seg(b,n,F,src,esc); via(b,n,esc); seg(b,n,B,esc,(esc[0],75)); seg(b,n,B,(esc[0],75),(targetx,75)); via(b,n,(targetx,75)); seg(b,n,F,(targetx,75),(targetx,76))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
