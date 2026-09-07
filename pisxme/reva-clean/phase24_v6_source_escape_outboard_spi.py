#!/usr/bin/env python3
"""Path-B disposable: clean V6 SPI escape, translated support destination."""
from pathlib import Path
import re
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
SCRUB=HERE/'.phase24_v6_outboard_spi_scrub.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_V6_SOURCE_OUTBOARD_SPI_V1.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
SPI={'SPICS','SPISO','SPISI','SPICLK','SPISO3'}
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def scrub(src):
 text=src.read_text(); cuts=[]; i=0
 while i<len(text):
  if text.startswith('\t(segment',i) or text.startswith('\t(via',i):
   d=0; j=i
   while j<len(text):
    if text[j]=='(': d+=1
    elif text[j]==')':
     d-=1
     if d==0:
      z=text[i:j+1]
      pts=[(float(x),float(y)) for x,y in re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)',z)]
      # Remove only old destination-side SPI copper.  V6 source pad escapes
      # stay authoritative and are not regenerated here.
      old=any(x>=84.5 and 40<=y<=75 for x,y in pts)
      if any(f'(net "{n}")' in z for n in SPI) and old: cuts.append((i,j+1))
      i=j; break
    j+=1
  i+=1
 for a,z in reversed(cuts): text=text[:a]+text[z:]
 SCRUB.write_text(text)
def route(b,n,source,bend,spine,target):
 net=b.FindNet(n); tr(b,net,F,source,bend); via(b,net,bend); last=bend
 for p in spine: tr(b,net,B,last,p); last=p
 via(b,net,last); tr(b,net,F,last,target)
def main():
 scrub(BASE); b=pcbnew.LoadBoard(str(SCRUB))
 # Translate U2 only: the source escape is unchanged, and the complete
 # support-placement variant remains disposable until its other nets move.
 u2=next(f for f in b.GetFootprints() if f.GetReference()=='U2')
 u2.SetPos(u2.GetPosition()+P(20,22))
 route(b,'SPICS',(83.95,62.8),(86,61),[(86,76),(110.8,76)],(110.8,80))
 route(b,'SPISO',(83.95,63.2),(87,62),[(87,77),(112,77)],(112,80))
 route(b,'SPISO3',(83.95,63.6),(88,63),[(88,78),(118,78)],(118,80))
 route(b,'SPICLK',(83.95,64.8),(89,64.8),[(89,79),(116.8,79)],(116.8,80))
 # Keep V6's wide SPISI F.Cu branch, moving its landing to the translated U2.
 net=b.FindNet('SPISI'); tr(b,net,F,(83.95,65.2),(85.5,70)); tr(b,net,F,(85.5,70),(105,70)); via(b,net,(105,70)); tr(b,net,B,(105,70),(105,79)); via(b,net,(105,79)); tr(b,net,F,(105,79),(115.6,80))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
