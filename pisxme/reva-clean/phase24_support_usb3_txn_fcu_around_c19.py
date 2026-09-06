"""Disposable repair: shift U7 USB3 TX_N F.Cu leg clear of C19."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_NATIVE_ORACLE_SUPPORT_TRANSPLANT.kicad_pcb'
OUT=R/'PHASE24_STORAGE_NATIVE_ORACLE_SUPPORT_TXN_FCU_AROUND_C19.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); b.Add(t)
def via(b,n,p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); b.Add(v)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/CORE_CM5/CM5_USB3_TX_N')
for t in list(b.GetTracks()):
    if t.GetNetname()=='/CORE_CM5/CM5_USB3_TX_N': b.Remove(t)
tr(b,n,(70.04,106.3),(71.2,106.3)); tr(b,n,(71.2,106.3),(72,108)); via(b,n,(72,108))
tr(b,n,(72,108),(82,108)); tr(b,n,(82,108),(102,108)); tr(b,n,(102,108),(103,107)); via(b,n,(103,107))
tr(b,n,(103,107),(112,107)); tr(b,n,(112,107),(112,141.5)); tr(b,n,(112,141.5),(115.5,141.5))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
