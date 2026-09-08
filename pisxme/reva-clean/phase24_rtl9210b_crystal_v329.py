"""V329: crystal support route on the V323 coherent placement."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_COHERENT_REORIENT_V323.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_ROUTE_V329.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE)); ni=b.FindNet('XTAL_IN');no=b.FindNet('XTAL_OUT')
 # XTAL_IN: U1.53 -> remote B.Cu spine -> Y1.1/C1.1.
 s(b,ni,F,(109.95,64.8),(112.0,64.8));v(b,ni,(112.0,64.8));s(b,ni,B,(112.0,64.8),(112.0,51.0));v(b,ni,(104.3,51.0));s(b,ni,B,(112.0,51.0),(104.3,51.0));s(b,ni,F,(104.3,51.0),(104.3,53.0));s(b,ni,F,(104.3,53.0),(109.1,53.0))
 # XTAL_OUT: separate B.Cu spine and a west-side Y1.2 -> C2.1 branch.
 s(b,no,F,(109.95,64.4),(113.5,64.4));v(b,no,(113.5,64.4));s(b,no,B,(113.5,64.4),(113.5,50.0));s(b,no,B,(113.5,50.0),(103.0,50.0));v(b,no,(103.0,50.0));s(b,no,F,(103.0,50.0),(105.7,50.0));s(b,no,F,(105.7,50.0),(105.7,53.0));s(b,no,F,(105.7,53.0),(103.0,53.0));s(b,no,F,(103.0,53.0),(103.0,55.0));s(b,no,F,(103.0,55.0),(104.4,55.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
