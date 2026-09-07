"""V245: translate the historical V95/V96 lower-edge route class onto V242."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V242.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V245.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
 # V95/V96 translated by -8 mm in Y, with the native current U1 pads.
 tr(b,n,F,(98.0,65.95),(98.0,66.8));tr(b,n,F,(98.0,66.8),(103.0,66.8));tr(b,n,F,(103.0,66.8),(103.0,65.8));via(b,n,(103.0,65.8));tr(b,n,B,(103.0,65.8),(107.0,65.8));tr(b,n,B,(107.0,65.8),(107.0,55.0));tr(b,n,B,(107.0,55.0),(104.0,55.0))
 tr(b,n,F,(99.2,65.95),(99.2,66.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
