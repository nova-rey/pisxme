#!/usr/bin/env python3
"""Disposable Path-B SPI route with the support branch farther outboard."""
from pathlib import Path
import re
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_BRANCH_OUTBOARD_V2.kicad_pcb'
SCRUB=HERE/'.phase24_outboard_spi_scrub.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SUPPORT_BRANCH_OUTBOARD_SPI_V4.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
SPI={'SPICS','SPISO','SPISI','SPICLK','SPISO3','PEDET','CLKREQ_N','PERST_N','RESET_N'}
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
      if any(f'(net "{n}")' in z for n in SPI): cuts.append((i,j+1))
      i=j; break
    j+=1
  i+=1
 for a,z in reversed(cuts): text=text[:a]+text[z:]
 SCRUB.write_text(text)
def route(b,n,s,sv,corridor,tv):
 net=b.FindNet(n); tr(b,net,F,s,sv); via(b,net,sv); last=sv
 for p in corridor: tr(b,net,B,last,p); last=p
 via(b,net,last); tr(b,net,F,last,tv)
def main():
 scrub(BASE); b=pcbnew.LoadBoard(str(SCRUB))
 route(b,'SPICS',(83.95,62.8),(85,61),[(86,61),(86,78),(110.8,78)],(110.8,80))
 route(b,'SPISO',(83.95,63.2),(85.5,62),[(87,62),(87,79),(112,79)],(112,80))
 route(b,'SPISO3',(83.95,63.6),(86,63),[(88,63),(88,81),(118,81)],(118,80))
 route(b,'SPICLK',(83.95,64.8),(89,64.8),[(89,82),(116.8,82)],(116.8,80))
 net=b.FindNet('SPISI'); tr(b,net,F,(83.95,65.2),(85.5,70)); tr(b,net,F,(85.5,70),(105,70)); via(b,net,(105,70)); tr(b,net,B,(105,70),(105,79)); via(b,net,(105,79)); tr(b,net,F,(105,79),(115.6,80))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
