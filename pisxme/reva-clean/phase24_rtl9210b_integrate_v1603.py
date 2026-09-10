"""Integrate the accepted V1603 launch network into the full V1601 support board."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_STAGGERED_HANDOFF_V1601.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_PATHB_V1603_INTEGRATED.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)
P = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))
names = ('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
source_y = {'REFCLK_P':68.,'REFCLK_N':69.,'LANE0_RXP':70.,'LANE0_RXN':71.,'LANE0_TXN':72.,'LANE0_TXP':73.}
channel = {'LANE0_RXN':44.,'LANE0_RXP':45.,'LANE0_TXN':46.,'LANE0_TXP':47.,'REFCLK_N':48.,'REFCLK_P':49.}
target = {'LANE0_RXN':133.75,'LANE0_RXP':134.25,'LANE0_TXN':135.25,'LANE0_TXP':135.75,'REFCLK_N':136.75,'REFCLK_P':137.25}
lane_x = dict(zip(names, (67.,68.,69.,70.,71.,72.)))
via_x = {'LANE0_RXN':132.,'LANE0_RXP':133.5,'LANE0_TXN':134.5,'LANE0_TXP':135.5,'REFCLK_N':141.50,'REFCLK_P':142.50}
final_y = {'LANE0_RXN':59.0,'LANE0_RXP':58.0,'LANE0_TXN':57.0,'LANE0_TXP':56.0,'REFCLK_N':41.0,'REFCLK_P':42.0}
b = pcbnew.LoadBoard(str(BASE))
def seg(n, a, z, layer):
    if a == z: return
    q = pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer); q.SetWidth(W)
    q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(n, x, y):
    q = pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30))
    q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
for name in names:
    n = b.FindNet(name); sy = source_y[name]; yy = channel[name]; x = lane_x[name]; vx = via_x[name]; tx = target[name]
    # JH1 is the accepted source funnel.  The F/B transition is outside its
    # pad field; the rest is the accepted V1603 channel/launch geometry.
    via(n, 84., sy); seg(n, (85.,sy), (84.,sy), F); seg(n, (84.,sy), (x,sy), B); via(n,x,sy)
    seg(n, (x,sy), (x,yy), F); via(n,x,yy); seg(n, (x,yy), (vx,yy), B); via(n,vx,yy)
    fy = final_y[name]
    if name == 'REFCLK_N':
        # Keep the reference leg's long approach on B.Cu and transition at
        # the target x.  This avoids crossing the adjacent REFCLK_P dogbone.
        seg(n, (vx,yy), (vx,fy), B); seg(n, (vx,fy), (tx,fy), B)
        via(n, tx, fy); seg(n, (tx,fy), (tx,62.725), F)
    else:
        seg(n, (vx,yy), (vx,fy), F)
        seg(n, (vx,fy), (tx,fy), F); seg(n, (tx,fy), (tx,62.725), F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT)); print(OUT)
