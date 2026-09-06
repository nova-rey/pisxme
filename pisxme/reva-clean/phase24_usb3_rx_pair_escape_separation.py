"""Disposable coordinated RX endpoint escape for Phase 24 USB3."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_USB3_PHASE18_ORACLE_TX_LAUNCH_SEPARATED.kicad_pcb'; OUT=R/'PHASE24_USB3_PHASE18_ORACLE_RX_PAIR_SEPARATED.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):
 p=p.GetPosition() if hasattr(p,'GetPosition') else p; return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def P(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def T(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def X(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.50));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
b=pcbnew.LoadBoard(str(BASE)); jobs={'RX_N':('/CORE_CM5/CM5_USB3_RX_N','128','42'),'RX_P':('/CORE_CM5/CM5_USB3_RX_P','130','43')}; ends={k:(xy(P(b,'J7',j)),xy(P(b,'U7',u))) for k,(_,j,u) in jobs.items()}
for t in list(b.GetTracks()):
 if any(t.GetNetname()==n for n,_,_ in jobs.values()): b.Remove(t)
for k,(netname,_,_) in jobs.items():
 n=b.FindNet(netname); src,goal=ends[k]
 if k=='RX_N':
  T(b,n,src,(71.2,103.9),F);T(b,n,(71.2,103.9),(72.0,103.9),F);X(b,n,(72.0,103.9));T(b,n,(72.0,103.9),(103.5,105.0),B);X(b,n,(103.5,105.0));T(b,n,(103.5,105.0),goal,F)
 else:
  T(b,n,src,(71.2,104.3),F);T(b,n,(71.2,104.3),(72.0,104.8),F);X(b,n,(72.0,104.8));T(b,n,(72.0,104.8),(103.5,106.0),B);X(b,n,(103.5,106.0));T(b,n,(103.5,106.0),goal,F)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
