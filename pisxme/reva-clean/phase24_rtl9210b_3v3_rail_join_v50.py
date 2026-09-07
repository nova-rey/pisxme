"""V50: join the corrected U1.20/C3 and R2/R3 3V3 rail taps."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U1_52_HANDOFF_V49.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_RAIL_JOIN_V50.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
 # Existing U1.20/C3 trunk terminates at the U1.20-side transition near 100.4,60.8.
 # Bring the two resistor rail taps to that same F.Cu trunk, outside the QFN field.
 tr(b,n,F,(90.2,56.0),(90.2,60.8)); tr(b,n,F,(90.2,60.8),(93.2,60.8))
 tr(b,n,F,(93.2,56.0),(93.2,60.8)); tr(b,n,F,(93.2,60.8),(100.4,60.8))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
