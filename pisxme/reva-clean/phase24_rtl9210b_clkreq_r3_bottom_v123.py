"""V123: connect R3 CLKREQ_N to the promoted U1/J1 control path."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_R2_RIGHT_RETURN_V122.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CLKREQ_R3_BOTTOM_V123.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.15));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('CLKREQ_N')
 tr(b,n,F,(92.0,56.0),(92.0,53.0));tr(b,n,F,(92.0,53.0),(87.0,53.0));via(b,n,(87.0,53.0));tr(b,n,B,(87.0,53.0),(87.0,85.0));tr(b,n,B,(87.0,85.0),(103.5,85.0));via(b,n,(103.5,85.0));tr(b,n,F,(103.5,85.0),(103.5,68.4))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
