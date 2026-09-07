"""V56: route RTL_5V around the U1.20 RTL_3V3 spine endpoint."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_3V3_RAIL_JOIN_V52.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL5V_ESCAPE_V56.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_5V')
 # The F.Cu path rises above the RTL_3V3 spine endpoint at (100.4,60.8).
 tr(b,n,F,(95.2,66.05),(95.2,64.5));tr(b,n,F,(95.2,64.5),(96.5,64.5));tr(b,n,F,(96.5,64.5),(96.5,60.0));tr(b,n,F,(96.5,60.0),(102.8,60.0));tr(b,n,F,(102.8,60.0),(102.8,66.8));vi(b,n,(102.8,66.8));tr(b,n,F,(101.95,66.8),(102.8,66.8))
 tr(b,n,B,(102.8,66.8),(108.5,66.8));tr(b,n,B,(108.5,66.8),(108.5,69.5));tr(b,n,B,(108.5,69.5),(116.9,69.5));tr(b,n,B,(116.9,69.5),(116.9,69.0));vi(b,n,(116.9,69.0));tr(b,n,F,(116.9,69.0),(116.4,69.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
