"""Phase 24 bounded strategy 1: pair-owned physical launch channels.

This is deliberately one channel plan, not a centerline router: each pair is
assigned a layer and a reserved via/trace corridor before copper is emitted.
"""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ENVELOPE_STRATEGY1_PAIR_CHANNELS.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
nets=('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
sy={'REFCLK_P':70.4,'REFCLK_N':70.8,'LANE0_RXP':71.6,'LANE0_RXN':72.0,'LANE0_TXN':72.8,'LANE0_TXP':73.2}
pad={'REFCLK_P':('55',137.25),'REFCLK_N':('53',136.75),'LANE0_RXP':('43',134.25),'LANE0_RXN':('41',133.75),'LANE0_TXN':('47',135.25),'LANE0_TXP':('49',135.75)}
# Pair-owned corridors. RX and REF use B.Cu; TX uses F.Cu.
plan={'LANE0_RXP':(B,130.0,79.0,133.0),'LANE0_RXN':(B,131.0,80.0,132.0),'LANE0_TXN':(F,135.0,81.0,134.0),'LANE0_TXP':(F,136.0,82.0,136.0),'REFCLK_P':(B,138.0,84.0,139.0),'REFCLK_N':(B,139.0,85.0,138.0)}
b=pcbnew.LoadBoard(str(BASE)); jh=b.FindFootprintByReference('JH1'); j=b.FindFootprintByReference('J1'); assert jh and j
def seg(n,a,z,l):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
for name in nets:
 n=b.FindNet(name); assert n
 y=sy[name]; layer,cx,cy,tx=plan[name]
 hp=next(p for p in jh.Pads() if p.GetNetname()==name)
 # Accepted V1590 source segment ends at the original handoff; preserve it.
 via(n,85.,y)
 if layer == F:
  seg(n,(85.,y),(cx,y),F); seg(n,(cx,y),(cx,cy),F); via(n,cx,cy)
 else:
  seg(n,(85.,y),(cx,y),B); seg(n,(cx,y),(cx,cy),B); via(n,cx,cy)
 d=j.FindPadByNumber(pad[name][0]).GetPosition(); dx=pcbnew.ToMM(d.x)
 seg(n,(cx,cy),(dx,62.725),F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
