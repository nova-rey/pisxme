#!/usr/bin/env python3
"""Disposable Path-B route: V6 source escape with lateral destination fanout."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_V6_LATERAL_SUPPORT_PLACEMENT_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_V6_LATERAL_SPI_V3.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def route(b,name,s,bend,spine,last,target):
 n=b.FindNet(name);tr(b,n,F,s,bend);via(b,n,bend);p=bend
 for z in spine:tr(b,n,B,p,z);p=z
 via(b,n,p);tr(b,n,F,p,target)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 route(b,'SPICS',(83.95,62.8),(86,61),[(86,61),(110.8,61)],(110.8,61),(110.8,58))
 route(b,'SPISO',(83.95,63.2),(87,62),[(87,62),(112,62)],(112,62),(112,58))
 route(b,'SPISO3',(83.95,63.6),(88,63),[(88,63),(118,63)],(118,63),(118,58))
 route(b,'SPICLK',(83.95,64.8),(89,64.8),[(89,64.8),(116.8,64.8)],(116.8,64.8),(116.8,58))
 n=b.FindNet('SPISI');tr(b,n,F,(83.95,65.2),(85.5,70));tr(b,n,F,(85.5,70),(115.6,70));tr(b,n,F,(115.6,70),(115.6,58))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
