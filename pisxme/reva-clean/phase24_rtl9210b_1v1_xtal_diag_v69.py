"""V69: diagnostic U1.60 route after removing the obstructing XTAL_IN field."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_1V1_TOP25_V63.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_1V1_XTAL_DIAG_V69.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for q in list(b.GetTracks()):
  if q.GetNetname()=='XTAL_IN': b.RemoveNative(q)
 n=b.FindNet('RTL_1V1')
 # With XTAL_IN removed, demonstrate the otherwise-clear U1.60 to C4 corridor.
 tr(b,n,F,(98.0,73.95),(98.0,74.8));tr(b,n,F,(98.0,74.8),(112.5,74.8));vi(b,n,(112.5,74.8));tr(b,n,B,(112.5,74.8),(113.8,74.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
