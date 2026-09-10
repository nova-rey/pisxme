"""V1602: launch from the validated staggered U1 handoff through north channels."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_STAGGERED_HANDOFF_V1601.kicad_pcb'
out=H/'PHASE24_RTL9210B_STAGGERED_NORTH_LAUNCH_V1602.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
order=('LANE0_RXN','LANE0_RXP','LANE0_TXN','LANE0_TXP','REFCLK_N','REFCLK_P')
hy={'REFCLK_P':68.,'REFCLK_N':69.,'LANE0_RXP':70.,'LANE0_RXN':71.,'LANE0_TXN':72.,'LANE0_TXP':73.}
sx=dict(zip(order,(79.,80.,81.,82.,83.,84.)))
ty=dict(zip(order,(44.,45.,46.,47.,48.,49.)))
vx=dict(zip(order,(132.,133.,134.,135.,136.,137.)))
dx={'LANE0_RXN':133.75,'LANE0_RXP':134.25,'LANE0_TXN':135.25,'LANE0_TXP':135.75,'REFCLK_N':136.75,'REFCLK_P':137.25}
b=pcbnew.LoadBoard(str(base)); jh=b.FindFootprintByReference('JH1'); j=b.FindFootprintByReference('J1'); assert jh and j
def seg(n,a,z,l):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
for name in order:
 n=b.FindNet(name); assert n; y=hy[name]; x=sx[name]; ch=ty[name]; x2=vx[name]
 via(n,87.,y); seg(n,(85.,y),(87.,y),F); seg(n,(87.,y),(x,y),F); seg(n,(x,y),(x,ch),F); via(n,x,ch)
 seg(n,(x,ch),(x2,ch),B); via(n,x2,ch); seg(n,(x2,ch),(dx[name],62.725),F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
