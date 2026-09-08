"""V292: PEDET transitions before REFCLK and PERST obstacles."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_ROUTE_SPISI_V289.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PEDET_ROUTE_V292.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.25));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('PEDET')
 tr(b,n,F,(90.9,53.0),(88.0,53.0));tr(b,n,F,(88.0,53.0),(88.0,46.0));via(b,n,(88.0,46.0));tr(b,n,B,(88.0,46.0),(106.0,46.0));tr(b,n,B,(106.0,46.0),(106.0,59.5));via(b,n,(106.0,59.5));tr(b,n,F,(106.0,59.5),(106.0,62.4));tr(b,n,F,(106.0,62.4),(101.95,62.4));via(b,n,(106.0,62.4));tr(b,n,B,(106.0,62.4),(139.0,62.4));via(b,n,(139.0,62.4));tr(b,n,F,(139.0,62.4),(140.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
