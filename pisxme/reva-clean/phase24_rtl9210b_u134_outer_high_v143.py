"""V143: outer-left/high B.Cu U1.34 escape clearing V137 RTL_5V."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL5V_BELOW_C5_V137.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U134_OUTER_HIGH_V143.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
 tr(b,n,F,(94.8,66.05),(92.8,66.05));tr(b,n,F,(92.8,66.05),(92.8,54.8));via(b,n,(92.8,54.8));tr(b,n,B,(92.8,54.8),(102.5,54.8));tr(b,n,B,(102.5,54.8),(102.5,60.8));tr(b,n,B,(102.5,60.8),(100.4,60.8));via(b,n,(100.4,60.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
