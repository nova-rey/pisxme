"""Disposable corrected-U2 placement with order-preserving two-layer SPI partition."""
from pathlib import Path
import re, pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_V1.kicad_pcb'; OUT=HERE/'PHASE24_RTL9210B_U2_CORRECTED_FAR_PARTITION_SPI_V1.kicad_pcb'; SCRUB=HERE/'.phase24_u2_far_partition_scrubbed.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20);NETS={'SPICS','SPISO','SPISO3','SPICLK','SPISI'}
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def fb(text):
 m=re.search(r'\n\s*\(footprint "BRINGUP_W25Q128_SPI_FLASH"',text);assert m;st=m.start()+1;d=0
 for i in range(st,len(text)):
  if text[i]=='(':d+=1
  elif text[i]==')':
   d-=1
   if d==0:return st,i+1,text[st:i+1]
def main():
 text=BASE.read_text();st,en,x=fb(text);first=True
 def cv(m):
  nonlocal first
  a,b=float(m.group(1)),float(m.group(2));tail=m.group(3)
  if first:first=False;return '(at 86 90 90)'
  return '(at %.4f %.4f%s)'%(a-95,b-58,tail)
 x=re.sub(r'\(at\s+([-\d.]+)\s+([-\d.]+)((?:\s+[-\d.]+)?)\)',cv,x);text=text[:st]+x+text[en:]
 spans=[]
 for m in re.finditer(r'\n\s+\((segment|via)\b',text):
  start=m.start()+1;d=0
  for i in range(start,len(text)):
   if text[i]=='(':d+=1
   elif text[i]==')':
    d-=1
    if d==0:
     q=text[start:i+1];pts=[(float(px),float(py)) for px,py in re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)',q)]
     if any(n in q for n in NETS) and any(80<=px<=125 and 55<=py<=100 for px,py in pts):spans.append((start,i+1))
     break
 for a,z in reversed(spans):text=text[:a]+text[z:]
 SCRUB.write_text(text);b=pcbnew.LoadBoard(str(SCRUB))
 # SPISO3/SPISI preserve relative order on F; SPICLK/SPISO/SPICS preserve it on B.
 lanes=[('SPISO3',(94.05,68.4),F,(93.5,68.4),(86.0,87.0)),('SPISI',(94.05,66.8),F,(91.5,66.8),(86.0,89.4)),('SPICLK',(94.05,67.2),B,(92.5,67.2),(86.0,88.2)),('SPISO',(94.05,68.8),B,(90.5,68.8),(86.0,93.0)),('SPICS',(94.05,69.2),B,(88.5,69.2),(86.0,94.2))]
 for name,src,layer,esc,dst in lanes:
  n=b.FindNet(name);s(b,n,F,src,esc);v(b,n,esc);app=(87.4,dst[1]);s(b,n,layer,esc,app);v(b,n,app);s(b,n,F,app,dst)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
