"""V20: move the U11-to-C83 AVDDL branch to a B.Cu corridor."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb'))
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,p):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(n,a,z,l,w=.2):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def near(a,z,x,y):
 return all(abs(a[i]-x if i==0 else a[i]-y)<.001 for i in range(2)) and all(abs(z[i]-x if i==0 else z[i]-y)<.001 for i in range(2))
n=b.FindNet('JMS_AVDDL')
# Remove only the existing U11/C83 branch segments and its two branch vias.
targets=[]
for t in list(b.GetTracks()):
 if t.GetNetCode()!=n.GetNetCode():continue
 if isinstance(t,pcbnew.PCB_VIA):
  p=tuple(round(v,3) for v in (pcbnew.ToMM(t.GetPosition().x),pcbnew.ToMM(t.GetPosition().y)))
  if p in {(141.8,140.5),(154.5,142.0)}:targets.append(t)
 else:
  pts=[tuple(round(v,3) for v in (pcbnew.ToMM(t.GetStart().x),pcbnew.ToMM(t.GetStart().y))),tuple(round(v,3) for v in (pcbnew.ToMM(t.GetEnd().x),pcbnew.ToMM(t.GetEnd().y)))]
  if any(p in {(141.8,138.6),(141.8,140.5),(154.5,142.0),(154.5,147.0)} for p in pts):targets.append(t)
for t in targets:b.RemoveNative(t)
source=xy('U11',20);cap=xy('C83',1);a=(141.8,141.0);sv=(143.5,141.0);rv=(154.5,146.0)
tr(n,source,a,F);tr(n,a,sv,F);via(n,sv);tr(n,sv,(154.5,141.0),B);tr(n,(154.5,141.0),rv,B);via(n,rv);tr(n,rv,cap,F)
b.BuildListOfNets();out=R/'PHASE24_STORAGE_U11_AVDDL_BCU_COAUTHORED_V20.kicad_pcb';b.Save(str(out));print(out,'removed',len(targets))
