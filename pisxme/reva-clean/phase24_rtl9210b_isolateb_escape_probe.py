"""Probe only the legal U1.12 pad-end escape on the accepted Path-B board."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_ISOLATEB_ESCAPE_PROBE.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
P = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))
W = pcbnew.FromMM(0.20)

b = pcbnew.LoadBoard(str(BASE)); n = b.FindNet("ISOLATEB")
u1 = b.FindFootprintByReference("U1"); p12 = u1.FindPadByNumber("12")
assert p12 and p12.GetNetname() == "ISOLATEB"

tp = pcbnew.FOOTPRINT(b); tp.SetReference("TP_ISO"); tp.SetValue("ISOLATEB_HANDOFF")
tp.SetLayer(F); tp.SetPosition(P(105, 78.5)); b.Add(tp)
pad = pcbnew.PAD(tp); pad.SetNumber("1"); pad.SetPosition(P(105, 78.5)); pad.SetSize(P(0.8, 0.8))
pad.SetShape(pcbnew.PAD_SHAPE_CIRCLE); pad.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
ls = pcbnew.LSET(); ls.AddLayer(F); pad.SetLayerSet(ls); pad.SetNet(n); pad.SetNetCode(n.GetNetCode()); tp.Add(pad)

def track(a, z, layer):
    q = pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
    q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

def via(x, y):
    q = pcbnew.PCB_VIA(b); q.SetPosition(P(x, y)); q.SetWidth(pcbnew.FromMM(0.6)); q.SetDrill(pcbnew.FromMM(0.3))
    q.SetLayerPair(F, B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

# Leave pad 12 through its south pad end, then transition outboard.
track((99.2, 73.5), (99.2, 74.6), F)
track((99.2, 74.6), (101.8, 74.6), F)
track((101.8, 74.6), (101.8, 78.5), F); via(101.8, 78.5)
track((101.8, 78.5), (105, 78.5), B); via(105, 78.5)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT)); print(OUT)
