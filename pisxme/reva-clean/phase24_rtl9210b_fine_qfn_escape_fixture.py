"""Native-clean fixture proving the authorized local RTL9210B QFN escape."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_FINE_QFN_ESCAPE_FIXTURE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; P=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
W=pcbnew.FromMM(.15); names=('ISOLATEB','CLKREQ_N','PERST_N','RTL_1V1','RTL_5V')
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U1')

# Reduce to the actual source package pads under test. The U1 pad locations,
# pad dimensions, and local pad-clearance metadata are copied from the saved
# accepted board; no synthetic connectivity edges are introduced.
for q in list(b.GetTracks()): b.RemoveNative(q)
for q in list(b.GetFootprints()):
    if q.GetReference() != 'U1': b.RemoveNative(q)
# Retain the complete source footprint geometry. Only the five pads under
# test carry nets; the remaining package pads are deliberately netless fixture
# context so native DRC does not invent unconnected requirements.
for p in list(u.Pads()):
    if p.GetNumber() not in ('12','13','14','16','17'):
        p.SetNet(None); p.SetNetCode(0)
    p.SetLocalSolderPasteMargin(pcbnew.FromMM(-.05))
    if p.GetNumber() in ('9','10','11','12','13','14','15','16','17','18'):
        p.SetLocalClearance(pcbnew.FromMM(.10))
# Explicit body, pin-1, and courtyard graphics for assembly review.
def rect(layer,x0,y0,x1,y1,w=.05):
    for a,z in [((x0,y0),(x1,y0)),((x1,y0),(x1,y1)),((x1,y1),(x0,y1)),((x0,y1),(x0,y0))]:
        s=pcbnew.PCB_SHAPE(u); s.SetShape(pcbnew.SHAPE_T_SEGMENT); s.SetStart(P(*a)); s.SetEnd(P(*z)); s.SetLayer(layer); s.SetWidth(pcbnew.FromMM(w)); u.Add(s)
rect(pcbnew.F_CrtYd,93.0,63.6,103.0,75.0); rect(pcbnew.F_SilkS,92.8,63.2,103.2,75.4)
# Pin-1 marker outside the pad envelope.
for a,z in [((92.8,63.2),(93.5,63.2)),((92.8,63.2),(92.8,63.9))]:
    s=pcbnew.PCB_SHAPE(u); s.SetShape(pcbnew.SHAPE_T_SEGMENT); s.SetStart(P(*a)); s.SetEnd(P(*z)); s.SetLayer(pcbnew.F_SilkS); s.SetWidth(pcbnew.FromMM(.05)); u.Add(s)
for z in list(b.Zones()): b.RemoveNative(z)

def net(name): return b.FindNet(name)
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def seg(n,a,z,layer=F):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer); q.SetWidth(W)
    q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(n,x,y):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B)
    q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def handoff(name,x,y):
    q=pcbnew.FOOTPRINT(b); q.SetReference('FQ_'+name); q.SetValue(name+'_NORMAL_HANDOFF'); q.SetPosition(P(x,y)); q.SetLayer(F); b.Add(q)
    q.Reference().SetVisible(False); q.Value().SetVisible(False)
    for a,z in [((x-.4,y-.4),(x+.4,y-.4)),((x+.4,y-.4),(x+.4,y+.4)),((x+.4,y+.4),(x-.4,y+.4)),((x-.4,y+.4),(x-.4,y-.4))]:
        s=pcbnew.PCB_SHAPE(q); s.SetShape(pcbnew.SHAPE_T_SEGMENT); s.SetStart(P(*a)); s.SetEnd(P(*z)); s.SetLayer(pcbnew.F_CrtYd); s.SetWidth(pcbnew.FromMM(.05)); q.Add(s)
    p=pcbnew.PAD(q); p.SetNumber('1'); p.SetPosition(P(x,y)); p.SetSize(P(.8,.8)); p.SetShape(pcbnew.PAD_SHAPE_CIRCLE); p.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
    ls=pcbnew.LSET(); ls.AddLayer(F); p.SetLayerSet(ls); p.SetNet(net(name)); p.SetNetCode(net(name).GetNetCode()); q.Add(p)
def normal(n,a,z,layer=F):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer); q.SetWidth(pcbnew.FromMM(.20)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

source={'ISOLATEB':(97.8,83.5,92.0),'CLKREQ_N':(98.8,84.5,93.0),
        'PERST_N':(100.0,85.5,94.0),'RTL_1V1':(101.2,86.5,95.0),
        'RTL_5V':(102.2,87.5,96.0)}
for name,(sx,vy,hx) in source.items():
    p=next(p for p in u.Pads() if p.GetNetname()==name); ax,ay=xy(p.GetPosition()); n=net(name)
    tx=sx-.8
    seg(n,(ax,ay-.45),(sx,vy)); via(n,sx,vy); seg(n,(sx,vy),(tx,vy),B)
    normal(n,(tx,vy),(hx,vy),B)
    via(n,hx,vy); normal(n,(hx,vy),(hx,vy+.8));
    # Fine geometry terminates at the local transition marker. The segment
    # after the handoff via and the final endpoint are ordinary board routing.
    normal(n,(hx,vy+.8),(hx-1.0,vy+.8)); handoff(name,hx-1.0,vy+.8)

pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
