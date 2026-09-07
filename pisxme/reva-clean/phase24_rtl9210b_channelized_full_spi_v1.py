"""Disposable channelized full RTL9210B SPI branch from native source vias."""
from pathlib import Path
import re,pcbnew
HERE=Path(__file__).resolve().parent;BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_V1.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_CHANNELIZED_FULL_SPI_V1.kicad_pcb';SCRUB=HERE/'.phase24_channelized_full_spi_scrubbed.kicad_pcb'
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
 source=[('SPISI',(94.05,66.8),(93.0,66.8),(92.2,66.0)),('SPICLK',(94.05,67.2),(93.0,67.2),(91.0,67.8)),('SPISO3',(94.05,68.4),(93.0,68.4),(90.0,68.4)),('SPISO',(94.05,68.8),(92.5,68.8),(91.0,70.0)),('SPICS',(94.05,69.2),(93.0,69.2),(92.2,71.2))]
 for name,pad,el,vq in source:
  n=b.FindNet(name);s(b,n,F,pad,el);s(b,n,F,el,vq)
  if name in ('SPISI','SPICLK','SPISO3'):v(b,n,vq)
 # Upper subset: source-via columns remain separated through the U2 row.
 for name,vq,targetx in [('SPISI',(92.2,66.0),86.6),('SPICLK',(91.0,67.8),87.8),('SPISO3',(90.0,68.4),89.0)]:
  n=b.FindNet(name);s(b,n,B,vq,(targetx,vq[1]));s(b,n,B,(targetx,vq[1]),(targetx,78));v(b,n,(targetx,78));s(b,n,F,(targetx,78),(targetx,80))
 # SPISO uses an independent F.Cu corridor below the source field.
 n=b.FindNet('SPISO');s(b,n,F,(91,70),(83,70));s(b,n,F,(83,70),(83,80))
 # SPICS stays on B.Cu below the upper channels, then dogbones into U2.
 n=b.FindNet('SPICS');v(b,n,(92.2,71.2));s(b,n,B,(92.2,71.2),(92.2,79));s(b,n,B,(92.2,79),(81.8,79));v(b,n,(81.8,79));s(b,n,F,(81.8,79),(81.8,80))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
