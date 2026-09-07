"""V145: disposable REFCLK pair launch from the V144 support basis."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SSD33_ON_V143_V144.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_REFCLK_V145.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=.20):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def pair(b,name,src,dst,corridor):
 n=b.FindNet(name); sx,sy=src; dx,dy=dst; cy=corridor
 tr(b,n,F,(sx,sy),(sx,cy));via(b,n,(sx,cy));tr(b,n,B,(sx,cy),(dx,cy),.20);via(b,n,(dx,cy));tr(b,n,F,(dx,cy),(dx,dy))
def main():
 b=pcbnew.LoadBoard(str(BASE))
 pair(b,'REFCLK_P',(98.4,73.95),(137.25,62.725),76.0)
 pair(b,'REFCLK_N',(98.8,73.95),(136.75,62.725),77.0)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
