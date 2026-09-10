"""V1599: disposable polarity-ordered two-layer launch discriminator."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb'
out=H/'PHASE24_RTL9210B_POLARITY_ORDERED_LAUNCH_V1599.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
allnets=('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
sy={'REFCLK_P':70.4,'REFCLK_N':70.8,'LANE0_RXP':71.6,'LANE0_RXN':72.0,'LANE0_TXN':72.8,'LANE0_TXP':73.2}
# Disposable pad remap swaps the RX and REFCLK differential polarities.
target={'LANE0_RXP':133.75,'LANE0_RXN':134.25,'LANE0_TXN':135.25,'LANE0_TXP':135.75,'REFCLK_P':136.75,'REFCLK_N':137.25}
hx={'LANE0_RXP':80.0,'LANE0_RXN':81.0,'LANE0_TXN':82.0,'LANE0_TXP':83.0,'REFCLK_P':84.0,'REFCLK_N':85.0}
b=pcbnew.LoadBoard(str(base))
# Strip unrelated copper so this is a launch topology discriminator.
for q in list(b.GetTracks()):
    if q.GetNetname() not in allnets: b.RemoveNative(q)
j=b.FindFootprintByReference('J1'); assert j
for num,net in (('41','LANE0_RXP'),('43','LANE0_RXN'),('53','REFCLK_P'),('55','REFCLK_N')):
    j.FindPadByNumber(num).SetNet(b.FindNet(net))
jh=b.FindFootprintByReference('JH1'); assert jh
def via(net,x,y):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
def seg(net,a,z,l):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
for name in allnets:
    n=b.FindNet(name); assert n; y=sy[name]; x=hx[name]
    pad=next(p for p in jh.Pads() if p.GetNetname()==name); pad.SetPosition(P(x,y))
    src=next(q for q in b.GetTracks() if q.GetNetname()==name and q.GetLayer()==F)
    src.SetEnd(P(x,y))
    if name.startswith('LANE0_'):
        # Ordered lane paths remain on F.Cu; the polarity-swapped RX pair is monotonic.
        d=j.FindPadByNumber({'LANE0_RXP':'41','LANE0_RXN':'43','LANE0_TXN':'47','LANE0_TXP':'49'}[name]).GetPosition()
        seg(n,(x,y),(pcbnew.ToMM(d.x),62.725),F)
    else:
        # REFCLK uses a separate B.Cu corridor and offset connector vias.
        vx={'REFCLK_P':136.0,'REFCLK_N':137.0}[name]
        via(n,x,y); seg(n,(x,y),(vx,80.0),B); via(n,vx,80.0); seg(n,(vx,80.0),(vx,62.725),F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
