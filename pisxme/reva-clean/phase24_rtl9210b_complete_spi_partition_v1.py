"""Disposable complete five-net U1-to-corrected-U2 two-layer SPI partition."""
from pathlib import Path
import re,pcbnew
HERE=Path(__file__).resolve().parent;BASE=HERE/'PHASE24_RTL9210B_U1_QFN_FIVE_DOGBONES_V4.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_COMPLETE_SPI_PARTITION_V1.kicad_pcb';SCRUB=HERE/'.phase24_complete_spi_partition_scrubbed.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
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
 SCRUB.write_text(text);b=pcbnew.LoadBoard(str(SCRUB))
 # U2 0-degree pads: SPICS=81.8, SPISO=83.0, SPISI=86.6, SPICLK=87.8, SPISO3=89.0 at y80.
 lanes=[('SPISO3',(88.0,68.4),B,(89.0,78.0)),('SPICLK',(88.0,67.8),B,(87.8,78.0)),('SPISI',(88.0,66.0),B,(86.6,78.0)),('SPISO',(88.0,70.0),F,(83.0,78.0)),('SPICS',(88.0,71.2),F,(81.8,78.0))]
 for name,src,layer,dst in lanes:
  n=b.FindNet(name)
  if layer==F:v(b,n,src)
  s(b,n,layer,src,dst);v(b,n,dst);s(b,n,F,dst,(dst[0],80.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
