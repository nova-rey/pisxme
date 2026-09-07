"""V159: REFCLK after V158 crystal relocation; N uses a short B.Cu source jog."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_XTAL_IN_INNER_ENDPOINT_V158.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_REFCLK_AFTER_XTAL_V159.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));p=b.FindNet('REFCLK_P');n=b.FindNet('REFCLK_N')
 tr(b,p,F,(98.4,73.95),(98.4,74.6));tr(b,p,F,(98.4,74.6),(137.75,74.6));via(b,p,(137.75,74.6));tr(b,p,B,(137.75,74.6),(137.75,62.725));via(b,p,(137.75,62.725));tr(b,p,F,(137.75,62.725),(137.25,62.725))
 tr(b,n,F,(98.8,73.95),(98.8,75.0));via(b,n,(98.8,75.0));tr(b,n,B,(98.8,75.0),(98.8,74.0));tr(b,n,B,(98.8,74.0),(104.5,74.0));via(b,n,(104.5,74.0));tr(b,n,F,(104.5,74.0),(136.25,74.0));via(b,n,(136.25,74.0));tr(b,n,B,(136.25,74.0),(136.25,62.0));via(b,n,(136.25,62.0));tr(b,n,F,(136.25,62.0),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
