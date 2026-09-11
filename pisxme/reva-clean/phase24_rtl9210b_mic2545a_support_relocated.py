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
u = fp("U3", "MIC2545A-1YM", 126, 86)
ul, ur = 123.3, 128.7
for num, x, y, n in [(1,ul,84.095,iso),(2,ul,85.365,gnd),(3,ul,86.635,gnd),(4,ul,87.905,ilim),
                     (5,ur,87.905,rail),(6,ur,86.635,ssd),(7,ur,85.365,rail),(8,ur,84.095,ssd)]:
    pad(u, num, x, y, n)
u.FindPadByNumber('2').SetNet(None); u.FindPadByNumber('2').SetNetCode(0)

r = fp("R15", "76.8R_1PCT", 121, 91)
pad(r, 1, 121, 89.8, ilim, .8, .6); pad(r, 2, 121, 92.2, gnd, .8, .6)
c = fp("C18", "100nF_IN_BYPASS", 130, 90)
pad(c, 1, 130, 89.2, rail, .8, .8); pad(c, 2, 130, 90.8, gnd, .8, .8)

# EN uses the authorized local fine escape, then a B.Cu route outside the
# existing CLKREQ_N and PEDET corridors, an ordinary via, and an F.Cu
# dogbone into U3.1; no via is placed in the support pad.
fine_seg(iso, (99.2,73.95), (98.35,74.8)); via(iso, 98.35, 74.8)
seg(iso, (98.35,74.8), (98.35,86.8), B)
seg(iso, (98.35,86.8), (122.2,86.8), B); via(iso,122.2,86.8)
seg(iso, (122.2,86.8), (123.3,84.095), F)
# Duplicate IN and OUT joins are explicit physical copper, not graph edges.
seg(rail, (128.7,87.905), (128.7,78)); via(rail,128.7,78); seg(rail,(128.7,78),(119.8,76.4),F)
seg(rail,(128.7,85.365),(128.7,78),B)
seg(rail,(130,89.2),(128.7,89.2)); seg(rail,(128.7,89.2),(128.7,87.905))
seg(ssd,(128.7,86.635),(130,86.635)); seg(ssd,(128.7,84.095),(130,84.095)); via(ssd,130,86.635); via(ssd,130,84.095)
seg(ssd,(130,84.095),(130,86.635),B); seg(ssd,(130,85.365),(130,64),B); via(ssd,130,64); seg(ssd,(130,64),(114.75,62.725),F)
seg(ilim,(123.3,87.905),(121,89.8))
seg(gnd,(123.3,86.635),(124.5,86.635)); seg(gnd,(124.5,86.635),(124.5,94))
seg(gnd,(124.5,94),(121,94)); seg(gnd,(121,94),(121,92.2))
seg(gnd,(124.5,94),(130,94)); seg(gnd,(130,94),(130,90.8)); via(gnd,124.5,94)
# Return along the outboard B.Cu perimeter to the existing authoritative
# board-GND transition; this avoids the occupied inner control corridors.
seg(gnd,(124.5,94),(140,94),B); seg(gnd,(140,94),(140,78),B)
seg(gnd,(140,78),(115.6,78),B)

pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
