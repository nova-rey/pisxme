"""V315: local RTL_3V3 bridge-field trial from V311."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL3V3_ROUTE_V315.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
 # Bridge U2's separated supply pads on B.Cu, then hand off to U1.52.
 s(b,n,F,(85.7,70.0),(84.5,72.0));v(b,n,(84.5,72.0))
 s(b,n,B,(84.5,72.0),(91.7,72.0));v(b,n,(91.7,72.0));s(b,n,F,(91.7,72.0),(91.7,70.0))
 s(b,n,B,(91.7,72.0),(93.0,72.0));v(b,n,(93.0,72.0));s(b,n,F,(93.0,72.0),(94.8,65.95))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
