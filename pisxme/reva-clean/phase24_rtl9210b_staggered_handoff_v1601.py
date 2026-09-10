"""V1601: legally spaced staggered U1-to-handoff breakout."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb'
out=H/'PHASE24_RTL9210B_STAGGERED_HANDOFF_V1601.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
nets=('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
source_y={'REFCLK_P':70.4,'REFCLK_N':70.8,'LANE0_RXP':71.6,'LANE0_RXN':72.0,'LANE0_TXN':72.8,'LANE0_TXP':73.2}
new_y=dict(zip(nets,(68.,69.,70.,71.,72.,73.)))
branch_x=dict(zip(nets,(90.,89.,88.,87.,86.,85.)))
b=pcbnew.LoadBoard(str(base)); h=b.FindFootprintByReference('JH1'); assert h
def seg(n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
for name in nets:
 n=b.FindNet(name); assert n; sy=source_y[name]; yy=new_y[name]; bx=branch_x[name]
 pad=next(p for p in h.Pads() if p.GetNetname()==name); pad.SetPosition(P(85.,yy))
 old=next(q for q in b.GetTracks() if q.GetNetname()==name and q.GetLayer()==F and abs(pcbnew.ToMM(q.GetStart().x)-94.05)<.01)
 b.RemoveNative(old)
 seg(n,(94.05,sy),(bx,sy)); seg(n,(bx,sy),(bx,yy)); seg(n,(bx,yy),(85.,yy))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
