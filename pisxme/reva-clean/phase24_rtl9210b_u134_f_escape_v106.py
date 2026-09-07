"""V106: keep the U1.34 departure on F.Cu until above the SPI channels."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U136_RIGHT_ESCAPE_V102.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U134_F_ESCAPE_V106.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
 tr(b,n,F,(94.8,66.05),(93.6,66.05));tr(b,n,F,(93.6,66.05),(93.6,62.0));via(b,n,(93.6,62.0))
 tr(b,n,B,(93.6,62.0),(98.8,62.0));tr(b,n,B,(98.8,62.0),(98.8,61.2));tr(b,n,B,(98.8,61.2),(100.4,61.2));tr(b,n,B,(100.4,61.2),(100.4,60.8));via(b,n,(100.4,60.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
