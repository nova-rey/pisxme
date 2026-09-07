"""V135: shift RTL_5V C5 transition right and above CLKREQ."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CLKREQ_R3_RAIL_OVERPASS_V131.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL5V_RIGHT_C5_V135.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_5V')
 tr(b,n,F,(95.2,66.05),(95.2,63.0));tr(b,n,F,(95.2,63.0),(93.5,63.0));tr(b,n,F,(93.5,63.0),(93.5,62.0));via(b,n,(93.5,62.0));tr(b,n,B,(93.5,62.0),(103.5,62.0));via(b,n,(103.5,62.0));tr(b,n,F,(103.5,62.0),(103.5,66.4));tr(b,n,F,(103.5,66.4),(102.0,66.4));tr(b,n,F,(102.0,66.4),(101.95,66.8))
 tr(b,n,F,(103.5,66.4),(104.5,66.4));tr(b,n,F,(104.5,66.4),(104.5,65.8));tr(b,n,F,(104.5,65.8),(117.2,65.8));via(b,n,(117.2,65.8));tr(b,n,B,(117.2,65.8),(117.2,69.0));via(b,n,(117.2,69.0));tr(b,n,F,(117.2,69.0),(116.4,69.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
