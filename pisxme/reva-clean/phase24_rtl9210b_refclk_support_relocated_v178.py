"""V178: west-side crystal/RSET cluster with regenerated native-pad routes."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent; BASE=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V174.kicad_pcb'; OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V178.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=.13208
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=W):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def move(b,ref,x,y):
 f=b.FindFootprintByReference(ref);q=f.GetPosition();f.SetPosition(pcbnew.VECTOR2I_MM(float(x),float(y)))
def main():
 b=pcbnew.LoadBoard(str(BASE))
 # Open west pocket: Y1, C1/C2, and RSET support are moved coherently.
 move(b,'Y1',90.,63.);move(b,'C1',87.,63.);move(b,'C2',92.,63.);move(b,'R1',89.,66.)
 xi,xo,rs=b.FindNet('XTAL_IN'),b.FindNet('XTAL_OUT'),b.FindNet('RSET')
 tr(b,xi,F,(95.2,65.95),(94.5,67.0));via(b,xi,(94.5,67.0));tr(b,xi,B,(94.5,67.0),(90.0,64.0));via(b,xi,(90.0,64.0));tr(b,xi,F,(90.0,64.0),(89.3,63.0));tr(b,xi,F,(89.3,63.0),(87.6,63.0))
 tr(b,xo,F,(95.6,65.95),(96.0,68.0));via(b,xo,(96.0,68.0));tr(b,xo,B,(96.0,68.0),(91.2,64.8));via(b,xo,(91.2,64.8));tr(b,xo,F,(91.2,64.8),(90.7,63.0));tr(b,xo,F,(90.7,63.0),(91.4,63.0))
 tr(b,rs,F,(94.05,65.2),(93.5,66.0));via(b,rs,(93.5,66.0));tr(b,rs,B,(93.5,66.0),(89.0,66.0));via(b,rs,(89.0,66.0));tr(b,rs,F,(89.0,66.0),(88.4,66.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
