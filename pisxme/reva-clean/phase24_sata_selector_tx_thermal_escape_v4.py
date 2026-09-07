#!/usr/bin/env python3
"""Path-A disposable V4: re-author only selector TX launches around U13 pad 43."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_STORAGE_SATA_SELECTOR_MINIMAL_V3_20260907.kicad_pcb'
OUT=ROOT/'PHASE24_STORAGE_SATA_SELECTOR_TX_THERMAL_ESCAPE_V4.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(.20)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def xy(p):
    q=p.GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def net(b,name):
    n=b.FindNet(name)
    if not n: raise RuntimeError(name)
    return n
def track(b,n,a,z,l):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def path(b,n,pts,l):
    for a,z in zip(pts,pts[1:]): track(b,n,a,z,l)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def main():
    b=pcbnew.LoadBoard(str(BASE))
    names={
      'TXP':'M2_SATA_A_P_PCIE_TXP0',
      'TXN':'M2_SATA_A_N_PCIE_TXN0',
    }
    for n in names.values():
        nn=net(b,n)
        for item in list(b.GetTracks()):
            if item.GetNetname()==n: b.RemoveNative(item)
    # Keep the pair ordered and leave the U13 exposed/side ground pads clear.
    routes={
      'TXP':('2','49',(176.5,147.2),[(176.5,147.2),(190,136),(210,136),(222.75,153.5)]),
      'TXN':('3','47',(176.5,147.8),[(176.5,147.8),(190,140),(210,140),(222.25,153.5)]),
    }
    for key,(up,jp,sv,bc) in routes.items():
        n=net(b,names[key]); src=xy(pad(b,'U13',up)); dst=xy(pad(b,'J3',jp))
        path(b,n,[src,(177.2,src[1]),sv],F); via(b,n,sv)
        path(b,n,[sv]+bc[1:],B); via(b,n,bc[-1]); path(b,n,[bc[-1],dst],F)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
