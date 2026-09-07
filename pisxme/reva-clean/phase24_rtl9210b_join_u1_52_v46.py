"""V46: co-author XTAL_IN transition and U1.52 RTL_3V3 handoff."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_3V3_PARTITIONED_V44.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_JOIN_U1_52_V46.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def rm(b,name):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
def main():
 b=pcbnew.LoadBoard(str(BASE));rm(b,'XTAL_IN')
 n=b.FindNet('XTAL_IN');t(b,n,F,(95.2,73.95),(95.2,75.5));t(b,n,F,(95.2,75.5),(93.2,76.5));v(b,n,(93.2,76.5));t(b,n,B,(93.2,76.5),(107.5,74.0));v(b,n,(107.5,74.0));t(b,n,F,(107.5,74.0),(108.3,75.8));t(b,n,F,(108.3,75.8),(109.6,78.0))
 n=b.FindNet('RTL_3V3');t(b,n,F,(94.8,73.95),(94.8,75.5));t(b,n,F,(94.8,75.5),(94.4,76.0));v(b,n,(94.4,76.0));t(b,n,B,(94.4,76.0),(90.2,75.5));
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
