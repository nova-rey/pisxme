"""V657 disposable: single SPICS west-channel discriminator."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_ORIENTATION180_3V3_C3_JOIN_PROBE.kicad_pcb'; out=H/'PHASE24_RTL9210B_SPICS_WEST_CHANNEL_PROBE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base)); n=b.FindNet('SPICS')
for q in list(b.GetTracks()):
 if q.GetNetname()=='SPICS': b.RemoveNative(q)
t(b,n,F,(94.05,69.2),(91.5,69.2));t(b,n,F,(91.5,69.2),(91.5,52));v(b,n,(91.5,52));t(b,n,B,(91.5,52),(71.8,52));v(b,n,(71.8,52));t(b,n,F,(71.8,52),(71.8,80));t(b,n,F,(71.8,80),(71.8,80))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
