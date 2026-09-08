"""V335: corrected outside-spine XTAL_OUT/C2 return."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_COHERENT_REORIENT_V323.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_ROUTE_V335.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE));ni=b.FindNet('XTAL_IN');no=b.FindNet('XTAL_OUT')
 s(b,ni,F,(109.95,64.8),(108,64.8));v(b,ni,(108,64.8));s(b,ni,B,(108,64.8),(108,51));s(b,ni,B,(108,51),(104.3,51));v(b,ni,(104.3,51));s(b,ni,F,(104.3,51),(104.3,54));v(b,ni,(104.3,54));s(b,ni,B,(104.3,54),(109.1,54));v(b,ni,(109.1,54));s(b,ni,F,(109.1,54),(109.1,53))
 s(b,no,F,(109.95,64.4),(113.5,64.4));v(b,no,(113.5,64.4));s(b,no,B,(113.5,64.4),(113.5,50));s(b,no,B,(113.5,50),(105.7,50));v(b,no,(105.7,50));s(b,no,F,(105.7,50),(105.7,53));s(b,no,F,(105.7,53),(111,53));v(b,no,(111,53));s(b,no,B,(111,53),(111,55));v(b,no,(111,55));s(b,no,F,(111,55),(104.4,56));s(b,no,F,(104.4,56),(104.4,55))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
