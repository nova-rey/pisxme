"""Clean TI-U7 180-degree source-local west-target fixture."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;B=pcbnew.F_Cu;L=pcbnew.B_Cu;W=pcbnew.FromMM(.15)
IN=R/'PHASE24_USB3_LOCAL_TI_MINIMAL.kicad_pcb';OUT=R/'PHASE24_USB3_LOCAL_TI_WEST_TARGET.kicad_pcb'
J=(('CM5_USB3_RX_N','128','42'),('CM5_USB3_RX_P','130','43'),('CM5_USB3_TX_N','140','45'),('CM5_USB3_TX_P','142','46'))
def V(p):return pcbnew.VECTOR2I_MM(*p)
def xy(p):q=p.GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def net(b,n):
 for q in (n,'/CORE_CM5/'+n,'/STORAGE/'+n):
  x=b.FindNet(q)
  if x:return x
 raise RuntimeError(n)
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(a));t.SetEnd(V(z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(B,L);v.SetNet(n);b.Add(v)
b=pcbnew.LoadBoard(str(IN));targets=((80.0,105.6),(81.0,106.0),(82.0,106.8),(83.0,107.2))
source_vias=((74.0,102.2),(76.0,105.2),(78.0,108.2),(80.0,111.2))
for i,(name,j,u) in enumerate(J):
 n=net(b,name);src=xy(b.FindFootprintByReference('J7').FindPadByNumber(j));dst=xy(b.FindFootprintByReference('U7').FindPadByNumber(u));sv=source_vias[i];tv=targets[i]
 tr(b,n,src,sv,L);via(b,n,sv);tr(b,n,sv,tv,L);via(b,n,tv);tr(b,n,tv,dst,B)
 print(name,src,dst,sv,tv)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
