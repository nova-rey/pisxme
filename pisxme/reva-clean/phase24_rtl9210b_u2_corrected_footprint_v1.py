"""Disposable test with U2 converted from absolute-pad to proper local coordinates."""
from pathlib import Path
import re
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U2_CORRECTED_FOOTPRINT_V1.kicad_pcb'
SCRUB=HERE/'.phase24_u2_corrected_scrubbed.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
NETS={'SPICS','SPISO','SPISO3','SPICLK','SPISI'}
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def block(text, name):
 m=re.search(r'\n\s*\(footprint "'+re.escape(name)+r'"',text); assert m
 st=m.start()+1; d=0
 for i in range(st,len(text)):
  if text[i]=='(': d+=1
  elif text[i]==')':
   d-=1
   if d==0:return st,i+1,text[st:i+1]
 raise RuntimeError('unbalanced footprint')
def main():
 text=BASE.read_text(); st,en,fb=block(text,'BRINGUP_W25Q128_SPI_FLASH')
 # Existing pads/property coordinates encode intended global origin (95,58).
 first=True
 def cv(m):
  nonlocal first
  x,y=float(m.group(1)),float(m.group(2)); tail=m.group(3)
  if first: first=False; return '(at 90 76'+tail+')'
  return '(at %.4f %.4f%s)'%(x-95,y-58,tail)
 fb=re.sub(r'\(at\s+([-\d.]+)\s+([-\d.]+)((?:\s+[-\d.]+)?)\)',cv,fb)
 text=text[:st]+fb+text[en:]
 # Remove all prior local SPI copper before reloading native geometry.
 spans=[]
 for m in re.finditer(r"\n\s+\((segment|via)\b",text):
  a=m.start()+1; d=0
  for i in range(a,len(text)):
   if text[i]=='(':d+=1
   elif text[i]==')':
    d-=1
    if d==0:
     q=text[a:i+1]; pts=[(float(x),float(y)) for x,y in re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)',q)]
     if any(n in q for n in NETS) and any(80<=x<=125 and 55<=y<=82 for x,y in pts):spans.append((a,i+1))
     break
 for a,z in reversed(spans):text=text[:a]+text[z:]
 SCRUB.write_text(text);b=pcbnew.LoadBoard(str(SCRUB))
 # Real corrected U2 pads are x=85.8..93.0 at y=76 after placement.
 lanes=[('SPISI',(94.05,66.8), (93.8,70), 90.6),('SPICLK',(94.05,67.2),(93.0,71.2),91.8),('SPISO3',(94.05,68.4),(92.2,72.4),93.0),('SPISO',(94.05,68.8),(91.4,73.6),87.0),('SPICS',(94.05,69.2),(90.6,74.8),85.8)]
 for name,src,esc,targetx in lanes:
  n=b.FindNet(name);seg(b,n,F,src,esc);via(b,n,esc);seg(b,n,B,esc,(esc[0],75));seg(b,n,B,(esc[0],75),(targetx,75));via(b,n,(targetx,75));seg(b,n,F,(targetx,75),(targetx,76))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
