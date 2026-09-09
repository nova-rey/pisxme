"""Disposable VBUS-sense route with an outboard resistor-side transition."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VBUS_RXN_REPAIR_V3.kicad_pcb'; OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VBUS_RXN_REPAIR_V10.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def vi(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('JMS_VBUS_SENSE')
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode():b.RemoveNative(t)
tr(b,n,F,(136.35,135.6),(134.0,135.6));vi(b,n,(134.0,135.6));tr(b,n,B,(134.0,135.6),(132.0,135.6));tr(b,n,B,(132.0,135.6),(132.0,142.0));vi(b,n,(132.0,142.0));tr(b,n,F,(132.0,142.0),(132.0,143.0));vi(b,n,(132.0,143.0));tr(b,n,B,(132.0,143.0),(132.0,146.8));tr(b,n,B,(132.0,146.8),(122.0,146.8));vi(b,n,(122.0,146.8));tr(b,n,F,(122.0,146.8),(124.5,148.0));tr(b,n,F,(124.5,148.0),(129.5,148.0))
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
