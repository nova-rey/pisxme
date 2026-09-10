"""V1596: co-author QFN handoffs and monotonic J1 launch."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
base = H / "PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb"
out = H / "PHASE24_RTL9210B_COAUTHORED_LAUNCH_V1596.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)
V = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))

routes = (
    ("REFCLK_P", 70.4, 79.0, 80.0, 137.25),
    ("REFCLK_N", 70.8, 80.0, 81.2, 136.75),
    ("LANE0_RXP", 71.6, 82.0, 82.4, 134.25),
    ("LANE0_RXN", 72.0, 83.0, 83.6, 133.75),
    ("LANE0_TXN", 72.8, 85.0, 84.8, 135.25),
    ("LANE0_TXP", 73.2, 86.0, 86.0, 135.75),
)
b = pcbnew.LoadBoard(str(base))
jh = b.FindFootprintByReference("JH1")
assert jh

# Move the disposable handoff pads and their U1 source segments together.
for name, source_y, channel_y, handoff_x, target_x in routes:
    pad = next(p for p in jh.Pads() if p.GetNetname() == name)
    old = pad.GetPosition()
    pad.SetPosition(V(handoff_x, source_y))
    seg = next(s for s in b.GetTracks()
               if s.GetNetname() == name and s.GetLayer() == F
               and abs(pcbnew.ToMM(s.GetStart().x) - 94.05) < .01
               and abs(pcbnew.ToMM(s.GetStart().y) - source_y) < .01)
    seg.SetEnd(V(handoff_x, source_y))
    # Short source-side handoff, then a reserved B.Cu channel.
    via1 = pcbnew.PCB_VIA(b)
    via1.SetPosition(V(handoff_x, source_y)); via1.SetWidth(pcbnew.FromMM(.60)); via1.SetDrill(pcbnew.FromMM(.30))
    via1.SetLayerPair(F, B); via1.SetNet(b.FindNet(name)); via1.SetNetCode(b.FindNet(name).GetNetCode()); b.Add(via1)
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(handoff_x, source_y)); t.SetEnd(V(target_x, channel_y)); t.SetLayer(B); t.SetWidth(W); t.SetNet(b.FindNet(name)); t.SetNetCode(b.FindNet(name).GetNetCode()); b.Add(t)
    via2 = pcbnew.PCB_VIA(b)
    via2.SetPosition(V(target_x, channel_y)); via2.SetWidth(pcbnew.FromMM(.60)); via2.SetDrill(pcbnew.FromMM(.30))
    via2.SetLayerPair(F, B); via2.SetNet(b.FindNet(name)); via2.SetNetCode(b.FindNet(name).GetNetCode()); b.Add(via2)
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(target_x, channel_y)); t.SetEnd(V(target_x, 62.725)); t.SetLayer(F); t.SetWidth(W); t.SetNet(b.FindNet(name)); t.SetNetCode(b.FindNet(name).GetNetCode()); b.Add(t)

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(out))
print(out)
