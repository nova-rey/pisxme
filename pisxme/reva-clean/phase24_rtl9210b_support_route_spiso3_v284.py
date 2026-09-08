"""V284: SPISO3 high north B.Cu corridor, avoiding the lower SPI field."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_ROUTE_SPISO_V282.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SUPPORT_ROUTE_SPISO3_V284.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(pcbnew.FromMM(.20)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.25)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('SPISO3')
 tr(b,n,F,(99.6,58.05),(99.6,49.0)); via(b,n,(99.6,49.0)); tr(b,n,B,(99.6,49.0),(90.5,49.0)); tr(b,n,B,(90.5,49.0),(90.5,68.0)); via(b,n,(90.5,68.0)); tr(b,n,F,(90.5,68.0),(90.5,70.0))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
