"""V170: move only the REFCLK upper span to F.Cu over the B.Cu CLKREQ trunk."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent; BASE=HERE/'PHASE24_RTL9210B_LOWER_1V1_HANDOFF_V160.kicad_pcb'; OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_V170.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=.13208
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=W):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));p,n=b.FindNet('REFCLK_P'),b.FindNet('REFCLK_N')
 # Measured pad-gap dogbones, then leave the XTAL/1V1 field on the outer F.Cu.
 tr(b,p,F,(98.4,73.95),(98.4,74.55));tr(b,p,F,(98.4,74.55),(98.2,74.8));tr(b,p,F,(98.2,74.8),(97.0,76.0));tr(b,p,F,(97.0,76.0),(90.0,76.0));via(b,p,(90.0,76.0));tr(b,p,B,(90.0,76.0),(90.0,62.8));via(b,p,(90.0,62.8));tr(b,p,F,(90.0,62.8),(138.5,62.8));tr(b,p,F,(138.5,62.8),(138.5,61.0));via(b,p,(138.5,61.0));tr(b,p,F,(138.5,61.0),(137.25,62.725))
 tr(b,n,F,(98.8,73.95),(98.8,74.55));tr(b,n,F,(98.8,74.55),(99.0,74.8));tr(b,n,F,(99.0,74.8),(102.0,76.0));tr(b,n,F,(102.0,76.0),(120.0,76.0));via(b,n,(120.0,76.0));tr(b,n,B,(120.0,76.0),(120.0,63.5));via(b,n,(120.0,63.5));tr(b,n,F,(120.0,63.5),(136.75,63.5));tr(b,n,F,(136.75,63.5),(136.75,61.0));via(b,n,(136.75,61.0));tr(b,n,F,(136.75,61.0),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
