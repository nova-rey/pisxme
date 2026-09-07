"""V74: isolated RTL_1V1 U1.50 upper B.Cu corridor to C4.1."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_1V1_TOP25_V63.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_1V1_LEFT50_V74.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
 tr(b,n,F,(94.05,72.8),(92.8,72.8));vi(b,n,(92.8,72.8));tr(b,n,B,(92.8,72.8),(92.8,66.5));tr(b,n,B,(92.8,66.5),(112.5,66.5));tr(b,n,B,(112.5,66.5),(112.5,69.0));tr(b,n,B,(112.5,69.0),(113.8,69.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
