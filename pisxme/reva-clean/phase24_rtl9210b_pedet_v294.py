"""V294: PEDET east-side U1.8 landing around PERST/CLKREQ."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_ROUTE_SPISI_V289.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PEDET_ROUTE_V294.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.25));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('PEDET')
 tr(b,n,F,(90.9,53),(88,53));tr(b,n,F,(88,53),(88,46));via(b,n,(88,46));tr(b,n,B,(88,46),(106,46));tr(b,n,B,(106,46),(106,59.5));via(b,n,(106,59.5));tr(b,n,F,(106,59.5),(102.6,59.5));tr(b,n,F,(102.6,59.5),(102.6,62.4));tr(b,n,F,(102.6,62.4),(101.95,62.4));via(b,n,(106,62.4));tr(b,n,B,(106,62.4),(139,62.4));via(b,n,(139,62.4));tr(b,n,F,(139,62.4),(140.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
