"""V1583: fixed-orientation REFCLK pair on an outer board corridor."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U155_REHOME_V1517.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_REFCLK_OUTER_CORRIDOR_V1583.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for n,src,xout,yout,xleft,ytop,xj in (
 ('REFCLK_P',(94.05,70.4),91.5,78.5,72.0,41.5,137.25),
 ('REFCLK_N',(94.05,70.8),92.5,79.2,70.8,42.2,136.75),
):
 net=b.FindNet(n); assert net
 tr(b,net,F,src,(xout,src[1])); tr(b,net,F,(xout,src[1]),(xout,yout)); via(b,net,xout,yout)
 tr(b,net,B,(xout,yout),(xleft,yout)); via(b,net,xleft,yout)
 tr(b,net,F,(xleft,yout),(xleft,ytop)); via(b,net,xleft,ytop)
 tr(b,net,B,(xleft,ytop),(xj-1.0,ytop)); tr(b,net,B,(xj-1.0,ytop),(xj-1.0,60.5)); via(b,net,xj-1.0,60.5)
 tr(b,net,F,(xj-1.0,60.5),(xj,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
