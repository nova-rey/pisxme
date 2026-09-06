"""Disposable RX_N lateral endpoint-via repair."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_USB3_PHASE18_ORACLE_TX_LAUNCH_SEPARATED.kicad_pcb'
OUT=R/'PHASE24_USB3_PHASE18_ORACLE_RXN_LATERAL_VIA.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):
 p=p.GetPosition() if hasattr(p,'GetPosition') else p
 return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def P(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def T(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def X(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.50));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/CORE_CM5/CM5_USB3_RX_N'); src=xy(P(b,'J7','128')); goal=xy(P(b,'U7','42'))
for t in list(b.GetTracks()):
 if t.GetNetname()=='/CORE_CM5/CM5_USB3_RX_N': b.Remove(t)
T(b,n,src,(71.2,103.9),F); T(b,n,(71.2,103.9),(72.0,103.9),F); X(b,n,(72.0,103.9))
T(b,n,(72.0,103.9),(101.0,103.0),B); X(b,n,(101.0,103.0)); T(b,n,(101.0,103.0),goal,F)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
