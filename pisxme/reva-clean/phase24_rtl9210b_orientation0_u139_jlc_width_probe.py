"""Disposable JLC-width U1.39 escape discriminator; never production CAD."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_QFN_ORIENTATION0_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_QFN_ORIENTATION0_U139_JLC_WIDTH_PROBE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
    v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.50));v.SetDrill(pcbnew.FromMM(.25));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
seg(b,n,F,(99.6,66.05),(101.2,64.5));via(b,n,(101.2,64.5))
seg(b,n,B,(101.2,64.5),(80.2,64.5));via(b,n,(80.2,64.5));seg(b,n,F,(80.2,64.5),(80.2,80.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
