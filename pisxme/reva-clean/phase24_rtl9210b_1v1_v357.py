"""V357: RTL_1V1 C4 handoff switches to F.Cu before XTAL_OUT."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_ROUTE_V342.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RTL1V1_ROUTE_V357.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b); x.SetPosition(P(*q)); x.SetWidth(pcbnew.FromMM(.60)); x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F,B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1')
 for a,z in [((103.2,58.05),(103.2,56.5)),((112,56.5),(112,55)),((113.2,53),(112.8,53))]: s(b,n,F,a,z); v(b,n,z)
 for a,z in [((103.2,56.5),(112,56.5))]: s(b,n,B,a,z)
 s(b,n,F,(112,55),(112,53)); s(b,n,F,(112,53),(112.8,53)); s(b,n,F,(112.8,53),(113.2,53))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
