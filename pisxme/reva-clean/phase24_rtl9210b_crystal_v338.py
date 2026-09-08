"""V338: crystal route on the cleared V337 support placement."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_CRYSTAL_RELOCATED_V337.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_ROUTE_V338.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE));ni=b.FindNet('XTAL_IN');no=b.FindNet('XTAL_OUT')
 s(b,ni,F,(109.95,64.8),(112,64.8));v(b,ni,(112,64.8));s(b,ni,B,(112,64.8),(112,47));s(b,ni,B,(112,47),(115.3,47));v(b,ni,(115.3,47));s(b,ni,F,(115.3,47),(115.3,49));s(b,ni,F,(115.3,49),(114.3,49));v(b,ni,(114.3,49));s(b,ni,B,(114.3,49),(114.3,48));s(b,ni,B,(114.3,48),(120.1,48));v(b,ni,(120.1,48));s(b,ni,F,(120.1,48),(120.1,49))
 s(b,no,F,(109.95,64.4),(113.5,64.4));v(b,no,(113.5,64.4));s(b,no,B,(113.5,64.4),(113.5,46));s(b,no,B,(113.5,46),(116.7,46));v(b,no,(116.7,46));s(b,no,F,(116.7,46),(116.7,49));s(b,no,F,(116.7,49),(118,49));v(b,no,(118,49));s(b,no,B,(118,49),(118,50));s(b,no,B,(118,50),(120.4,50));v(b,no,(120.4,50));s(b,no,F,(120.4,50),(120.4,53))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
