"""V319: corrected native endpoints for the coordinated In2 rail trial."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_COORDINATED_RAILS_V319.kicad_pcb'
F,L=pcbnew.F_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,pcbnew.B_Cu);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 # Rail endpoints are deliberately off-pad; the only inner-layer tracks are power nets.
 n=b.FindNet('RTL_5V');s(b,n,F,(95.2,58.05),(93,58.05));v(b,n,(93,58.05));s(b,n,L,(93,58.05),(103,57));s(b,n,L,(103,57),(116.4,62));v(b,n,(116.4,62));s(b,n,F,(116.4,62),(116.4,61))
 n=b.FindNet('RTL_1V1');s(b,n,F,(94.05,59.2),(92.8,59.2));v(b,n,(92.8,59.2));s(b,n,L,(92.8,59.2),(105,72.5));s(b,n,L,(105,72.5),(105.2,51.5));v(b,n,(105.2,51.5));s(b,n,F,(105.2,51.5),(105.2,53))
 n=b.FindNet('RTL_3V3');s(b,n,F,(85.7,70),(83.5,70));v(b,n,(83.5,70));s(b,n,L,(83.5,70),(94.8,67.5));v(b,n,(94.8,67.5));s(b,n,F,(94.8,67.5),(94.8,65.95));s(b,n,F,(94.7,63.5),(94.8,65.95))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
