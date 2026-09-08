"""V301: transplant the previously validated CLKREQ sideband topology."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_ROUTE_V300.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CLKREQ_ROUTE_V301.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.25));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('CLKREQ_N')
 tr(b,n,F,(93.4,53),(92,48));tr(b,n,F,(92,48),(92,42));via(b,n,(92,42));tr(b,n,B,(92,42),(75,42));tr(b,n,B,(75,42),(75,69.5));tr(b,n,B,(75,69.5),(102.4,69.5));via(b,n,(102.4,69.5));tr(b,n,F,(102.4,69.5),(103.5,69.5));via(b,n,(103.5,69.5));tr(b,n,F,(103.5,69.5),(105.5,69.5));via(b,n,(105.5,69.5));tr(b,n,B,(105.5,69.5),(137.5,69.5));via(b,n,(137.5,69.5));tr(b,n,F,(137.5,69.5),(136.5,70.275));via(b,n,(102.4,61));tr(b,n,B,(102.4,61),(102.4,69.5));tr(b,n,F,(101.95,60.4),(102.4,61))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
