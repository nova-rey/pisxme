"""V1597: stripped six-net orthogonal launch discriminator."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
base = H / "PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb"
out = H / "PHASE24_RTL9210B_ORTHOGONAL_LAUNCH_V1597.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)
V = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))
NETS = ("REFCLK_P", "REFCLK_N", "LANE0_RXP", "LANE0_RXN", "LANE0_TXN", "LANE0_TXP")
routes = (
    ("REFCLK_P", 70.4, 78.0, 80.0, 137.25),
    ("REFCLK_N", 70.8, 79.0, 81.2, 136.75),
    ("LANE0_RXP", 71.6, 80.0, 82.4, 134.25),
    ("LANE0_RXN", 72.0, 81.0, 83.6, 133.75),
    ("LANE0_TXN", 72.8, 82.0, 84.8, 135.25),
    ("LANE0_TXP", 73.2, 83.0, 86.0, 135.75),
)
b = pcbnew.LoadBoard(str(base))
for item in list(b.GetTracks()):
    if item.GetNetname() not in NETS:
        b.RemoveNative(item)
jh = b.FindFootprintByReference("JH1")
assert jh
for name, source_y, channel_y, handoff_x, target_x in routes:
    net = b.FindNet(name); assert net
    pad = next(p for p in jh.Pads() if p.GetNetname() == name)
    pad.SetPosition(V(handoff_x, source_y))
    source = next(s for s in b.GetTracks() if s.GetNetname() == name and s.GetLayer() == F)
    source.SetEnd(V(handoff_x, source_y))
    def via(x, y):
        q = pcbnew.PCB_VIA(b); q.SetPosition(V(x, y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
    def seg(a, z, layer):
        q = pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z)); q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
    via(handoff_x, source_y)
    seg((handoff_x, source_y), (target_x, source_y), B)
    seg((target_x, source_y), (target_x, channel_y), B)
    via(target_x, channel_y)
    seg((target_x, channel_y), (target_x, 62.725), F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(out))
print(out)
