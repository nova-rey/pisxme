"""V1523: rehome U1.52 RTL_3V3 north/east to open the XTAL_OUT pocket."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U155_REHOME_V1517.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RTL3V3_REHOME_U152_V1523.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('RTL_3V3'); F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def xy(o): return (round(o.x/1e6,4),round(o.y/1e6,4))
def near(a,z): return xy(a)==tuple(round(v,4) for v in z)
removed=[]
for o in list(b.GetTracks()):
 if o.GetNetCode()!=n.GetNetCode(): continue
 if isinstance(o,pcbnew.PCB_VIA) and xy(o.GetPosition())==(93.0,66.8): b.RemoveNative(o); removed.append('via93')
 elif isinstance(o,pcbnew.PCB_TRACK) and (near(o.GetStart(),(94.05,66.8)) and near(o.GetEnd(),(93.0,66.8)) or near(o.GetStart(),(93.0,66.8)) and near(o.GetEnd(),(93.0,65.8)) or near(o.GetStart(),(93.0,65.8)) and near(o.GetEnd(),(99.6,65.8))): b.RemoveNative(o); removed.append(xy(o.GetStart()))
def tr(a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr((94.05,66.8),(94.05,65.8),F); via(94.05,65.8); tr((94.05,65.8),(96.5,65.8),B); tr((96.5,65.8),(96.5,62.8),B); tr((96.5,62.8),(99.6,62.8),B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT,'removed',removed)
