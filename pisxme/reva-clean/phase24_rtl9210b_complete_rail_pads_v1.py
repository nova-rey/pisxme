"""Disposable completion of two additional relocated RTL9210B rail pads."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_RELOCATION_RAILS_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SUPPORT_RELOCATION_RAIL_PADS_V1.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def path(b,name,src,sv,bend,dv,dst):
 n=b.FindNet(name);seg(b,n,F,src,sv);via(b,n,sv);seg(b,n,B,sv,bend);seg(b,n,B,bend,dv);via(b,n,dv);seg(b,n,F,dv,dst)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 # Pad 34 to the existing local 3V3 dogbone; pad 33 to the 5V trunk.
 path(b,'RTL_3V3',(101.95,66.8),(106.0,66.8),(106.0,68.5),(109.6,68.5),(109.6,68.5))
 path(b,'RTL_5V',(101.95,67.2),(114.0,67.2),(114.0,68.5),(115.6,68.5),(116.4,69.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
