"""V55: clear the C5 ground pad and SPISI departure in the RTL_5V route."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_3V3_RAIL_JOIN_V52.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL5V_ESCAPE_V55.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_5V')
 # Lift the U1 top-edge corridor above the diagonal SPISI departure.
 tr(b,n,F,(95.2,66.05),(95.2,64.5));tr(b,n,F,(95.2,64.5),(96.5,64.5));tr(b,n,F,(96.5,64.5),(96.5,63.5));tr(b,n,F,(96.5,63.5),(102.8,63.5));tr(b,n,F,(102.8,63.5),(102.8,66.8));vi(b,n,(102.8,66.8));tr(b,n,F,(101.95,66.8),(102.8,66.8))
 # Approach C5.1 from the right, with a full clearance radius from pad 2.
 tr(b,n,B,(102.8,66.8),(108.5,66.8));tr(b,n,B,(108.5,66.8),(108.5,69.5));tr(b,n,B,(108.5,69.5),(116.9,69.5));tr(b,n,B,(116.9,69.5),(116.9,69.0));vi(b,n,(116.9,69.0));tr(b,n,F,(116.9,69.0),(116.4,69.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
