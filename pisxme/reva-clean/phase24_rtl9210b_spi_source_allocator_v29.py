"""Upper-envelope allocator for the three remaining RTL9210B SPI channels."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_90_MIXED_V24.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SPI_SOURCE_ALLOCATOR_V29.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def rm(b,name):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for name in ('SPISO3','SPISO','SPICS'):rm(b,name)
 n=b.FindNet('SPISO3');t(b,n,F,(99.6,66.05),(99.6,60.0));v(b,n,(99.6,60.0));t(b,n,B,(99.6,60.0),(89.0,60.0));t(b,n,B,(89.0,60.0),(89.0,78.0));v(b,n,(89.0,78.0));t(b,n,F,(89.0,78.0),(89.0,80.0))
 n=b.FindNet('SPISO');t(b,n,F,(99.2,66.05),(99.2,58.5));v(b,n,(99.2,58.5));t(b,n,B,(99.2,58.5),(83.0,58.5));t(b,n,B,(83.0,58.5),(83.0,78.0));v(b,n,(83.0,78.0));t(b,n,F,(83.0,78.0),(83.0,80.0))
 n=b.FindNet('SPICS');t(b,n,F,(98.8,66.05),(98.8,57.0));v(b,n,(98.8,57.0));t(b,n,B,(98.8,57.0),(81.8,57.0));t(b,n,B,(81.8,57.0),(81.8,78.0));v(b,n,(81.8,78.0));t(b,n,F,(81.8,78.0),(81.8,80.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
