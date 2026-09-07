"""V146: REFCLK pair on a clear F.Cu corridor with B.Cu J1 drops."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SSD33_ON_V143_V144.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_REFCLK_F_CORRIDOR_V146.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def route(b,name,src,cy,drop,contact):
 n=b.FindNet(name); sx,sy=src; dx,dy=drop; cx,cyc=contact
 tr(b,n,F,(sx,sy),(sx,cy));tr(b,n,F,(sx,cy),(dx,cy));via(b,n,(dx,cy));tr(b,n,B,(dx,cy),(dx,dy));via(b,n,(dx,dy));tr(b,n,F,(dx,dy),(cx,dy))
def main():
 b=pcbnew.LoadBoard(str(BASE))
 route(b,'REFCLK_P',(98.4,73.95),72.5,(137.75,62.725),(137.25,62.725))
 route(b,'REFCLK_N',(98.8,73.95),73.0,(136.0,62.725),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
