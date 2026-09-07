"""V33: B.Cu long-span XTAL/RSET support handoff on the V31 allocator."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SPI_SOURCE_ALLOCATOR_V31.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SPI_SOURCE_ALLOCATOR_SUPPORT_V33.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 n=b.FindNet('XTAL_IN');t(b,n,F,(95.2,73.95),(95.2,75.5));v(b,n,(95.2,75.5));t(b,n,B,(95.2,75.5),(104.3,75.5));v(b,n,(104.3,75.5));t(b,n,F,(104.3,75.5),(104.3,72.8));t(b,n,F,(104.3,72.8),(105.6,75.0))
 n=b.FindNet('XTAL_OUT');t(b,n,F,(95.6,73.95),(95.6,76.5));v(b,n,(95.6,76.5));t(b,n,B,(95.6,76.5),(105.7,76.5));v(b,n,(105.7,76.5));t(b,n,F,(105.7,76.5),(105.7,72.8));t(b,n,F,(105.7,72.8),(107.4,75.0))
 n=b.FindNet('RSET');t(b,n,F,(94.05,73.2),(93.0,75.0));v(b,n,(93.0,75.0));t(b,n,B,(93.0,75.0),(104.4,78.0));v(b,n,(104.4,78.0));t(b,n,F,(104.4,78.0),(104.4,78.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
