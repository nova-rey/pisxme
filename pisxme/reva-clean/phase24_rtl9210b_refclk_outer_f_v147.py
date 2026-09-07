"""V147: outer REFCLK F.Cu corridors with separated J1-side drops."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SSD33_ON_V143_V144.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_REFCLK_OUTER_F_V147.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));p=b.FindNet('REFCLK_P');n=b.FindNet('REFCLK_N')
 tr(b,p,F,(98.4,73.95),(98.4,71.9));tr(b,p,F,(98.4,71.9),(137.75,71.9));via(b,p,(137.75,71.9));tr(b,p,B,(137.75,71.9),(137.75,62.725));via(b,p,(137.75,62.725));tr(b,p,F,(137.75,62.725),(137.25,62.725))
 tr(b,n,F,(98.8,73.95),(98.8,72.4));tr(b,n,F,(98.8,72.4),(136.25,72.4));via(b,n,(136.25,72.4));tr(b,n,B,(136.25,72.4),(136.25,62.0));via(b,n,(136.25,62.0));tr(b,n,F,(136.25,62.0),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
