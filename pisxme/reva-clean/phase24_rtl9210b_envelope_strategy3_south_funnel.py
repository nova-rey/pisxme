"""Phase 24 bounded strategy 3: south-perimeter physical funnel."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ENVELOPE_STRATEGY3_SOUTH_FUNNEL.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
order=('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
sy={'REFCLK_P':70.4,'REFCLK_N':70.8,'LANE0_RXP':71.6,'LANE0_RXN':72.0,'LANE0_TXN':72.8,'LANE0_TXP':73.2}
ty={'LANE0_RXP':134.25,'LANE0_RXN':133.75,'LANE0_TXN':135.25,'LANE0_TXP':135.75,'REFCLK_P':137.25,'REFCLK_N':136.75}
sx=dict(zip(order,(67.,68.,69.,70.,71.,72.)))
ch=dict(zip(order,(88.,89.,90.,91.,92.,93.)))
vx=dict(zip(order,(130.,131.,132.,133.,134.,135.)))
b=pcbnew.LoadBoard(str(BASE)); jh=b.FindFootprintByReference('JH1'); j=b.FindFootprintByReference('J1'); assert jh and j
def seg(n,a,z,l):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
for name in order:
 n=b.FindNet(name); assert n; y=sy[name]; x=sx[name]; yy=ch[name]; xvia=vx[name]; dx=ty[name]
 src=next(q for q in b.GetTracks() if q.GetNetname()==name and q.GetLayer()==F)
 src.SetEnd(P(x,y)); seg(n,(85.,y),(x,y),F); via(n,x,y)
 via(n,x,yy); seg(n,(x,y),(x,yy),B); seg(n,(x,yy),(xvia,yy),B); via(n,xvia,yy); seg(n,(xvia,yy),(dx,62.725),F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
