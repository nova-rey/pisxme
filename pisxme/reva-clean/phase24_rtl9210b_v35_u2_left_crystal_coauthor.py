"""Co-author XTAL source transitions and U1.55 1V1 escape on V35 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_SOURCE_PRESERVED.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_CRYSTAL_COAUTHOR.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(p(*a));q.SetEnd(p(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base))
for x in list(b.GetTracks()):
 if x.GetNetname() in {'XTAL_IN','XTAL_OUT','RTL_1V1'}: b.RemoveNative(x)
ni=b.FindNet('XTAL_IN'); s(b,ni,F,(95.2,73.95),(95.2,75.5));s(b,ni,F,(95.2,75.5),(93.8,76.5));v(b,ni,(93.8,76.5));s(b,ni,B,(93.8,76.5),(107.5,75.0));v(b,ni,(107.5,75.0));s(b,ni,F,(107.5,75.0),(108.3,75.8));s(b,ni,F,(108.3,75.8),(109.6,78.0))
no=b.FindNet('XTAL_OUT');s(b,no,F,(95.6,73.95),(95.6,76.0));s(b,no,F,(95.6,76.0),(95.0,77.0));v(b,no,(95.0,77.0));s(b,no,B,(95.0,77.0),(110.5,76.8));v(b,no,(110.5,76.8));s(b,no,F,(110.5,76.8),(109.7,75.8));s(b,no,F,(109.7,75.8),(111.4,78.0))
n=b.FindNet('RTL_1V1')
for src,points in [((94.05,67.2),[(87.0,67.2),(87.0,84.0)]),((94.05,68.8),[(88.0,68.8),(88.0,84.0)]),((94.05,72.8),[(89.0,72.8),(89.0,84.0)]),((96.0,73.95),[(96.0,77.5),(97.2,77.5),(97.2,84.0)]),((98.0,73.95),[(98.0,84.0)]),((99.2,73.95),[(99.2,84.0)])]:
 prev=src
 for point in points: s(b,n,F,prev,point);prev=point
 v(b,n,prev)
s(b,n,B,(87.0,84.0),(104.0,84.0));v(b,n,(104.0,84.0));s(b,n,F,(104.0,84.0),(104.0,82.0));s(b,n,F,(104.0,82.0),(104.0,82.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
