"""V35: in-board support-cluster translation with separated U1 handoffs."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SPI_SOURCE_ALLOCATOR_V31.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for ref in ('Y1','C1','C2','R1'):
  f=b.FindFootprintByReference(ref);p=f.GetPosition();f.SetPosition(P(p.x/1e6+4,p.y/1e6+3))
 n=b.FindNet('XTAL_IN');t(b,n,F,(95.2,73.95),(95.2,75.5));t(b,n,F,(95.2,75.5),(94.4,76.0));v(b,n,(94.4,76.0));t(b,n,B,(94.4,76.0),(107.5,75.0));v(b,n,(107.5,75.0));t(b,n,F,(107.5,75.0),(108.3,75.8));t(b,n,F,(108.3,75.8),(109.6,78.0))
 n=b.FindNet('XTAL_OUT');t(b,n,F,(95.6,73.95),(95.6,77.0));t(b,n,F,(95.6,77.0),(96.4,77.0));v(b,n,(96.4,77.0));t(b,n,B,(96.4,77.0),(110.5,76.8));v(b,n,(110.5,76.8));t(b,n,F,(110.5,76.8),(109.7,75.8));t(b,n,F,(109.7,75.8),(111.4,78.0))
 n=b.FindNet('RSET');t(b,n,F,(94.05,73.2),(91.0,78.0));v(b,n,(91.0,78.0));t(b,n,B,(91.0,78.0),(107.6,80.2));v(b,n,(107.6,80.2));t(b,n,F,(107.6,80.2),(108.4,81.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
