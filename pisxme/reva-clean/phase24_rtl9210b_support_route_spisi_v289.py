"""V289: trial SPISI high-north B.Cu corridor."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_ROUTE_SPICLK_V288.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SUPPORT_ROUTE_SPISI_V289.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.25));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('SPISI')
 tr(b,n,F,(101.2,58.05),(101.2,57.5));tr(b,n,F,(101.2,57.5),(104.0,57.5));via(b,n,(104.0,57.5));tr(b,n,B,(104.0,57.5),(104.0,47.5));tr(b,n,B,(104.0,47.5),(88.1,47.5));tr(b,n,B,(88.1,47.5),(88.1,68.0));via(b,n,(88.1,68.0));tr(b,n,F,(88.1,68.0),(88.1,70.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
