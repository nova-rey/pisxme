"""V179: clean west crystal cluster plus one authoritative REFCLK route."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent; BASE=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V174.kicad_pcb'; OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V179.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=.13208
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=W):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def move(b,ref,x,y): b.FindFootprintByReference(ref).SetPosition(pcbnew.VECTOR2I_MM(float(x),float(y)))
def remove_net(b,name):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for net in ('REFCLK_P','REFCLK_N','XTAL_IN','XTAL_OUT','RSET'):remove_net(b,net)
 move(b,'Y1',88.,60.);move(b,'C1',85.5,60.);move(b,'C2',90.5,60.);move(b,'R1',88.,63.)
 xi,xo,rs=b.FindNet('XTAL_IN'),b.FindNet('XTAL_OUT'),b.FindNet('RSET')
 tr(b,xi,F,(95.2,65.95),(94.5,67.0));via(b,xi,(94.5,67.0));tr(b,xi,B,(94.5,67.0),(87.8,61.0));via(b,xi,(87.8,61.0));tr(b,xi,F,(87.8,61.0),(87.3,60.0));tr(b,xi,F,(87.3,60.0),(86.1,60.0))
 tr(b,xo,F,(95.6,65.95),(95.0,68.0));via(b,xo,(95.0,68.0));tr(b,xo,B,(95.0,68.0),(89.2,61.5));via(b,xo,(89.2,61.5));tr(b,xo,F,(89.2,61.5),(88.7,60.0));tr(b,xo,F,(88.7,60.0),(89.9,60.0))
 tr(b,rs,F,(94.05,65.2),(93.5,64.0));via(b,rs,(93.5,64.0));tr(b,rs,B,(93.5,64.0),(87.5,63.0));via(b,rs,(87.5,63.0));tr(b,rs,F,(87.5,63.0),(87.4,63.0))
 p,n=b.FindNet('REFCLK_P'),b.FindNet('REFCLK_N')
 tr(b,p,F,(98.4,65.95),(98.2,66.8));via(b,p,(98.2,66.8));tr(b,p,B,(98.2,66.8),(98.2,60.0));tr(b,p,B,(98.2,60.0),(138.5,60.0));via(b,p,(138.5,60.0));tr(b,p,F,(138.5,60.0),(137.25,62.725))
 tr(b,n,F,(98.8,65.95),(99.0,66.8));via(b,n,(99.0,66.8));tr(b,n,B,(99.0,66.8),(99.0,60.8));tr(b,n,B,(99.0,60.8),(136.75,60.8));via(b,n,(136.75,60.8));tr(b,n,F,(136.75,60.8),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
