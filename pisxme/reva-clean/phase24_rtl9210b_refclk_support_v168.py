"""V168: pad-gap QFN escape with outboard J1 transitions."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent; BASE=HERE/'PHASE24_RTL9210B_LOWER_1V1_HANDOFF_V160.kicad_pcb'; OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_V168.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=.13208
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=W):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));p,n=b.FindNet('REFCLK_P'),b.FindNet('REFCLK_N')
 tr(b,p,F,(98.4,73.95),(98.4,74.55));tr(b,p,F,(98.4,74.55),(98.2,74.8));tr(b,p,F,(98.2,74.8),(97.0,76.0));via(b,p,(97.0,76.0))
 tr(b,n,F,(98.8,73.95),(98.8,74.55));tr(b,n,F,(98.8,74.55),(99.0,74.8));tr(b,n,F,(99.0,74.8),(102.0,76.0));via(b,n,(102.0,76.0))
 tr(b,p,B,(97.0,76.0),(93.0,64.5));tr(b,p,B,(93.0,64.5),(138.5,64.5));tr(b,p,B,(138.5,64.5),(138.5,61.0));via(b,p,(138.5,61.0));tr(b,p,F,(138.5,61.0),(137.25,62.725))
 tr(b,n,B,(102.0,76.0),(102.0,66.0));tr(b,n,B,(102.0,66.0),(136.75,66.0));tr(b,n,B,(136.75,66.0),(136.75,61.0));via(b,n,(136.75,61.0));tr(b,n,F,(136.75,61.0),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
