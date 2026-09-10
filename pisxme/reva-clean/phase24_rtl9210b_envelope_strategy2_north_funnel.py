"""Phase 24 bounded strategy 2: north-perimeter physical funnel."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ENVELOPE_STRATEGY2_NORTH_FUNNEL.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
order=('LANE0_RXN','LANE0_RXP','LANE0_TXN','LANE0_TXP','REFCLK_N','REFCLK_P')
sy={'REFCLK_P':70.4,'REFCLK_N':70.8,'LANE0_RXP':71.6,'LANE0_RXN':72.0,'LANE0_TXN':72.8,'LANE0_TXP':73.2}
ty={'LANE0_RXN':133.75,'LANE0_RXP':134.25,'LANE0_TXN':135.25,'LANE0_TXP':135.75,'REFCLK_N':136.75,'REFCLK_P':137.25}
srcx=dict(zip(order,(69.,70.,71.,72.,73.,74.)))
top_y=dict(zip(order,(44.,45.,46.,47.,48.,49.)))
via_x=dict(zip(order,(132.,133.,134.,135.,136.,137.)))
b=pcbnew.LoadBoard(str(BASE)); jh=b.FindFootprintByReference('JH1'); j=b.FindFootprintByReference('J1'); assert jh and j
def seg(n,a,z,l):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
for name in order:
 n=b.FindNet(name); assert n; y=sy[name]; x=srcx[name]; ch=top_y[name]; vx=via_x[name]; dx=ty[name]
 hp=next(p for p in jh.Pads() if p.GetNetname()==name)
 seg(n,(85.,y),(x,y),F); seg(n,(x,y),(x,ch),F); via(n,x,ch)
 seg(n,(x,ch),(vx,ch),B); via(n,vx,ch); seg(n,(vx,ch),(dx,62.725),F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
