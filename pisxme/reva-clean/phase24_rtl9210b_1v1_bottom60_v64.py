"""V64: isolated RTL_1V1 U1.60 bottom-edge to the C4.1 corridor."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_1V1_TOP25_V63.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_1V1_BOTTOM60_V64.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
 tr(b,n,F,(98.0,73.95),(98.0,76.5));vi(b,n,(98.0,76.5));tr(b,n,B,(98.0,76.5),(103.0,76.5));tr(b,n,B,(103.0,76.5),(103.0,77.5));tr(b,n,B,(103.0,77.5),(108.5,77.5));tr(b,n,B,(108.5,77.5),(108.5,77.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
