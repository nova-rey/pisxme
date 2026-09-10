"""V1598: ordered connector via row with direct offset dogbones."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb'
out=H/'PHASE24_RTL9210B_CONNECTOR_OFFSET_V1598.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
NETS=('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
source_y={'REFCLK_P':70.4,'REFCLK_N':70.8,'LANE0_RXP':71.6,'LANE0_RXN':72.0,'LANE0_TXN':72.8,'LANE0_TXP':73.2}
target={'LANE0_RXN':133.75,'LANE0_RXP':134.25,'LANE0_TXN':135.25,'LANE0_TXP':135.75,'REFCLK_N':136.75,'REFCLK_P':137.25}
handoff={'LANE0_RXN':80.0,'LANE0_RXP':81.0,'LANE0_TXN':82.0,'LANE0_TXP':83.0,'REFCLK_N':84.0,'REFCLK_P':85.0}
via_x={'LANE0_RXN':132.0,'LANE0_RXP':133.0,'LANE0_TXN':134.0,'LANE0_TXP':135.0,'REFCLK_N':136.0,'REFCLK_P':137.0}
b=pcbnew.LoadBoard(str(base))
for q in list(b.GetTracks()):
    if q.GetNetname() not in NETS: b.RemoveNative(q)
jh=b.FindFootprintByReference('JH1'); assert jh
for name in NETS:
    n=b.FindNet(name); assert n
    y=source_y[name]; hx=handoff[name]; vx=via_x[name]; tx=target[name]
    pad=next(p for p in jh.Pads() if p.GetNetname()==name); pad.SetPosition(P(hx,y))
    src=next(q for q in b.GetTracks() if q.GetNetname()==name and q.GetLayer()==F)
    src.SetEnd(P(hx,y))
    def addvia(x,yy):
        q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,yy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
    def seg(a,z,l):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
    addvia(hx,y); seg((hx,y),(vx,84.0),B); addvia(vx,84.0); seg((vx,84.0),(tx,62.725),F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
