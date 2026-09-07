"""V243: test a west-side U1.40 RTL_1V1 branch on the V242 basis."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V242.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V243.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
    q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
    q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
    tr(b,n,F,(94.05,60.8),(91.0,60.8));via(b,n,(91.0,60.8))
    tr(b,n,B,(91.0,60.8),(91.0,55.0));tr(b,n,B,(91.0,55.0),(92.0,55.0))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
