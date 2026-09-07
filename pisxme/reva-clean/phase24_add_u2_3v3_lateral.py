#!/usr/bin/env python3
"""Disposable completion of the relocated U2 RTL_3V3 rail landing."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RAIL_ONLY_LATERAL_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RAIL_ONLY_LATERAL_U2_V2.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
 tr(b,n,B,(120.4,43),(134.2,43))
 # U2.3 is jogged around the nearby C5 ground pad; U2.8 can use a direct
 # vertical landing.  Both branches remain on the named 3V3 net.
 via(b,n,(129.5,43));tr(b,n,F,(129.5,43),(129.5,55));tr(b,n,F,(129.5,55),(128.2,58))
 via(b,n,(134.2,43));tr(b,n,F,(134.2,43),(134.2,58))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
