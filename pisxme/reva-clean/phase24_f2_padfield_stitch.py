"""Disposable same-net F2 fuse-pad joins for the unpopulated B input branch."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"
OUT = ROOT / "PHASE24_F2_PADFIELD_STITCH.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def add(net_name, layer, a, z):
    n = b.FindNet(net_name)
    if n is None:
        raise RuntimeError(net_name)
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(layer)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(0.30))
    t.SetStart(p(*a))
    t.SetEnd(p(*z))
    b.Add(t)


# Each fuse side is joined as a compact four-pad field; no connection is
# invented between the raw and fused nets.
add("/POWER_INPUT/12V_IN_B", pcbnew.F_Cu, (43.6, 118.75), (43.6, 121.25))
add("/POWER_INPUT/12V_IN_B", pcbnew.F_Cu, (47.1, 118.75), (47.1, 121.25))
add("/POWER_INPUT/12V_IN_B", pcbnew.F_Cu, (43.6, 118.75), (47.1, 118.75))
add("/POWER_INPUT/FUSED_12V_B", pcbnew.F_Cu, (52.9, 118.75), (52.9, 121.25))
add("/POWER_INPUT/FUSED_12V_B", pcbnew.F_Cu, (56.4, 118.75), (56.4, 121.25))
add("/POWER_INPUT/FUSED_12V_B", pcbnew.F_Cu, (52.9, 118.75), (56.4, 118.75))

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
