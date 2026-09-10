"""Source-row funnel probe with reserved physical via/corridor envelopes."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SOURCE_ROW_STAGGERED_FUNNEL.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; P=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
W=pcbnew.FromMM(.20); names=('ISOLATEB','CLKREQ_N','PERST_N','RTL_1V1','RTL_5V')
b=pcbnew.LoadBoard(str(BASE))

def n(name): return b.FindNet(name)
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)

# Remove only the source-field copper for the five coupled departures.  The
# remote board circuitry is retained; this probe owns no production copper.
for q in list(b.GetTracks()):
    if q.GetNetname() not in names: continue
    ps=[q.GetPosition()] if isinstance(q,pcbnew.PCB_VIA) else [q.GetStart(),q.GetEnd()]
    if any(95<=xy(p)[0]<=112 and 72.5<=xy(p)[1]<=82.5 for p in ps): b.RemoveNative(q)

def seg(net,a,z,layer=F):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
    q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
def via(net,x,y):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B)
    q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
def handoff(name,x,y):
    q=pcbnew.FOOTPRINT(b); q.SetReference('FH_'+name); q.SetValue(name+'_SOURCE_HANDOFF'); q.SetPosition(P(x,y)); q.SetLayer(F); b.Add(q)
    p=pcbnew.PAD(q); p.SetNumber('1'); p.SetPosition(P(x,y)); p.SetSize(P(.8,.8)); p.SetShape(pcbnew.PAD_SHAPE_CIRCLE); p.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
    ls=pcbnew.LSET(); ls.AddLayer(F); p.SetLayerSet(ls); p.SetNet(n(name)); p.SetNetCode(n(name).GetNetCode()); q.Add(p)

# Reserve one complete B.Cu horizontal channel per net.  The via rows are
# 1.0 mm apart, well outside the 0.4-mm QFN pitch and explicit 0.6-mm via
# envelopes.  Handoffs are intentionally west of the QFN field.
source={'ISOLATEB':(97.8,83.5,92.0),'CLKREQ_N':(100.6,84.5,93.0),
        'PERST_N':(101.4,85.5,94.0),'RTL_1V1':(102.2,86.5,95.0),
        'RTL_5V':(103.0,87.5,96.0)}
for name,(sx,vy,hx) in source.items():
    u=b.FindFootprintByReference('U1'); p=next(p for p in u.Pads() if p.GetNetname()==name)
    ax,ay=xy(p.GetPosition())
    # Pad-end escape is straight and kept on F.Cu; no diagonal enters the
    # 0.4-mm pitch row.  The handoff pad is a real physical endpoint.
    seg(n(name),(ax,ay-.45),(sx,vy),F); via(n(name),sx,vy)
    seg(n(name),(sx,vy),(hx,vy),B); via(n(name),hx,vy)
    seg(n(name),(hx,vy),(hx,vy+.8),F); handoff(name,hx,vy+.8)

pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
