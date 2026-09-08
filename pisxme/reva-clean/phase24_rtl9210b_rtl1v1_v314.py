"""V314: RTL_1V1 lower-perimeter collector trial from V311."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL1V1_ROUTE_V314.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
 # Left-side QFN pads escape to isolated B.Cu verticals.
 for y in (59.2,60.8,64.8):
  s(b,n,F,(94.05,y),(92.8,y));v(b,n,(92.8,y));s(b,n,B,(92.8,y),(92.8,84.0))
 # Bottom-edge pads use vertical F.Cu dogbones to B.Cu below the existing field.
 for x in (96.0,98.0,99.2):
  s(b,n,F,(x,65.95),(x,76.0));v(b,n,(x,76.0));s(b,n,B,(x,76.0),(x,84.0))
 for x in (92.8,96.0,98.0,99.2): s(b,n,B,(x,84.0),(110.0,84.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
