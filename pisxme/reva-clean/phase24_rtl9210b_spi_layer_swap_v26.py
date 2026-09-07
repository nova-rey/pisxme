"""Layer-swap SPISO/SPISO3 and add SPICS on the V24 source baseline."""
from pathlib import Path
import pcbnew

HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_90_MIXED_V24.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_ROTATE_U1_90_LAYER_SWAP_V26.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def remove(b,name):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
def main():
 b=pcbnew.LoadBoard(str(BASE));remove(b,'SPISO3')
 n=b.FindNet('SPISO3');t(b,n,F,(99.6,66.05),(99.6,60.8));t(b,n,F,(99.6,60.8),(100.0,60.8));v(b,n,(100.0,60.8));t(b,n,B,(100.0,60.8),(89,60.8));t(b,n,B,(89,60.8),(89,78));v(b,n,(89,78));t(b,n,F,(89,78),(89,80))
 n=b.FindNet('SPISO');t(b,n,F,(99.2,66.05),(99.2,58.5));t(b,n,F,(99.2,58.5),(83,58.5));t(b,n,F,(83,58.5),(83,80))
 n=b.FindNet('SPICS');t(b,n,F,(98.8,66.05),(98.8,57.5));v(b,n,(98.8,57.5));t(b,n,B,(98.8,57.5),(81.8,57.5));t(b,n,B,(81.8,57.5),(81.8,78));v(b,n,(81.8,78));t(b,n,F,(81.8,78),(81.8,80))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
