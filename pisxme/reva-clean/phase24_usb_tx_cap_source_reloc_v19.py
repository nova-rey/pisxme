"""V19: move USB TX caps toward U11 while retaining the U12 launch corridor."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb'));F=pcbnew.F_Cu
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,p):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(n,a,z,w=.2):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def clear(name):
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode():b.RemoveNative(t)
 return n
for ref,pos in (('C86',(145.0,141.0)),('C87',(145.0,143.0))):
 f=b.FindFootprintByReference(ref);f.SetPosition(V(*pos));f.SetOrientationDegrees(0)
p=clear('USB_TXP1');n=clear('USB_TXN1');pp=clear('JMS_USB3_TXP');nn=clear('JMS_USB3_TXN')
tr(p,xy('U11',21),(141.2,139.4),.15);tr(p,(141.2,139.4),(141.2,141.0));tr(p,(141.2,141.0),xy('C86',1))
tr(n,xy('U11',22),(141.0,139.0),.15);tr(n,(141.0,139.0),(140.6,139.4),.15);tr(n,(140.6,139.4),(140.6,143.0));tr(n,(140.6,143.0),xy('C87',1))
tr(pp,xy('C86',2),(147.5,141.0));tr(pp,(147.5,141.0),(147.5,145.0));tr(pp,(147.5,145.0),(162.0,145.0));tr(pp,(162.0,145.0),(162.0,137.0));tr(pp,(162.0,137.0),xy('U12',25),.15)
tr(nn,xy('C87',2),(147.5,143.0));tr(nn,(147.5,143.0),(147.5,149.0));tr(nn,(147.5,149.0),(163.0,149.0));tr(nn,(163.0,149.0),(163.0,137.4));tr(nn,(163.0,137.4),xy('U12',24),.15)
b.BuildListOfNets();out=R/'PHASE24_STORAGE_USB_TX_CAP_SOURCE_RELOC_V19.kicad_pcb';b.Save(str(out));print(out)
