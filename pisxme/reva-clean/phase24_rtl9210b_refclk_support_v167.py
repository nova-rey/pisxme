"""V167: pad-aware REFCLK dogbones, then an upper B.Cu QFN-to-J1 span."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_LOWER_1V1_HANDOFF_V160.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_V167.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
NARROW=.13208
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=.2):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a,d=.30,w=.60):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(w));q.SetDrill(pcbnew.FromMM(d));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));p,n=b.FindNet('REFCLK_P'),b.FindNet('REFCLK_N')
 # Leave the 0.4-mm QFN row through the gaps between pads 60/61 and 62/63.
 tr(b,p,F,(98.4,73.95),(98.4,74.55),NARROW);tr(b,p,F,(98.4,74.55),(98.2,74.8),NARROW);tr(b,p,F,(98.2,74.8),(97.0,76.0),NARROW);via(b,p,(97.0,76.0))
 tr(b,n,F,(98.8,73.95),(98.8,74.55),NARROW);tr(b,n,F,(98.8,74.55),(99.0,74.8),NARROW);tr(b,n,F,(99.0,74.8),(102.0,76.0),NARROW);via(b,n,(102.0,76.0))
 # Rise outside the QFN/XTAL field, stay north of the J1 sideband row.
 tr(b,p,B,(97.0,76.0),(93.0,66.0));tr(b,p,B,(93.0,66.0),(137.25,66.0));via(b,p,(137.25,62.725));tr(b,p,F,(137.25,62.725),(137.25,62.725))
 tr(b,n,B,(102.0,76.0),(102.0,66.8));tr(b,n,B,(102.0,66.8),(136.75,66.8));via(b,n,(136.75,62.725));tr(b,n,F,(136.75,62.725),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
