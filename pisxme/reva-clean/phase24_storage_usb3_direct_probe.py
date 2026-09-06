"""Disposable direct USB3 corridor probe on the selected storage placement."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_MACRO_FRESH_STORAGE_LOCAL_J3_EDGE.kicad_pcb'
OUT=R/'PHASE24_STORAGE_LOCAL_J3_EDGE_USB3_DIRECT.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.15)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def pad(b,r,k): return b.FindFootprintByReference(r).FindPadByNumber(str(k))
def net(b,s):
    n=b.FindNet('/CORE_CM5/'+s)
    if n is None: raise RuntimeError(s)
    return n
def tr(b,n,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);b.Add(t)
b=pcbnew.LoadBoard(str(BASE))
jobs=[('CM5_USB3_RX_N','128','42'),('CM5_USB3_RX_P','130','43'),('CM5_USB3_TX_N','140','45'),('CM5_USB3_TX_P','142','46')]
term=[(s,xy(pad(b,'J7',sp).GetPosition()),xy(pad(b,'U7',tp).GetPosition())) for s,sp,tp in jobs]
for t in list(b.Tracks()):
    if any(k in t.GetNetname() for k in ('CM5_USB3_','BRIDGE_SATA_','SATA_M2_','BRIDGE_XI','BRIDGE_XO')): b.Remove(t)
for s,a,z in term:
    n=net(b,s)
    # Two intermediate points keep each pair monotonic and create a
    # constant-width corridor without a transition or via stub.
    midx=78.0 + (term.index((s,a,z)) * 1.0)
    tr(b,n,a,(midx,a[1])); tr(b,n,(midx,a[1]),(midx,z[1])); tr(b,n,(midx,z[1]),z)
    print(s,a,z)
b.Save(str(OUT)); print(OUT)
