#!/usr/bin/env python3
"""V11: V10 with staggered M.2 contact-row dogbone departure heights."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V1.kicad_pcb'
OUT=ROOT/'PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V11.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): q=p.GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(b,n,a,z,l):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def path(b,n,pts,l):
    for a,z in zip(pts,pts[1:]): tr(b,n,a,z,l)
def via(b,n,p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U13'); j=b.FindFootprintByReference('J3')
    specs=[
      ('M2_SATA_A_P_PCIE_TXP0','2','49',(220,153.5),'F',[(175,147.2),(175,132),(190,132),(208,132),(220,153.5)],156.0),
      ('M2_SATA_A_N_PCIE_TXN0','3','47',(218,153.5),'B',[(173.5,147.6),(173.5,136),(192,136),(210,136),(218,153.5)],158.5),
      ('M2_SATA_B_P_PCIE_RXN0','6','41',(214,153.5),'F',[(169,148.8),(169,154),(190,154),(206,154),(214,153.5)],158.5),
      ('M2_SATA_B_N_PCIE_RXP0','7','43',(216,153.5),'B',[(171.5,151),(171.5,165),(206,165),(206,168),(213,168),(216,153.5)],156.0),
    ]
    for name,up,jp,target,layer,pts,depart_y in specs:
        n=b.FindNet(name)
        for item in list(b.GetTracks()):
            if item.GetNetname()==name: b.RemoveNative(item)
        src=xy(u.FindPadByNumber(up)); dst=xy(j.FindPadByNumber(jp)); sx,sy=pts[0]
        if layer=='F': path(b,n,[src,(sx,sy)]+pts[1:],F)
        else:
            if name.endswith('RXP0'): path(b,n,[src,(171.5,149.2),(sx,sy)],F)
            else: path(b,n,[src,(sx,sy)],F)
            via(b,n,(sx,sy)); path(b,n,pts[1:],B)
        via(b,n,target)
        path(b,n,[dst,(dst[0],depart_y),target],F)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
