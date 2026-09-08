"""V355: RTL_1V1 package escape and B.Cu support trunk trial."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_ROUTE_V342.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RTL1V1_ROUTE_V355.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b); x.SetPosition(P(*q)); x.SetWidth(pcbnew.FromMM(.60)); x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F,B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1')
 esc=[((103.2,58.05),(102.5,57.5)),((102.05,61.6),(101.3,61.6)),((103.2,65.95),(103.2,67)),((104.8,65.95),(104.8,67)),((108.8,65.95),(108.8,67)),((109.95,64),(111,64)),((109.95,62),(111,62)),((109.95,60.8),(111,60.8)),((113.2,53),(113.2,51.5))]
 for a,z in esc: s(b,n,F,a,z); v(b,n,z)
 for a,z in [((102.5,57.5),(102.5,51.5)),((101.3,61.6),(99,61.6)),((103.2,67),(103.2,70)),((104.8,67),(104.8,70)),((108.8,67),(108.8,70)),((111,64),(115,64)),((111,62),(115,62)),((111,60.8),(115,60.8)),((113.2,51.5),(102.5,51.5))]: s(b,n,B,a,z)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
