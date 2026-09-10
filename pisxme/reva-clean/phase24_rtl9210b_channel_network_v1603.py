"""V1603: alternating-layer channel network from staggered handoff to J1."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_STAGGERED_HANDOFF_V1601.kicad_pcb'
out=H/'PHASE24_RTL9210B_CHANNEL_NETWORK_V1603.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
names=('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
source_y={'REFCLK_P':68.,'REFCLK_N':69.,'LANE0_RXP':70.,'LANE0_RXN':71.,'LANE0_TXN':72.,'LANE0_TXP':73.}
channel={'LANE0_RXN':44.,'LANE0_RXP':45.,'LANE0_TXN':46.,'LANE0_TXP':47.,'REFCLK_N':48.,'REFCLK_P':49.}
target={'LANE0_RXN':(133.75,'41'),'LANE0_RXP':(134.25,'43'),'LANE0_TXN':(135.25,'47'),'LANE0_TXP':(135.75,'49'),'REFCLK_N':(136.75,'53'),'REFCLK_P':(137.25,'55')}
lane_x=dict(zip(names,(67.,68.,69.,70.,71.,72.)))
via_x={'LANE0_RXN':132.,'LANE0_RXP':134.25,'LANE0_TXN':135.25,'LANE0_TXP':136.25,'REFCLK_N':137.25,'REFCLK_P':138.25}
b=pcbnew.LoadBoard(str(base))
for q in list(b.GetTracks()):
    if q.GetNetname() not in names: b.RemoveNative(q)
for fp in list(b.GetFootprints()):
    if fp.GetReference() not in ('U1','J1','JH1'): b.RemoveNative(fp)
def seg(n,a,z,l):
 if a == z: return
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
for name in names:
 n=b.FindNet(name); assert n; sy=source_y[name]; yy=channel[name]; x=lane_x[name]; vx=via_x[name]; tx=target[name][0]
 # F.Cu handoff dogbone, B.Cu source sorting, F.Cu isolated vertical, B.Cu target channel.
 via(n,84.,sy); seg(n,(85.,sy),(84.,sy),F); seg(n,(84.,sy),(x,sy),B); via(n,x,sy)
 seg(n,(x,sy),(x,yy),F); via(n,x,yy); seg(n,(x,yy),(vx,yy),B)
 # Separated F.Cu connector approaches.  Via x positions are monotonic and
 # each is at or to the right of the preceding pad x, so no final approach
 # corridor can intersect a later pad's vertical dogbone.
 final_y={'LANE0_RXN':59.0,'LANE0_RXP':59.6,'LANE0_TXN':60.2,
          'LANE0_TXP':60.8,'REFCLK_N':61.4,'REFCLK_P':62.0}[name]
 via(n,vx,yy); seg(n,(vx,yy),(vx,final_y),F)
 seg(n,(vx,final_y),(tx,final_y),F); seg(n,(tx,final_y),(tx,62.725),F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
