"""V330: separated crystal source escapes on the V323 placement."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_COHERENT_REORIENT_V323.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_ROUTE_V330.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE));ni=b.FindNet('XTAL_IN');no=b.FindNet('XTAL_OUT')
 # Separate U1 source departures before entering the shared support area.
 s(b,ni,F,(109.95,64.8),(108.0,64.8));v(b,ni,(108.0,64.8));s(b,ni,B,(108.0,64.8),(112.0,51.0));v(b,ni,(104.3,51.0));s(b,ni,B,(112.0,51.0),(104.3,51.0));s(b,ni,F,(104.3,51.0),(104.3,53.0));s(b,ni,F,(104.3,53.0),(109.1,53.0))
 s(b,no,F,(109.95,64.4),(113.5,64.4));v(b,no,(113.5,64.4));s(b,no,B,(113.5,64.4),(105.7,54.0));v(b,no,(105.7,54.0));s(b,no,F,(105.7,54.0),(105.7,53.0));s(b,no,B,(105.7,54.0),(103.0,54.0));v(b,no,(103.0,54.0));s(b,no,F,(103.0,54.0),(103.0,55.0));s(b,no,F,(103.0,55.0),(104.4,55.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
