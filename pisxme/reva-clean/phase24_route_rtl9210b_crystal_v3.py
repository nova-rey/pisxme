#!/usr/bin/env python3
"""Path-B disposable: dual B.Cu crystal corridors with separated U1 returns."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CRYSTAL_V3.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(x,y)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def route(b,name,items):
 n=b.FindNet(name)
 for l,a,z in items: seg(b,n,l,a,z)
def main():
 b=pcbnew.LoadBoard(str(BASE)); ni=b.FindNet('XTAL_IN'); no=b.FindNet('XTAL_OUT')
 route(b,'XTAL_IN',[(F,(66.4,55),(66.4,53.4)),(F,(66.4,53.4),(69.3,53.4)),(F,(69.3,53.4),(69.3,55)),(F,(69.3,55),(69.3,56.0))])
 via(b,ni,69.3,56.0)
 route(b,'XTAL_IN',[(B,(69.3,56.0),(69.3,57.0)),(B,(69.3,57.0),(73.8,57.0)),(B,(73.8,57.0),(73.8,59.2))])
 via(b,ni,73.8,59.2); seg(b,ni,F,(73.8,59.2),(76.05,59.2))
 route(b,'XTAL_OUT',[(F,(72.4,55),(72.4,54.2)),(F,(72.4,54.2),(70.7,54.2)),(F,(70.7,54.2),(70.7,55)),(F,(70.7,55),(70.7,57.8))])
 via(b,no,70.7,57.8)
 route(b,'XTAL_OUT',[(B,(70.7,57.8),(72.8,57.8)),(B,(72.8,57.8),(72.8,60.6))])
 via(b,no,72.8,60.6)
 route(b,'XTAL_OUT',[(F,(72.8,60.6),(75.2,60.6)),(F,(75.2,60.6),(75.2,59.6)),(F,(75.2,59.6),(76.05,59.6))])
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
