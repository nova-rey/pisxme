"""V598: route SPICS down an allocated west transition corridor."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V595_CLKREQ_LOCAL.kicad_pcb'
out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V598_SPICS_WEST.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('SPICS')
seg(b,n,F,(102.05,61.2),(100.5,61.2));via(b,n,(100.5,61.2))
seg(b,n,B,(100.5,61.2),(100.5,76.0));seg(b,n,B,(100.5,76.0),(83.3,76.0));
via(b,n,(83.3,68.0));seg(b,n,B,(83.3,76.0),(83.3,68.0));seg(b,n,F,(83.3,68.0),(83.3,70.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
