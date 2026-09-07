"""V40: jointly allocate outer RTL_3V3 and corrected RTL_5V spines."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_5V_RAIL_V39.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_JOINT_RAILS_V40.kicad_pcb'
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
 # U1.20 to an outer B.Cu spine; C3 is reached by a local F.Cu dogbone.
 t(b,n,F,(100.4,66.05),(100.4,54.0));v(b,n,(100.4,54.0));t(b,n,B,(100.4,54.0),(120.0,54.0));t(b,n,B,(120.0,54.0),(120.0,68.0));t(b,n,B,(120.0,68.0),(110.4,68.0));v(b,n,(110.4,68.0));t(b,n,F,(110.4,68.0),(110.4,69.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
