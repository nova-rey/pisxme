"""Disposable via-in-pad discriminator for the RTL9210B U1.39 escape."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_QFN_ORIENTATION0_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_QFN_ORIENTATION0_U139_VIA_IN_PAD_PROBE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
v=pcbnew.PCB_VIA(b);v.SetPosition(P(99.6,66.05));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
seg(b,n,B,(99.6,66.05),(80.2,64.5));v2=pcbnew.PCB_VIA(b);v2.SetPosition(P(80.2,64.5));v2.SetWidth(pcbnew.FromMM(.60));v2.SetDrill(pcbnew.FromMM(.30));v2.SetLayerPair(F,B);v2.SetNet(n);v2.SetNetCode(n.GetNetCode());b.Add(v2);seg(b,n,F,(80.2,64.5),(80.2,80.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
