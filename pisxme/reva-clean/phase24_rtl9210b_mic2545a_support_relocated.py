"""Bounded local-support relocation probe for the accepted RTL9210B baseline."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_PATHB_ISOLATEB_SUPPORT_INTEGRATED.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
P = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))
W = pcbnew.FromMM(0.20)
FW = pcbnew.FromMM(0.15)
b = pcbnew.LoadBoard(str(BASE))

def net(name):
    n = b.FindNet(name)
    if n: return n
    n = pcbnew.NETINFO_ITEM(b, name); b.Add(n); return n

def fp(ref, value, x, y):
    q = pcbnew.FOOTPRINT(b); q.SetReference(ref); q.SetValue(value)
    q.SetLayer(F); q.SetPosition(P(x, y)); b.Add(q); return q

def pad(q, num, x, y, n, sx=1.55, sy=.60):
    p = pcbnew.PAD(q); p.SetNumber(str(num)); p.SetPosition(P(x, y))
    p.SetSize(P(sx, sy)); p.SetShape(pcbnew.PAD_SHAPE_ROUNDRECT)
    p.SetRoundRectRadiusRatio(.18); p.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
    p.SetLocalSolderMaskMargin(pcbnew.FromMM(0)); p.SetLocalSolderPasteMargin(pcbnew.FromMM(-.05))
    ls = pcbnew.LSET(); ls.AddLayer(F); p.SetLayerSet(ls)
    p.SetNet(n); p.SetNetCode(n.GetNetCode()); q.Add(p)

def seg(n, a, z, layer=F):
    q = pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
    q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

def fine_seg(n, a, z, layer=F):
    q = pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
    q.SetWidth(FW); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

def via(n, x, y):
    q = pcbnew.PCB_VIA(b); q.SetPosition(P(x, y)); q.SetWidth(pcbnew.FromMM(.7)); q.SetDrill(pcbnew.FromMM(.35))
    q.SetLayerPair(F, B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

iso, rail, ssd, gnd, ilim = [net(x) for x in ("ISOLATEB", "RTL_3V3", "SSD_3V3", "GND", "MIC2545_ILIM")]

# Relocated coherent support island: lower/outboard of the U1 south-row field.
u = fp("U3", "MIC2545A-1YM", 108, 90)
ul, ur = 105.3, 110.7
for num, x, y, n in [(1,ul,88.095,iso),(2,ul,89.365,gnd),(3,ul,90.635,gnd),(4,ul,91.905,ilim),
                     (5,ur,91.905,rail),(6,ur,90.635,ssd),(7,ur,89.365,rail),(8,ur,88.095,ssd)]:
    pad(u, num, x, y, n)
u.FindPadByNumber('2').SetNet(None); u.FindPadByNumber('2').SetNetCode(0)

r = fp("R15", "76.8R_1PCT", 102, 95)
pad(r, 1, 102, 93.8, ilim, .8, .6); pad(r, 2, 102, 96.2, gnd, .8, .6)
c = fp("C18", "100nF_IN_BYPASS", 115, 94)
pad(c, 1, 115, 93.2, rail, .8, .8); pad(c, 2, 115, 94.8, gnd, .8, .8)

# EN uses the authorized local fine escape, then a B.Cu route outside the
# existing CLKREQ_N and PEDET corridors, an ordinary via, and an F.Cu
# dogbone into U3.1; no via is placed in the support pad.
fine_seg(iso, (99.2,73.95), (98.35,74.8)); via(iso, 98.35, 74.8)
seg(iso, (98.35,74.8), (98.35,86.8), B)
seg(iso, (95.5,86.8), (104.2,86.8), B); via(iso,104.2,86.8)
seg(iso, (104.2,86.8), (105.3,88.095), F)
# Duplicate IN and OUT joins are explicit physical copper, not graph edges.
seg(rail, (110.7,91.905), (112,91.905)); seg(rail,(110.7,89.365),(112,89.365)); seg(rail,(112,89.365),(112,91.905)); via(rail,112,91.905)
seg(rail,(112,91.905),(112,78.5),B); via(rail,112,78.5); seg(rail,(112,78.5),(113.8,76.4),F)
seg(rail,(115,93.2),(114,93.2)); seg(rail,(114,93.2),(114,91.905))
seg(ssd,(110.7,90.635),(111,90.635)); seg(ssd,(110.7,88.095),(111,88.095)); via(ssd,111,90.635); via(ssd,111,88.095)
seg(ssd,(111,88.095),(111,90.635),B); seg(ssd,(111,89.365),(111,64),B); via(ssd,111,64); seg(ssd,(111,64),(114.75,62.725),F)
seg(ilim,(105.3,91.905),(102,93.8)); seg(gnd,(102,96.2),(100,96.2)); via(gnd,100,96.2)
seg(gnd,(105.3,90.635),(104,90.635)); via(gnd,104,90.635); seg(gnd,(104,90.635),(104,84),B); seg(gnd,(104,84),(114.4,84),B); seg(gnd,(114.4,84),(114.4,77.2),B)
seg(gnd,(115,94.8),(117,94.8)); via(gnd,117,94.8)

pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
