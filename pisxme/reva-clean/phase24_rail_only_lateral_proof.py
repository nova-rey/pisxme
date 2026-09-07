#!/usr/bin/env python3
"""Disposable rail-only proof for the laterally relocated RTL9210B support."""
from pathlib import Path
import re
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
SCRUB=HERE/'.phase24_rail_only_lateral_base.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RAIL_ONLY_LATERAL_V1.kicad_pcb'
RAILS={'RTL_3V3','RTL_1V1','RTL_5V','GND'}
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def strip(src):
 text=src.read_text();cuts=[];i=0
 while i<len(text):
  if text.startswith('\t(segment',i) or text.startswith('\t(via',i):
   d=0;j=i
   while j<len(text):
    if text[j]=='(':d+=1
    elif text[j]==')':
     d-=1
     if d==0:
      z=text[i:j+1]
      pts=[(float(x),float(y)) for x,y in re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)',z)]
      names={n for n in RAILS if f'(net "{n}")' in z}
      if not names or names != {'GND'}:cuts.append((i,j+1))
      i=j;break
    j+=1
  i+=1
 for a,z in reversed(cuts):text=text[:a]+text[z:]
 SCRUB.write_text(text)
def main():
 strip(BASE);b=pcbnew.LoadBoard(str(SCRUB))
 for ref,dx in [('U2',35),('C3',20),('C4',20),('C5',20)]:
  f=next(x for x in b.GetFootprints() if x.GetReference()==ref);f.SetPos(f.GetPosition()+P(dx,0))
 # Separate B.Cu rail spines; only the selected U1 source pads are asserted
 # here.  Additional QFN rail pads remain for the subsequent collector pass.
 # Use alternating layers for the three long spines.  This avoids crossing
 # one rail's source escape with another rail's horizontal collector.
 n=b.FindNet('RTL_3V3');tr(b,n,F,(83.95,58.8),(83.95,57.5));tr(b,n,F,(83.95,57.5),(86.5,57.5));via(b,n,(86.5,57.5));tr(b,n,B,(86.5,57.5),(86.5,43));tr(b,n,B,(86.5,43),(120.4,43));tr(b,n,B,(120.4,43),(120.4,51));via(b,n,(120.4,51))
 n=b.FindNet('RTL_1V1');tr(b,n,F,(82.8,58.05),(82.8,56.8));tr(b,n,F,(82.8,56.8),(83.5,56.8));via(b,n,(83.5,56.8));tr(b,n,B,(83.5,56.8),(83.5,45));via(b,n,(83.5,45));tr(b,n,F,(83.5,45),(123.4,45));via(b,n,(123.4,45));tr(b,n,B,(123.4,45),(123.4,51));via(b,n,(123.4,51))
 n=b.FindNet('RTL_5V');tr(b,n,F,(83.95,59.2),(85,59.2));via(b,n,(85,59.2));tr(b,n,B,(85,59.2),(85,47));via(b,n,(85,47));tr(b,n,F,(85,47),(126.4,47));via(b,n,(126.4,47));tr(b,n,B,(126.4,47),(126.4,51));via(b,n,(126.4,51))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
