"""V42: partition RTL_3V3 source, C3 trunk, and U2 drop."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CORRECT_RAIL_CAPS_V38.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_PARTITIONED_V42.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for x in list(b.GetTracks()):
  if x.GetNetname()=='RTL_3V3':b.RemoveNative(x)
 n=b.FindNet('RTL_3V3')
 # Retain the validated V24 U1.20-to-C3 trunk.
 t(b,n,F,(100.4,66.05),(100.4,60.8));v(b,n,(100.4,60.8));t(b,n,B,(100.4,60.8),(110,60.8));t(b,n,B,(110,60.8),(110,68.5));v(b,n,(110,68.5));t(b,n,F,(110,68.5),(110.4,69))
 # Left-side source fanout for U1.34/U1.39, clear of pad 35.
 t(b,n,F,(94.8,66.05),(93.0,65.2));t(b,n,F,(93.0,65.2),(93.0,68.4));t(b,n,F,(93.0,68.4),(94.05,68.4))
 # U1.39 to U2.8: B.Cu handoff, then F.Cu drop below the support paths.
 t(b,n,F,(94.05,68.4),(92.0,68.4));v(b,n,(92.0,68.4));t(b,n,B,(92.0,68.4),(92.0,75.5));v(b,n,(92.0,75.5));t(b,n,B,(92.0,75.5),(90.2,75.5));v(b,n,(90.2,75.5));t(b,n,F,(90.2,75.5),(90.2,80.0))
 # U2.3 joins the same drop below the SPI pad row.
 t(b,n,F,(84.2,80.0),(84.2,82.0));t(b,n,F,(84.2,82.0),(90.2,82.0));t(b,n,F,(90.2,82.0),(90.2,80.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
