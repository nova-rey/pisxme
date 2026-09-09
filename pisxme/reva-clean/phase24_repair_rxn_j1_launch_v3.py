"""Disposable RX_N launch routed around the left edge and below J1."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VBUS_measured_gap.kicad_pcb'; OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VBUS_RXN_REPAIR_V3.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def vi(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('CM5_USB3_RX_N')
for q in list(b.GetTracks()):
 if q.GetNetCode()==n.GetNetCode():b.RemoveNative(q)
vi(b,n,(70,88));tr(b,n,B,(73,88),(70,88));tr(b,n,B,(70,88),(70,97));tr(b,n,B,(70,97),(145,97));tr(b,n,B,(145,97),(145,137.8));vi(b,n,(145,137.8));tr(b,n,F,(145,137.8),(153.5,137.8))
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
