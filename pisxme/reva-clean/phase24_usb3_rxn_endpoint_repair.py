"""Disposable repair of the RX_N endpoint approach on the Phase 18 oracle route."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_USB3_PHASE18_ORACLE_ON_CORRECTED_MACRO.kicad_pcb"
OUT = R / "PHASE24_USB3_PHASE18_ORACLE_RXN_DOGLEG.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def add_track(b,n,a,z,l):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); b.Add(t)
def add_via(b,n,p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); b.Add(v)

b=pcbnew.LoadBoard(str(BASE))
n=b.FindNet('/CORE_CM5/CM5_USB3_RX_N')
u=pad(b,'U7','42'); goal=xy(u.GetPosition())
j=pad(b,'J7','128'); src=xy(j.GetPosition())
for t in list(b.GetTracks()):
    if t.GetNetname() == '/CORE_CM5/CM5_USB3_RX_N': b.Remove(t)
# Recreate the validated native source launch, then move left/down in B.Cu,
# transition outside the U7 pad field, and make a short F.Cu approach.
add_track(b,n,src,(71.2,103.9),F)
add_track(b,n,(71.2,103.9),(72.0,103.9),F)
add_via(b,n,(72.0,103.9))
add_track(b,n,(72.0,103.9),(101.5,107.0),B)
add_track(b,n,(101.5,107.0),(103.5,107.0),B)
add_via(b,n,(103.5,107.0))
add_track(b,n,(103.5,107.0),goal,F)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
