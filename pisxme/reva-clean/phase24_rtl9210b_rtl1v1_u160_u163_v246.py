"""V246: co-author lower-edge U1.60/U1.63 around REFCLK/PEDET fields."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V242.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V246.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
 tr(b,n,F,(98.0,65.95),(97.4,66.4));tr(b,n,F,(97.4,66.4),(97.4,67.5));tr(b,n,F,(97.4,67.5),(103.0,67.5));tr(b,n,F,(103.0,67.5),(103.0,65.8));via(b,n,(103.0,65.8));tr(b,n,B,(103.0,65.8),(107.0,65.8));tr(b,n,B,(107.0,65.8),(107.0,63.0));via(b,n,(107.0,63.0));tr(b,n,F,(107.0,63.0),(107.0,54.5));via(b,n,(107.0,54.5));tr(b,n,B,(107.0,54.5),(104.0,55.0));tr(b,n,F,(99.2,65.95),(99.2,67.5))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
