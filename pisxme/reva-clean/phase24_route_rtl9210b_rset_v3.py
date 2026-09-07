#!/usr/bin/env python3
"""Path-B disposable: route RSET around the crystal field on B.Cu."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RSET_V3.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(x,y)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RSET')
 seg(b,n,F,(69.4,51.0),(69.4,52.0)); via(b,n,69.4,52.0)
 for a,z in [((69.4,52.0),(69.4,53.0)),((69.4,53.0),(76.5,53.0)),((76.5,53.0),(76.5,57.0))]: seg(b,n,B,a,z)
 via(b,n,76.5,57.0); seg(b,n,F,(76.5,57.0),(76.8,58.05))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
