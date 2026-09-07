"""V43: move the V42 3V3 downstream transition clear of RSET."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_3V3_PARTITIONED_V42.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_PARTITIONED_V43.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
 # Replace the V42 segment/vias between the U1.39 handoff and U2.
 for x in list(b.GetTracks()):
  if x.GetNetname()=='RTL_3V3' and (x.GetStart()==P(92,68.4) or x.GetEnd()==P(92,68.4) or x.GetStart()==P(92,75.5) or x.GetEnd()==P(92,75.5) or x.GetStart()==P(90.2,75.5) or x.GetEnd()==P(90.2,75.5) or x.GetStart()==P(90.2,79) or x.GetEnd()==P(90.2,79)):
   b.RemoveNative(x)
 for x in list(b.GetTracks()):
  p=x.GetPosition()
  if x.GetNetname()=='RTL_3V3' and ((p.x/1e6,p.y/1e6) in [(92,68.4),(92,75.5),(90.2,75.5),(90.2,79)]): b.RemoveNative(x)
 t(b,n,F,(94.05,68.4),(92.0,68.4));v(b,n,(92.0,68.4));t(b,n,B,(92.0,68.4),(90.5,74.5));v(b,n,(90.5,74.5));t(b,n,B,(90.5,74.5),(90.2,75.5));v(b,n,(90.2,75.5));t(b,n,F,(90.2,75.5),(90.2,80.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
