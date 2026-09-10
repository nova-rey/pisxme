"""Apply the accepted V1601/V1603 high-speed launch to the clean V1517 support baseline."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_REHOME_U152_V1523.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); P=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
N=('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
src={'REFCLK_P':(61,70.4),'REFCLK_N':(62,70.8),'LANE0_RXP':(64,71.6),'LANE0_RXN':(65,72.0),'LANE0_TXN':(67,72.8),'LANE0_TXP':(68,73.2)}
handoff_y={'REFCLK_P':68.,'REFCLK_N':69.,'LANE0_RXP':70.,'LANE0_RXN':71.,'LANE0_TXN':72.,'LANE0_TXP':73.}
channel={'LANE0_RXN':44.,'LANE0_RXP':45.,'LANE0_TXN':46.,'LANE0_TXP':47.,'REFCLK_N':48.,'REFCLK_P':49.}
lane_x=dict(zip(N,(67.,68.,69.,70.,71.,72.))); vx={'LANE0_RXN':132.,'LANE0_RXP':133.5,'LANE0_TXN':134.5,'LANE0_TXP':135.5,'REFCLK_N':141.5,'REFCLK_P':142.5}; fy={'LANE0_RXN':59.,'LANE0_RXP':58.,'LANE0_TXN':57.,'LANE0_TXP':56.,'REFCLK_N':41.,'REFCLK_P':42.}; tx={'LANE0_RXN':133.75,'LANE0_RXP':134.25,'LANE0_TXN':135.25,'LANE0_TXP':135.75,'REFCLK_N':136.75,'REFCLK_P':137.25}
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
    pts=[q.GetPosition()] if isinstance(q,pcbnew.PCB_VIA) else [q.GetStart(),q.GetEnd()]
    local_1v1=q.GetNetname()=='RTL_1V1' and any(87<=pcbnew.ToMM(p.x)<=95 and 68<=pcbnew.ToMM(p.y)<=72 for p in pts)
    if q.GetNetname() in N or local_1v1: b.RemoveNative(q)
u0=b.FindFootprintByReference('U1')
for p in u0.Pads(): p.SetLocalClearance(pcbnew.FromMM(.15))
fp=pcbnew.FOOTPRINT(b); fp.SetReference('JH1'); fp.SetValue('QFN_ESCAPE_HANDOFF'); fp.SetPosition(P(0,0)); fp.SetLayer(F); b.Add(fp)
for name in N:
    p=pcbnew.PAD(fp); p.SetNumber(str(src[name][0])); p.SetPosition(P(85,handoff_y[name])); p.SetSize(P(.6,.2)); p.SetShape(pcbnew.PAD_SHAPE_RECT); p.SetAttribute(pcbnew.PAD_ATTRIB_SMD); ls=pcbnew.LSET(); ls.AddLayer(F); p.SetLayerSet(ls); net=b.FindNet(name); p.SetNet(net); p.SetNetCode(net.GetNetCode()); fp.Add(p)
def seg(n,a,z,l):
    if a==z:return
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(n,x,y):
    if any(isinstance(q,pcbnew.PCB_VIA) and q.GetNetCode()==n.GetNetCode() and q.GetPosition()==P(x,y) for q in b.GetTracks()): return
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
for name in N:
    net=b.FindNet(name); num,_=src[name]; sy=handoff_y[name]; x=lane_x[name]; yy=channel[name]; v=vx[name]; target=tx[name]
    u=b.FindFootprintByReference('U1'); up=next(p for p in u.Pads() if p.GetNumber()==str(num)); a=up.GetPosition(); ax,ay=pcbnew.ToMM(a.x),pcbnew.ToMM(a.y)
    # Accepted V1601 staggered source handoff.
    if name=='REFCLK_P': seg(net,(ax,ay),(90,70.4),F); seg(net,(90,70.4),(90,68),F); seg(net,(90,68),(85,68),F)
    elif name=='REFCLK_N': seg(net,(ax,ay),(89,70.8),F); seg(net,(89,70.8),(89,69),F); seg(net,(89,69),(85,69),F)
    elif name=='LANE0_RXP': seg(net,(ax,ay),(88,71.6),F); seg(net,(88,71.6),(88,70),F); seg(net,(88,70),(85,70),F)
    elif name=='LANE0_RXN': seg(net,(ax,ay),(87,72),F); seg(net,(87,72),(87,71),F); seg(net,(87,71),(85,71),F)
    elif name=='LANE0_TXN':
        seg(net,(ax,ay),(92.5,72.8),F); seg(net,(92.5,72.8),(92.5,74),F); via(net,92.5,74); seg(net,(92.5,74),(86,74),B); via(net,86,74); seg(net,(86,74),(86,72),F); seg(net,(86,72),(85,72),F)
    else:
        seg(net,(ax,ay),(93.5,73.2),F); seg(net,(93.5,73.2),(93.5,75),F); via(net,93.5,75); seg(net,(93.5,75),(85,75),B); via(net,85,75); seg(net,(85,75),(85,73),F)
    via(net,84,sy); seg(net,(85,sy),(84,sy),F); seg(net,(84,sy),(x,sy),B); via(net,x,sy); seg(net,(x,sy),(x,yy),F); via(net,x,yy); seg(net,(x,yy),(v,yy),B)
    if name != 'REFCLK_N': via(net,v,yy)
    if name=='REFCLK_N':
        seg(net,(v,yy),(v,fy[name]),B); seg(net,(v,fy[name]),(target,fy[name]),B); via(net,target,fy[name]); seg(net,(target,fy[name]),(target,62.725),F)
    else:
        seg(net,(v,yy),(v,fy[name]),F); seg(net,(v,fy[name]),(target,fy[name]),F); seg(net,(target,fy[name]),(target,62.725),F)
# Reclose RTL_1V1 on the east-side shelf between the QFN pads and exposed pad.
one=b.FindNet('RTL_1V1'); seg(one,(94.05,68),(95.2,68),F); seg(one,(95.2,68),(95.2,66.05),F); seg(one,(94.05,70),(95.2,70),F); seg(one,(95.2,70),(95.2,68),F); seg(one,(94.05,71.2),(95.2,71.2),F); seg(one,(95.2,71.2),(95.2,70),F)
# The old west collector was orphaned when the source field was cleared; it
# is not connected to any live pad or support load and is removed explicitly.
for q in list(b.GetTracks()):
    if q.GetNetname()=='RTL_1V1' and isinstance(q,pcbnew.PCB_TRACK) and q.GetLayer()==B and ((pcbnew.ToMM(q.GetStart().x),pcbnew.ToMM(q.GetStart().y))==(88.,58.) or (pcbnew.ToMM(q.GetEnd().x),pcbnew.ToMM(q.GetEnd().y))==(88.,58.)): b.RemoveNative(q)
for q in list(b.GetTracks()):
    if q.GetNetname()=='RTL_1V1' and isinstance(q,pcbnew.PCB_VIA) and (pcbnew.ToMM(q.GetPosition().x),pcbnew.ToMM(q.GetPosition().y))==(99.,58.): b.RemoveNative(q)
for q in list(b.GetTracks()):
    if q.GetNetname()=='RTL_1V1' and isinstance(q,pcbnew.PCB_TRACK) and q.GetLayer()==F and pcbnew.ToMM(q.GetStart().x)==99 and pcbnew.ToMM(q.GetStart().y)==58 and pcbnew.ToMM(q.GetEnd().x)==99 and pcbnew.ToMM(q.GetEnd().y)==60.5: b.RemoveNative(q)
for q in list(b.GetTracks()):
    if q.GetNetname()=='RTL_1V1' and isinstance(q,pcbnew.PCB_TRACK) and q.GetLayer()==F and pcbnew.ToMM(q.GetStart().x)==99 and pcbnew.ToMM(q.GetStart().y)==60.5 and pcbnew.ToMM(q.GetEnd().x)==112 and pcbnew.ToMM(q.GetEnd().y)==60.5: b.RemoveNative(q)
for q in list(b.GetTracks()):
    if q.GetNetname()=='RTL_1V1' and isinstance(q,pcbnew.PCB_TRACK) and q.GetLayer()==F and pcbnew.ToMM(q.GetStart().x)==112 and pcbnew.ToMM(q.GetStart().y)==60.5 and pcbnew.ToMM(q.GetEnd().x)==112 and pcbnew.ToMM(q.GetEnd().y)==64.8: b.RemoveNative(q)
for q in list(b.GetTracks()):
    if q.GetNetname()=='RTL_1V1' and isinstance(q,pcbnew.PCB_VIA) and (pcbnew.ToMM(q.GetPosition().x),pcbnew.ToMM(q.GetPosition().y))==(112.,64.8): b.RemoveNative(q)
inn=b.FindNet('XTAL_IN'); seg(inn,(94.05,67.2),(92.6,67.2),F); seg(inn,(92.6,67.2),(92.6,66.2),F); via(inn,92.6,66.2); seg(inn,(92.6,66.2),(88,66.2),B); seg(inn,(88,66.2),(88,63.2),B); via(inn,88,63.2); seg(inn,(88,63.2),(88,62),F); seg(inn,(88,62),(88,59),F)
out=b.FindNet('XTAL_OUT'); seg(out,(94.05,67.6),(92,67.6),F); seg(out,(92,67.6),(92,62.8),F); seg(out,(92,62.8),(91,62.8),F); seg(out,(91,62.8),(91,62),F); seg(out,(91,62),(91,60.5),F); seg(out,(91,60.5),(89.4,59),F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
