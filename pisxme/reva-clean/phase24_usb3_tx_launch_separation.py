"""Disposable TX launch separation for the native CM5IO USB3 route."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_USB3_PHASE18_ORACLE_ON_CORRECTED_MACRO.kicad_pcb'
OUT=R/'PHASE24_USB3_PHASE18_ORACLE_TX_LAUNCH_SEPARATED.kicad_pcb'
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
b=pcbnew.LoadBoard(str(BASE)); u7=b.FindFootprintByReference('U7'); j7=b.FindFootprintByReference('J7')
ends={'TX_N':('/CORE_CM5/CM5_USB3_TX_N','140','45'),'TX_P':('/CORE_CM5/CM5_USB3_TX_P','142','46')}
coords={k:(xy(P(b,'J7',j)),xy(P(b,'U7',u))) for k,(_,j,u) in ends.items()}
for t in list(b.GetTracks()):
 if any(t.GetNetname()==n for n,_,_ in ends.values()): b.Remove(t)
for k,(netname,_,_) in ends.items():
 n=b.FindNet(netname); src,goal=coords[k]
 if k=='TX_N':
  T(b,n,src,(71.2,106.3),F); T(b,n,(71.2,106.3),(72.5,106.3),F); T(b,n,(72.5,106.3),(72.5,108.0),F); T(b,n,(72.5,108.0),(72.0,108.0),F); X(b,n,(72.0,108.0)); T(b,n,(72.0,108.0),(82.0,108.0),B); T(b,n,(82.0,108.0),(102.0,108.0),B); T(b,n,(102.0,108.0),(103.0,107.0),B); X(b,n,(103.0,107.0)); T(b,n,(103.0,107.0),goal,F)
 else:
  T(b,n,src,(70.8,106.7),F); T(b,n,(70.8,106.7),(70.8,109.0),F); T(b,n,(70.8,109.0),(71.0,109.0),F); X(b,n,(71.0,109.0)); T(b,n,(71.0,109.0),(82.0,112.0),B); X(b,n,(82.0,112.0)); T(b,n,(82.0,112.0),goal,F)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
