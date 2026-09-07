"""V53: pad-oriented RTL_5V escape from corrected U1 to C5."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_3V3_RAIL_JOIN_V52.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL5V_ESCAPE_V53.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_5V')
 # U1.33 exits the top edge; U1.17 exits the right edge.  The shared
 # B.Cu corridor is above the existing SPI bands and approaches C5 from left.
 tr(b,n,F,(95.2,66.05),(95.2,65.2));vi(b,n,(95.2,65.2))
 tr(b,n,F,(101.95,66.8),(102.8,66.8));vi(b,n,(102.8,66.8))
 tr(b,n,B,(95.2,65.2),(102.8,65.2));tr(b,n,B,(102.8,65.2),(102.8,66.8))
 tr(b,n,B,(102.8,66.8),(115.6,69.0));vi(b,n,(115.6,69.0));tr(b,n,F,(115.6,69.0),(116.4,69.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
