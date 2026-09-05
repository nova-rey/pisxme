"""Disposable U4 layer-separated exposed-pad power-field experiment."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"
OUT = ROOT / "PHASE24_U4_LAYER_SEPARATED_POWER_STITCH.kicad_pcb"
board = pcbnew.LoadBoard(str(BASE))


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def track(net_name, layer, a, b, width=0.20):
    n = board.FindNet(net_name)
    if n is None:
        raise RuntimeError(net_name)
    t = pcbnew.PCB_TRACK(board)
    t.SetLayer(layer)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(width))
    t.SetStart(p(*a))
    t.SetEnd(p(*b))
    board.Add(t)


def via(net_name, x, y):
    n = board.FindNet(net_name)
    v = pcbnew.PCB_VIA(board)
    v.SetNet(n)
    v.SetPosition(p(x, y))
    v.SetWidth(pcbnew.FromMM(0.60))
    v.SetDrill(pcbnew.FromMM(0.30))
    board.Add(v)


ox, oy = 225.0, 105.0
# U4 protected-12V chain: a wide outer F.Cu dogleg avoids both the NC pad and
# the nearby PG_BRIDGE_3V3 route. This variant is a geometric discriminator;
# later board power distribution will use explicit plane launches.
track("12V_PROTECTED", pcbnew.F_Cu, (ox - 2.25, oy - 2.0), (ox - 3.50, oy - 2.0))
track("12V_PROTECTED", pcbnew.F_Cu, (ox - 3.50, oy - 2.0), (ox - 3.50, oy - 4.50))
track("12V_PROTECTED", pcbnew.F_Cu, (ox - 3.50, oy - 4.50), (ox + 5.50, oy - 4.50))
track("12V_PROTECTED", pcbnew.F_Cu, (ox + 5.50, oy - 4.50), (ox + 5.50, oy - 2.0))
track("12V_PROTECTED", pcbnew.F_Cu, (ox + 5.50, oy - 2.0), (ox + 2.25, oy - 2.0))
track("12V_PROTECTED", pcbnew.F_Cu, (ox + 5.50, oy - 2.0), (ox + 5.50, oy - 0.75))
track("12V_PROTECTED", pcbnew.F_Cu, (ox + 5.50, oy - 0.75), (ox + 2.25, oy - 0.75))

# Local POWER_GND field remains on F.Cu, separate from the B.Cu 12V route.
track("POWER_GND", pcbnew.F_Cu, (ox, oy - 1.125), (ox, oy + 1.125))
track("POWER_GND", pcbnew.F_Cu, (ox - 2.25, oy + 0.75), (ox, oy + 0.75))
track("POWER_GND", pcbnew.F_Cu, (ox, oy + 0.75), (ox + 2.25, oy + 0.75))

pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
