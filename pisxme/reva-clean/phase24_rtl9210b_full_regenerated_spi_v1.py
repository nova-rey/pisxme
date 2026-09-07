"""Disposable full regenerated RTL9210B SPI branch; no inherited local copper."""
from pathlib import Path
import re,pcbnew
HERE=Path(__file__).resolve().parent;BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_V1.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_FULL_REGENERATED_SPI_V3.kicad_pcb';SCRUB=HERE/'.phase24_full_regenerated_spi_scrubbed_v3.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20);NETS=('SPISI','SPICLK','SPISO3','SPISO','SPICS','XTAL_IN','XTAL_OUT','RSET')
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 text=BASE.read_text();m=re.search(r'\n\s*\(footprint "BRINGUP_W25Q128_SPI_FLASH"',text);assert m;st=m.start()+1;d=0
 for i in range(st,len(text)):
  if text[i]=='(':d+=1
  elif text[i]==')':
   d-=1
   if d==0:en=i+1;break
 fb=text[st:en];first=True
 def cv(q):
  nonlocal first
  x,y=float(q.group(1)),float(q.group(2));tail=q.group(3)
  if first:first=False;return '(at 86 80 0)'
  return '(at %.4f %.4f%s)'%(x-95,y-58,tail)
 fb=re.sub(r'\(at\s+([-\d.]+)\s+([-\d.]+)((?:\s+[-\d.]+)?)\)',cv,fb);text=text[:st]+fb+text[en:]
 spans=[]
 for m in re.finditer(r'\n\s+\((segment|via)\b',text):
  a=m.start()+1;dd=0
  for i in range(a,len(text)):
   if text[i]=='(':dd+=1
   elif text[i]==')':
    dd-=1
    if dd==0:
     q=text[a:i+1];pts=[(float(x),float(y)) for x,y in re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)',q)]
     if any(n in q for n in NETS) and any(80<=x<=125 and 55<=y<=82 for x,y in pts):spans.append((a,i+1))
     break
 for a,z in reversed(spans):text=text[:a]+text[z:]
 SCRUB.write_text(text);b=pcbnew.LoadBoard(str(SCRUB))
 # Source dogbones from rotated U1; source exits are staggered, then branch is regenerated.
 source=[('SPISI',(94.05,66.8),(93.0,66.8),(92.2,66.0),(88.0,66.0)),('SPICLK',(94.05,67.2),(93.0,67.2),(91.0,67.8),(88.0,67.8)),('SPISO3',(94.05,68.4),(93.0,68.4),(90.0,68.4),(88.0,68.4)),('SPISO',(94.05,68.8),(92.5,68.8),(91.0,70.0),(88.0,70.0)),('SPICS',(94.05,69.2),(93.0,69.2),(92.2,71.2),(88.0,71.2))]
 for name,pad,el,vq,end in source:
  n=b.FindNet(name);s(b,n,F,pad,el);s(b,n,F,el,vq)
  if name not in ('SPISO','SPICS'):
   v(b,n,vq);s(b,n,B,vq,end)
 # Monotonic upper group to U2 target row via B.Cu, with F.Cu dogbones into pads.
 for name,src,target in [('SPISI',(88,66),(86.6,78)),('SPICLK',(88,67.8),(87.8,78)),('SPISO3',(88,68.4),(89,78))]:
  n=b.FindNet(name);s(b,n,B,src,(target[0],src[1]));s(b,n,B,(target[0],src[1]),target);v(b,n,target);s(b,n,F,target,(target[0],80))
 # Reversed lower pair: separate F.Cu corridors; SPICS goes above SPISO before descending.
 n=b.FindNet('SPISO');s(b,n,F,(91,70),(83,70));s(b,n,F,(83,70),(83,80))
 n=b.FindNet('SPICS');s(b,n,F,(92.2,71.2),(92.2,65));s(b,n,F,(92.2,65),(81.8,65));s(b,n,F,(81.8,65),(81.8,80))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
