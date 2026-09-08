"""V354: B.Cu RTL_5V trunk crosses east at y66, below XTAL_IN endpoint."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_ROUTE_V342.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RTL5V_ROUTE_V354.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b); x.SetPosition(P(*q)); x.SetWidth(pcbnew.FromMM(.60)); x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F,B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_5V')
 for a,z in [((102.8,58.05),(98.5,58.05)),((102.05,64.8),(103.5,64.8)),((124.4,61),(124.4,59))]: s(b,n,F,a,z); v(b,n,z)
 for a,z in [((98.5,58.05),(96,58.05)),((96,58.05),(96,66)),((96,66),(105,66)),((105,66),(120,66)),((120,66),(120,59)),((120,59),(124.4,59)),((103.5,64.8),(105,64.8)),((105,64.8),(105,66))]: s(b,n,B,a,z)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
