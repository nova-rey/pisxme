"""V689: translate the crystal micro-island left and rebuild its field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_U139_JOG_V687.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_CRYSTAL_LEFT_V689.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(fp,num):
 q=fp.FindPadByNumber(str(num)).GetPosition();return (pcbnew.ToMM(q.x),pcbnew.ToMM(q.y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
# Translate the complete crystal micro-island by 3 mm, preserving relative placement.
for ref in ('Y1','C1','C2'):
 fp=b.FindFootprintByReference(ref);p=fp.GetPosition();fp.SetPosition(p+P(-3,0))
for q in list(b.GetTracks()):
 if q.GetNetname() in ('XTAL_IN','XTAL_OUT'):b.RemoveNative(q)
for q in list(b.GetTracks()):
 if q.GetNetname()=='GND':
  a,z=q.GetStart(),q.GetEnd();pts={(round(pcbnew.ToMM(a.x),3),round(pcbnew.ToMM(a.y),3)),(round(pcbnew.ToMM(z.x),3),round(pcbnew.ToMM(z.y),3))}
  if pts & {(85.6,63.0),(85.6,63.8)}:b.RemoveNative(q)
for q in list(b.GetTracks()):
 if type(q).__name__!='PCB_VIA':continue
 p=q.GetPosition();xy0=(round(pcbnew.ToMM(p.x),3),round(pcbnew.ToMM(p.y),3))
 if q.GetNetname()=='GND' and xy0 in {(85.6,63.8),(91.6,63.8)}:b.RemoveNative(q)
ni=b.FindNet('XTAL_IN');no=b.FindNet('XTAL_OUT');ng=b.FindNet('GND')
yi=b.FindFootprintByReference('Y1');c1=b.FindFootprintByReference('C1');c2=b.FindFootprintByReference('C2')
yin=xy(yi,1);yout=xy(yi,2);c1p=xy(c1,1);c1g=xy(c1,2);c2p=xy(c2,1);c2g=xy(c2,2)
# Separate source escapes and ordinary-via layer changes, then short local cap joins.
t(b,ni,F,(94.05,67.2),(90,67.2));t(b,ni,F,(90,67.2),(90,65));v(b,ni,(90,65));t(b,ni,B,(90,65),(86.3,65));v(b,ni,(86.3,64));t(b,ni,F,(86.3,64),yin);t(b,ni,F,yin,c1p)
t(b,no,F,(94.05,67.6),(91,67.6));t(b,no,F,(91,67.6),(91,66));v(b,no,(91,66));t(b,no,B,(91,66),(86.8,66));v(b,no,(86.8,65));t(b,no,F,(86.8,65),yout);t(b,no,F,yout,c2p)
for pad,via in ((c1g,(c1g[0],c1g[1]+.8)),(c2g,(c2g[0],c2g[1]+.8))):
 v(b,ng,via);t(b,ng,F,pad,via)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
