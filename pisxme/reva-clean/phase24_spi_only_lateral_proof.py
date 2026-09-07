#!/usr/bin/env python3
"""Disposable SPI-only proof from the native V6 fixture."""
from pathlib import Path
import re
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
SCRUB=HERE/'.phase24_spi_only_base.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SPI_ONLY_LATERAL_V1.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
SPI={'SPICS','SPISO','SPISI','SPICLK','SPISO3'}
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def strip(src):
 text=src.read_text(); cuts=[]; i=0
 while i<len(text):
  if text.startswith('\t(segment',i) or text.startswith('\t(via',i):
   d=0;j=i
   while j<len(text):
    if text[j]=='(':d+=1
    elif text[j]==')':
     d-=1
     if d==0:
      z=text[i:j+1]
      if not any(f'(net "{n}")' in z for n in SPI|{'GND'}): cuts.append((i,j+1))
      i=j;break
    j+=1
  i+=1
 for a,z in reversed(cuts):text=text[:a]+text[z:]
 SCRUB.write_text(text)
def route(b,name,bend,spine,target):
 n=b.FindNet(name);last=bend
 for p in spine:tr(b,n,B,last,p);last=p
 via(b,n,last);tr(b,n,F,last,target)
def main():
 strip(BASE); b=pcbnew.LoadBoard(str(SCRUB))
 u2=next(f for f in b.GetFootprints() if f.GetReference()=='U2');u2.SetPos(u2.GetPosition()+P(35,0))
 route(b,'SPICS',(86,61),[(86,48),(125.8,48)],(125.8,58))
 route(b,'SPISO',(87,62),[(87,49),(127,49)],(127,58))
 route(b,'SPISO3',(88,63),[(88,50),(133,50)],(133,58))
 route(b,'SPICLK',(89,64.8),[(89,52),(131.8,52)],(131.8,58))
 n=b.FindNet('SPISI');tr(b,n,F,(85.5,70),(120,70));tr(b,n,F,(120,70),(130.6,70));tr(b,n,F,(130.6,70),(130.6,58))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
