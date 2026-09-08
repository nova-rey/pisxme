"""V345: pad-clear RTL_5V handoff and 3V3-avoiding In2 tree."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_RTL3V3_ROUTE_V342.kicad_pcb';OUT=H/'PHASE24_RTL9210B_RTL5V_ROUTE_V345.kicad_pcb'
F,B,L=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_5V')
 s(b,n,F,(102.8,58.05),(99.5,58.05));v(b,n,(99.5,58.05))
 s(b,n,F,(102.05,64.8),(103,64.8));s(b,n,F,(103,64.8),(103,67.5));v(b,n,(103,67.5))
 v(b,n,(124.4,59));s(b,n,F,(124.4,61),(124.4,59))
 for a,z in [((99.5,58.05),(99.5,57)),((99.5,57),(124.4,57)),((124.4,57),(124.4,59)),((103,67.5),(103,68.5)),((103,68.5),(99.5,68.5)),((99.5,68.5),(99.5,57))]:s(b,n,L,a,z)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
