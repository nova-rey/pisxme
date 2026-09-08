"""V310: split R3 CLKREQ trunk around SPISI and PEDET B.Cu lanes."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_ROUTE_V300.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CLKREQ_ROUTE_V310.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.25));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('CLKREQ_N')
 tr(b,n,F,(93.4,53),(93.4,55));via(b,n,(93.4,55));tr(b,n,B,(93.4,55),(93.4,48.5));via(b,n,(93.4,48.5));tr(b,n,F,(93.4,48.5),(93.4,45));via(b,n,(93.4,45));tr(b,n,B,(93.4,45),(80,45));via(b,n,(80,45));tr(b,n,F,(80,45),(80,74));via(b,n,(80,74));tr(b,n,B,(80,74),(103.2,74));via(b,n,(103.2,74));tr(b,n,F,(103.2,74),(105.5,74));via(b,n,(105.5,74));tr(b,n,B,(105.5,74),(137.5,74));via(b,n,(137.5,74));tr(b,n,F,(137.5,74),(136.5,70.275));tr(b,n,F,(101.95,60.4),(102.8,60.4));tr(b,n,F,(102.8,60.4),(102.8,61.5));via(b,n,(102.8,61.5));tr(b,n,B,(102.8,61.5),(102.8,74))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
