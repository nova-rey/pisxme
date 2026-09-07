"""V31: keep SPISO3's B.Cu lane, move its target drop to F.Cu."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SPI_SOURCE_ALLOCATOR_V30.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SPI_SOURCE_ALLOCATOR_V31.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for x in list(b.GetTracks()):
  if x.GetNetname()=='SPISO3':b.RemoveNative(x)
 n=b.FindNet('SPISO3')
 t(b,n,F,(99.6,66.05),(99.6,60));t(b,n,F,(99.6,60),(100.2,60));v(b,n,(100.2,60));t(b,n,B,(100.2,60),(90.5,60));v(b,n,(90.5,60));t(b,n,F,(90.5,60),(89,61));t(b,n,F,(89,61),(89,80))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
