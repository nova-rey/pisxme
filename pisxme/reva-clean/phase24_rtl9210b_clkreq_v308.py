"""V308: clear the final R3/XTAL_IN departure intersection."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_ROUTE_V300.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CLKREQ_ROUTE_V308.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.25));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('CLKREQ_N')
 tr(b,n,F,(93.4,53),(93.4,52.5));tr(b,n,F,(93.4,52.5),(98.2,52.5));tr(b,n,F,(98.2,52.5),(98.2,45));via(b,n,(98.2,45));tr(b,n,B,(98.2,45),(80,45));via(b,n,(80,45));tr(b,n,F,(80,45),(80,74));via(b,n,(80,74));tr(b,n,B,(80,74),(103.2,74));via(b,n,(103.2,74));tr(b,n,F,(103.2,74),(105.5,74));via(b,n,(105.5,74));tr(b,n,B,(105.5,74),(137.5,74));via(b,n,(137.5,74));tr(b,n,F,(137.5,74),(136.5,70.275));tr(b,n,F,(101.95,60.4),(102.8,60.4));tr(b,n,F,(102.8,60.4),(102.8,61.5));via(b,n,(102.8,61.5));tr(b,n,B,(102.8,61.5),(102.8,74))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
