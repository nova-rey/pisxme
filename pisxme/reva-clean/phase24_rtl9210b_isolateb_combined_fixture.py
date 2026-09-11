"""Disposable combined U1.12-to-MIC2545A support geometry proof."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ISOLATEB_COMBINED_FIXTURE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; P=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); W=pcbnew.FromMM(.20); FW=pcbnew.FromMM(.15)
u=b.FindFootprintByReference('U1')
for t in list(b.GetTracks()): b.RemoveNative(t)
for f in list(b.GetFootprints()):
    if f.GetReference()!='U1': b.RemoveNative(f)
for s in list(b.GetDrawings()):
    if s.GetLayer()==pcbnew.Edge_Cuts: b.RemoveNative(s)
for z in list(b.Zones()): b.RemoveNative(z)
for p in u.Pads():
    if p.GetNumber()!='12': p.SetNet(None); p.SetNetCode(0)
    p.SetLocalClearance(pcbnew.FromMM(.15))
def N(name):
    n=b.FindNet(name)
    if n:return n
    n=pcbnew.NETINFO_ITEM(b,name); b.Add(n); return n
iso,rail,load,gnd,ilim=N('ISOLATEB'),N('RTL_3V3'),N('SSD_3V3'),N('GND'),N('MIC2545_ILIM')
def fp(ref,val,x,y):
    q=pcbnew.FOOTPRINT(b); q.SetReference(ref); q.SetValue(val); q.SetPosition(P(x,y)); q.SetLayer(F); b.Add(q); return q
def pad(q,num,x,y,n,sx=1.55,sy=.60):
    p=pcbnew.PAD(q); p.SetNumber(str(num)); p.SetPosition(P(x,y)); p.SetSize(P(sx,sy)); p.SetShape(pcbnew.PAD_SHAPE_ROUNDRECT); p.SetRoundRectRadiusRatio(.18); p.SetAttribute(pcbnew.PAD_ATTRIB_SMD); ls=pcbnew.LSET();ls.AddLayer(F);p.SetLayerSet(ls);p.SetNet(n);p.SetNetCode(n.GetNetCode());q.Add(p);return p
def tr(n,a,z,l=F,w=W):
    q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(w);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(n,x,y):
    q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def rect(q,x0,y0,x1,y1,layer):
    for a,z in [((x0,y0),(x1,y0)),((x1,y0),(x1,y1)),((x1,y1),(x0,y1)),((x0,y1),(x0,y0))]:
        s=pcbnew.PCB_SHAPE(q);s.SetShape(pcbnew.SHAPE_T_SEGMENT);s.SetStart(P(*a));s.SetEnd(P(*z));s.SetLayer(layer);s.SetWidth(pcbnew.FromMM(.05));q.Add(s)
def edge(x0,y0,x1,y1):
    for a,z in [((x0,y0),(x1,y0)),((x1,y0),(x1,y1)),((x1,y1),(x0,y1)),((x0,y1),(x0,y0))]:
        s=pcbnew.PCB_SHAPE(b);s.SetShape(pcbnew.SHAPE_T_SEGMENT);s.SetStart(P(*a));s.SetEnd(P(*z));s.SetLayer(pcbnew.Edge_Cuts);s.SetWidth(pcbnew.FromMM(.05));b.Add(s)
u3=fp('U3','MIC2545A-1YM',108,90); ul,ur=105.3,110.7
for num,x,y,n in [(1,ul,88.095,iso),(2,ul,89.365,None),(3,ul,90.635,gnd),(4,ul,91.905,ilim),(5,ur,91.905,rail),(6,ur,90.635,load),(7,ur,89.365,rail),(8,ur,88.095,load)]:
    p=pad(u3,num,x,y,n) if n else pad(u3,num,x,y,gnd); p.SetNet(n);p.SetNetCode(n.GetNetCode() if n else 0)
rect(u3,97.05,87.4,102.95,92.6,pcbnew.F_CrtYd);rect(u3,97.15,87.5,102.85,92.5,pcbnew.F_SilkS)
jin=fp('JIN','SSD_3V3_SOURCE',120,100.635);pad(jin,1,120,100.635,rail,1,1)
jout=fp('JOUT','SSD_3V3_LOAD',120,96.5);pad(jout,1,120,96.5,load,1,1)
jg=fp('JGND','GND_RETURN',101,100.635);pad(jg,1,101,100.635,gnd,1,1)
r=fp('R15','76.8R_1PCT',101,95);pad(r,1,101,93.8,ilim,.8,.6);pad(r,2,101,96.2,gnd,.8,.6)
# Source escape uses the authorized local 0.15-mm rule, then ordinary via,
# B.Cu corridor, ordinary via, and F.Cu dogbone into EN; no via-in-pad.
tr(iso,(99.2,73.95),(99.2,84),F,FW);via(iso,99.2,84);tr(iso,(99.2,84),(104.2,86.8),B);via(iso,104.2,86.8);tr(iso,(104.2,86.8),(105.3,88.095),F)
# duplicated input and output joins are physical copper.
tr(rail,(ur,91.905),(114,91.905));tr(rail,(ur,89.365),(114,89.365));tr(rail,(114,89.365),(114,91.905));tr(rail,(114,91.905),(120,100.635))
tr(load,(ur,90.635),(111.5,90.635));via(load,111.5,90.635);tr(load,(ur,88.095),(111.5,88.095));via(load,111.5,88.095);tr(load,(111.5,88.095),(111.5,90.635),B);tr(load,(111.5,90.635),(116,90.635),B);via(load,116,90.635);tr(load,(116,90.635),(120,96.5))
tr(gnd,(ul,90.635),(103,90.635));tr(gnd,(103,90.635),(103,100.635));tr(gnd,(101,96.2),(103,96.2));tr(gnd,(103,96.2),(103,100.635));tr(gnd,(103,100.635),(101,100.635))
tr(ilim,(ul,91.905),(104.5,91.905));via(ilim,104.5,91.905);tr(ilim,(104.5,91.905),(100,91.905),B);via(ilim,100,91.905);tr(ilim,(100,91.905),(101,93.8))
edge(92.8,64.8,125,110)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
