"""V313: RTL_5V perimeter escape, avoiding the dense QFN upper field."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL5V_ROUTE_V313.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_5V')
 # Each QFN pad gets a short F.Cu escape, then the rail uses a remote B.Cu perimeter.
 s(b,n,F,(95.2,58.05),(91.0,58.05));v(b,n,(91.0,58.05));s(b,n,B,(91.0,58.05),(91.0,82.0))
 s(b,n,F,(101.95,58.8),(104.0,58.8));v(b,n,(104.0,58.8));s(b,n,B,(104.0,58.8),(104.0,82.0))
 s(b,n,B,(91.0,82.0),(116.4,82.0));v(b,n,(116.4,82.0));s(b,n,F,(116.4,82.0),(116.4,61.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
