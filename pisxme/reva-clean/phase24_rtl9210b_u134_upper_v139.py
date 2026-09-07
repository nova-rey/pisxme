"""V139: alternate U1.34 upper F.Cu/B.Cu handoff on the V137 basis."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RTL5V_BELOW_C5_V137.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U134_UPPER_V139.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(pcbnew.FromMM(.20)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
 tr(b,n,F,(94.8,66.05),(94.8,59.5)); via(b,n,(94.8,59.5)); tr(b,n,B,(94.8,59.5),(100.4,59.5)); tr(b,n,B,(100.4,59.5),(100.4,60.8)); via(b,n,(100.4,60.8))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
