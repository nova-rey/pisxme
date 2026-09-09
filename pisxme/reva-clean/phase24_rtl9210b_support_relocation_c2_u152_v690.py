"""V690: move C2 outboard and co-author the U1.52 3V3 branch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_U139_JOG_V687.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_C2_U152_V690.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(fp,num):
 q=fp.FindPadByNumber(str(num)).GetPosition();return (pcbnew.ToMM(q.x),pcbnew.ToMM(q.y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));c2=b.FindFootprintByReference('C2');c2.SetPosition(c2.GetPosition()+P(3,0))
for q in list(b.GetTracks()):
 if q.GetNetname()=='XTAL_OUT':b.RemoveNative(q)
for q in list(b.GetTracks()):
 if q.GetNetname()=='GND':
  a,z=q.GetStart(),q.GetEnd();pts={(round(pcbnew.ToMM(a.x),3),round(pcbnew.ToMM(a.y),3)),(round(pcbnew.ToMM(z.x),3),round(pcbnew.ToMM(z.y),3))}
  if pts & {(91.6,63.8)}:b.RemoveNative(q)
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and q.GetNetname()=='GND':
  p=q.GetPosition();ifxy=(round(pcbnew.ToMM(p.x),3),round(pcbnew.ToMM(p.y),3))
  if ifxy==(91.6,63.8):b.RemoveNative(q)
no=b.FindNet('XTAL_OUT');n3=b.FindNet('RTL_3V3');ng=b.FindNet('GND');yi=b.FindFootprintByReference('Y1');c2=b.FindFootprintByReference('C2')
yout=xy(yi,2);c2p=xy(c2,1);c2g=xy(c2,2)
t(b,no,F,(94.05,67.6),(90.8,67.6));t(b,no,F,(90.8,67.6),(90.8,68.6));v(b,no,(90.8,68.6));t(b,no,B,(90.8,68.6),(88.7,65.8));v(b,no,(88.7,65.8));t(b,no,F,(88.7,65.8),yout);t(b,no,F,yout,(92.5,62.0));t(b,no,F,(92.5,62.0),c2p)
v(b,ng,(c2g[0],c2g[1]+.8));t(b,ng,F,c2g,(c2g[0],c2g[1]+.8))
t(b,n3,F,(94.05,66.8),(92.0,66.8));t(b,n3,F,(92.0,66.8),(92.0,55.0));t(b,n3,F,(92.0,55.0),(103.0,55.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
