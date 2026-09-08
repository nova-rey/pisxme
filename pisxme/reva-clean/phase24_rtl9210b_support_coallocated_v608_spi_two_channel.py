"""V608: coordinate SPISI and SPISO3 endpoint transitions."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V595_CLKREQ_LOCAL.kicad_pcb';out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V608_SPI_TWO_CHANNEL.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base))
for name,src,ep,x in [('SPISI',(102.05,58.8),(96.1,70.0),94.5),('SPISO3',(102.05,60.4),(98.5,70.0),96.5)]:
 n=b.FindNet(name); y=src[1];s(b,n,F,src,(99.5,y));v(b,n,(99.5,y));s(b,n,B,(99.5,y),(x,y));s(b,n,B,(x,y),(x,68.5));v(b,n,(x,68.5));s(b,n,F,(x,68.5),(ep[0] if name=='SPISI' else x,68.5));s(b,n,F,(ep[0] if name=='SPISI' else x,68.5),ep)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
