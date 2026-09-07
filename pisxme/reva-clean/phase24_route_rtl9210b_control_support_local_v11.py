#!/usr/bin/env python3
"""Path-B V11: move only the PEDET upper return below the V6 RTL_5V via."""
from pathlib import Path
import pcbnew

HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V11.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z,l):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l)
    t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def path(b,n,pts,l):
    for a,z in zip(pts,pts[1:]): tr(b,n,a,z,l)
def via(b,n,p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.6));
    v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('PEDET')
    for item in list(b.GetTracks()):
        if item.GetNetname()=='PEDET': b.RemoveNative(item)
    # Keep the QFN/source and local pull-up escape, but move only the upper
    # F.Cu return from y=40.6 to y=39.5 so it clears the RTL_5V via at 85,41.
    path(b,n,[(79.6,65.95),(79.6,68.5)],F); via(b,n,(79.6,68.5))
    path(b,n,[(79.6,68.5),(68,68.5),(68,48)],B); via(b,n,(68,48))
    path(b,n,[(68,48),(71,48)],F); path(b,n,[(68,48),(68,43)],B); via(b,n,(68,43))
    path(b,n,[(68,43),(68,39.5),(144,39.5),(144,61.5),(140.75,61.5),(140.75,62.725)],F)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
