"""Complete the two remaining SPI channels on the V24 source baseline."""
from pathlib import Path
import pcbnew

HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_90_MIXED_V24.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_ROTATE_U1_90_COMPLETE_SPI_V25.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 n=b.FindNet('SPISO');t(b,n,F,(99.2,66.05),(99.2,58.5));t(b,n,F,(99.2,58.5),(83,58.5));t(b,n,F,(83,58.5),(83,80))
 n=b.FindNet('SPICS');t(b,n,F,(98.8,66.05),(98.8,60.0));v(b,n,(98.8,60.0));t(b,n,B,(98.8,60.0),(81.8,60.0));t(b,n,B,(81.8,60.0),(81.8,78.0));v(b,n,(81.8,78.0));t(b,n,F,(81.8,78.0),(81.8,80.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
