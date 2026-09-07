"""V51: route R2/R3 3V3 taps through a B.Cu collector."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U1_52_HANDOFF_V49.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_RAIL_JOIN_V51.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
 # Leave the QFN/SPI F.Cu field immediately and collect the rail on B.Cu.
 tr(b,n,F,(90.2,56.0),(89.2,56.0));tr(b,n,F,(89.2,56.0),(89.2,55.0));vi(b,n,(89.2,55.0))
 tr(b,n,F,(93.2,56.0),(92.2,56.0));tr(b,n,F,(92.2,56.0),(92.2,55.0));vi(b,n,(92.2,55.0))
 tr(b,n,B,(89.2,55.0),(92.2,55.0));tr(b,n,B,(92.2,55.0),(100.4,55.0));tr(b,n,B,(100.4,55.0),(100.4,60.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
