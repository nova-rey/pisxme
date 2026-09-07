"""V59: clear C3 ground and the RTL_3V3 handoff in the 1V1 sub-primitive."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_3V3_RAIL_JOIN_V52.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_1V1_C4_RIGHT_V59.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
 tr(b,n,F,(101.95,67.2),(102.8,67.2));vi(b,n,(102.8,67.2))
 tr(b,n,B,(102.8,67.2),(108.0,67.2));tr(b,n,B,(108.0,67.2),(108.0,70.5));tr(b,n,B,(108.0,70.5),(113.8,70.5));tr(b,n,B,(113.8,70.5),(113.8,69.0));vi(b,n,(113.8,69.0));tr(b,n,F,(113.8,69.0),(113.4,69.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
