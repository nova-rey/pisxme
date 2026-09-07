"""V49: co-author the corrected U1.52 escape around the XTAL_IN field."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CORRECT_U1_FRAME_V47.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U1_52_HANDOFF_V49.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for q in list(b.GetTracks()):
  if q.GetNetname()=='RTL_3V3': b.RemoveNative(q)
 n=b.FindNet('RTL_3V3')
 # U1.20 -> corrected C3 trunk, with only genuine layer transitions.
 tr(b,n,F,(100.4,66.05),(100.4,60.8));vi(b,n,(100.4,60.8));tr(b,n,B,(100.4,60.8),(110.0,60.8));tr(b,n,B,(110.0,60.8),(110.0,68.5));vi(b,n,(110.0,68.5));tr(b,n,F,(110.0,68.5),(110.4,69.0))
 # U1.34/U1.39 and downstream U2 branch.
 tr(b,n,F,(94.8,66.05),(93.0,65.2));tr(b,n,F,(93.0,65.2),(93.0,68.4));tr(b,n,F,(93.0,68.4),(94.05,68.4));tr(b,n,F,(93.0,68.4),(92.0,68.4));vi(b,n,(92.0,68.4));tr(b,n,B,(92.0,68.4),(90.2,75.5));vi(b,n,(90.2,75.5));tr(b,n,F,(90.2,75.5),(90.2,80.0));tr(b,n,F,(90.2,80.0),(90.2,82.0));tr(b,n,F,(90.2,82.0),(84.2,82.0));tr(b,n,F,(84.2,82.0),(84.2,80.0))
 # U1.52 exits left/below the QFN; via at 94.2,74.4 clears XTAL_IN.
 tr(b,n,F,(94.8,73.95),(94.8,74.4));tr(b,n,F,(94.8,74.4),(94.2,74.4));vi(b,n,(94.2,74.4));tr(b,n,B,(94.2,74.4),(90.2,74.4));tr(b,n,B,(90.2,74.4),(90.2,75.5))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
